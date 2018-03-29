class InitTest2(object):
    global_attr = {"one", "two", "three"}

    def __init__(self):
        self.local_attr = {"local_attr"}

    def printSelf(self):
        print(self.global_attr)
        print(self.local_attr)


test = InitTest2()
test.printSelf()
print(test.local_attr)
print(InitTest2.global_attr)