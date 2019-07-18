def palindrome(num):
    num = str(num)
    s = []
    for i in range(len(num)):
        s.append(num[i])
        if s[i] != num[-1-i]:
            return False
    return True

def palindrome2(num):
    rev = 0
    n = num
    while num > 0:
        l = num % 10
        rev = (rev * 10) + l
        num = num // 10
    if rev == n:
        return True
    return False


if __name__ == '__main__':
    num = int(input().strip())
    print(palindrome(num))
    print(palindrome2(num))