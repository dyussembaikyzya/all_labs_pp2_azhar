def permutations(some):
    n = len(some)
    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end=" ")
        print()
a = str(input( ))
permutations(a)