def zero():
    return 'zero'
def one():
    return 'one'
def indirect(i):
    switcher={
            0:zero,
            1:one,
            2:lambda:'two'
            }
    func=switcher.get(i,lambda :'Invalid')
    return func()

print(indirect(1))




def somefunc(i):
    switcher={
            "GG":zero,
            "ICI":one,
            "PICI":lambda:'two'
            }
    func=switcher.get(i,lambda :'Invalid')
    return func()

print(somefunc("PICI"))