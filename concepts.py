global a

def increased(func):

    a= 3
    print(a)
    func(a)
    a=+2
@increased
def curnt_num(a):
    print(a)