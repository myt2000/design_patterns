class A(object):
    pass

if __name__ == '__main__':
    a = A()
    b = A()

    print(id(a) == id(b))
    print(a, b)
'''
False
<__main__.A object at 0x0000025432EF7548> <__main__.A object at 0x00000254356A11C8>
'''