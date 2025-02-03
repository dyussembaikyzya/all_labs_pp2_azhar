def histogram(arr):
    for i in arr:
        print('*' * i)
n = input("n = ")
m = list(map(int,n.split()))
histogram(m)
