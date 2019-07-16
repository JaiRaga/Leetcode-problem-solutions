def lis(arr,target):
    v = 0
    ind1 = 0
    ind2 = 0
    for i in arr:
        if i < target:
            v = target - i
            if arr.count(v) != 0 and arr.count(v) != arr.index(i):
                ind1 = arr.index(i)
                ind2 = arr.index(v)
                return ind1, ind2


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    target = int(input().strip())
    print(lis(arr, target))

