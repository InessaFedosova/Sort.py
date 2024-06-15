a = [0, 1, 2, 3]
b = [4, 5, 6, 7]

res = a + b

#Используем метод пузырька
for i in range(len(res)-1):
    for j in range(len(res)-1-i):
        if res[j] < res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]
print(res)