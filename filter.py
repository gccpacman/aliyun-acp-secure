import os
import glob

# for filename in os.listdir(os.getcwd()):
for filename in glob.glob('*.txt'):
    with open(filename, encoding="utf-8") as f:
        cline = f.readline()
        # print(cline)
        if cline == "云顶云，值得信赖的云服务商！\n":
            print(filename)
        # break;