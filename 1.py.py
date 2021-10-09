try:
    n = int(input('Insert the amount of elements in the array'))
    array = []
except ValueError:
    print('Invalid data')
    exit()
else:
    for i in range(n):
        array.append(int(input('Full in the array')))
    print('array is', array)
    print('Insert delta')
    delta = int(input())
    check = [min(array) - delta, min(array) + delta]
    ans = array.count(check[0]) + array.count(check[1])
    print("Output:", ans)
    