class InitTest1(object):
    _global_attr = {"one", "two", "three"}

    '''__init__方法带除self外的参数时，实例化对象时必须也传入相应类型的参数，否则不会执行该__init__方法'''

    def __init__(self, local_attr1):
        self._global_attr = {"_global_attr"}
        self.local_attr1 = local_attr1
        self.local_attr2 = {"local_attr2"}

    def printSelf(self):
        print(self._global_attr)
        print(self.local_attr1)
        print(self.local_attr2)


test = InitTest1({"spring", "cloud"})
test.printSelf()
print(test.local_attr1)
print(test.local_attr2)
