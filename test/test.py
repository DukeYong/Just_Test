class test(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print self.a
        print self.b

    def __call__(self,a ,b):
        self.a = a
        self.b = b

if __name__ == '__main__':
    instance = test(1,2)
    instance.show()
    try:
        assert '__call__' in dir(test), "no __call__ method"
        instance(3,4)
        instance.show()
    except AssertionError, e:
        print "no __call__ method"
        print e