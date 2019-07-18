def rev(num):
    num = str(num)
    s = ''
    sign = ''
    for i in range(len(num)):
        if num[i] == '-':
            sign += num[i]
        elif num[i] == 0 and i == len(num)-1:
            pass
        else:
            s = num[i]+s
    if len(sign) == 1:
        s = sign + s
    s = int(s)
    return s

if __name__ == '__main__':
    num = int(input().strip())
    print(rev(num))