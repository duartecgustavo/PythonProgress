def fatorial (num):
    f=1
    for c in range(1, num+1):
        f*=c
        print(f)
    return f

def dobro(num):
    num+=num
    return num

def triplo(num):
    return num * 3