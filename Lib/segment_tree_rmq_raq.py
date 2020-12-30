class SegmentTreeRangeAdd:
    def __init__(self, size, f=lambda x, y: min(x, y), default=2 ** 31 - 1):
        self.size = (size - 1).bit_length()
        self.no = 2 ** self.size
        self.default = default
        self.data = [default] * (self.no * 2)
        self.lazy = [None] * (self.no * 2)
        self.f = f

    def get_index(self, left, right):
        l_left = (left + self.no) >> 1
        r_right = (right + self.no) >> 1
        lc = 0 if left & 1 else (l_left & -l_left).bit_length()
        rc = 0 if right & 1 else (r_right & -r_right).bit_length()
        for i in range(self.size):
            if rc <= i:
                yield r_right
            if l_left < r_right and lc <= i:
                yield l_left
            l_left >>= 1
            r_right >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i - 1]
            if v is None:
                continue
            self.lazy[2 * i - 1] += v
            self.data[2 * i - 1] += v
            self.lazy[2 * i] += v
            self.data[2 * i] += v
            self.lazy[i - 1] = 0

    def update(self, left, right, x):
        *ids, = self.get_index(left, right)
        self.propagates(*ids)
        l_left = self.no + left
        r_right = self.no + right
        while l_left < r_right:
            if r_right & 1:
                r_right -= 1
                self.lazy[r_right - 1] += x
                self.data[r_right - 1] += x
            if l_left & 1:
                self.lazy[l_left - 1] += x
                self.data[l_left - 1] += x
                l_left += 1
            l_left >>= 1
            r_right >>= 1
        for i in ids:
            self.data[i - 1] = self.f(self.data[2 * i - 1], self.data[2 * i])

    def query(self, left, right):
        self.propagates(*self.get_index(left, right))
        l_left = self.no + left
        r_right = self.no + right

        res = self.default
        while l_left < r_right:
            if r_right & 1:
                r_right -= 1
                res = self.f(res, self.data[r_right - 1])
            if l_left & 1:
                res = self.f(res, self.data[l_left - 1])
                l_left += 1
            l_left >>= 1
            r_right >>= 1
        return res
