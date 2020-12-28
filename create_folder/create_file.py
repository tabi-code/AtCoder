import os

for i in range(126, 200):
    for j in range(65, 71):
        folder = "C:/Dropbox/vscode/AtCoder/AtCoder/ABC/ABC" + ("000" + str(i))[-3:]
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = folder + "/ABC" + ("000" + str(i))[-3:] + chr(j) + ".py"
        f = open(path, 'w')
        f.write('')
        f.close()