import os

for i in range(126):
    for j in range(65, 70):
        folder = "C:/Dropbox/vscode/AtCoder/AtCoder/ABC/ABC" + ("000" + str(i))[-3:]
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = folder + "/ABC" + ("000" + str(i))[-3:] + chr(j) + ".py"
        f = open(path, 'w')
        f.write('')  # 何も書き込まなくてファイルは作成されました
        f.close()