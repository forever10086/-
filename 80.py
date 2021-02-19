# 有一个大文件，输出这个大文件有多少行，而且可以找到任意行的文本
"""
with open("largefile.txt", "r",encoding="utf-8") as f:
    hang = 0  # 文件有多少行
    file_len_list = []  # 文件每一行有多长
    line = f.readline()
    while line: # 这种方法要求文件是同类型字符
        file_len_list.append(len(line))
        print(len(line), ":", end="")
        print(line, end="")
        hang = hang + 1
        line = f.readline()
    print("\n")
    print(file_len_list)
    print(hang)

    aim = int(input("请输入想要输出行的行号："))
    f.seek(sum(file_len_list[:aim]))
    print(f.readline())
"""

### 用f.tell()与f.seek()来求，使用二进制模式来打开文件
"""with open("test.txt", "r", encoding="utf-8") as f:
    hang = 0  # 文件有多少行
    i = f.tell()
    line = f.readline()
    j = f.tell()
    l = [j - i]
    while line:
        key1 = f.tell()
        print(line, end="")
        hang = hang + 1
        line = f.readline()
        key2 = f.tell()
        l.append(key2 - key1)
    print("")
    print(hang)
    print(l)
    while 1:
        aim = int(input("请输入想要输出行的行号：若想退出，请输入-1"))
        if aim == -1:
            print("退出查找")
            break
        if aim <= hang:
            f.seek(sum(l[:aim - 1]))
            print(f.readline())
        else:
            print("所想输出行超出文件行数，即文件不存在该行")
"""

with open("test.txt", "rb") as f:
    hang = 0  # 文件有多少行
    i = f.tell()
    line = f.readline()
    j = f.tell()
    l = [j - i]
    while line:
        key1 = f.tell()
        print(line.decode("utf-8"),end="")
        hang = hang + 1
        line = f.readline()
        key2 = f.tell()
        l.append(key2 - key1)
    print("")
    print(hang)
    print(l)
    while 1:
        aim = int(input("请输入想要输出行的行号：若想退出，请输入0："))
        if aim == 0:
            print("退出查找")
            break
        if aim <= hang:
            f.seek(sum(l[:aim - 1]))
            # decode()方法以encoding指定的编码格式解码字符串。默认编码为字符串编码。
            print(f.readline().decode(encoding="utf-8"))
        else:
            print("所想输出行超出文件行数，即文件不存在该行")
