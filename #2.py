n = [1,6,-5,8,3,7,1,2,4]

larg_sum = cur_sum = n[0]

for i in range (1, len(n)):
    cur_sum = max(n[i],  cur_sum + n[1])
    larg_sum = max(larg_sum, cur_sum)
print(larg_sum)