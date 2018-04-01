def testReadFile(file):
    """
    :rtype: object
    """
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        print(line.encode("utf-8"))


"""返回指定区间的素数"""


def getSu(start, end):
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                k = i / j;
                print(i, "==", j, "*", k)
                break;
            else:
                continue
        if i == j + 1:
            print(i, "is prime number !")
