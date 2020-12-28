class SegmentTree:
    def __init__(self, size, f=lambda x, y: x + y, default=0):
        self.size = 2 ** (size - 1).bit_length()
        self.default = default
        self.dat = [default] * (self.size * 2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i * 2], self.dat[i * 2 + 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        left_res, right_res = self.default, self.default
        while left < right:
            if left & 1:
                left_res = self.f(left_res, self.dat[left])
                left += 1

            if right & 1:
                right -= 1
                right_res = self.f(self.dat[right], right_res)
            left >>= 1
            right >>= 1
        res = self.f(left_res, right_res)
        return res