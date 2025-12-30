

def two_numb(L, target):
    n = len(L)
    
    for i in range(n):
        for j in range(i + 1, n):
            if L[i] + L[j] == target:
                return [i, j]

L = [2,8,6,1,5,3,9,7,4]
target = 8
output = two_numb(L, target)
print(output)
