num = [1,7,5,9,4,8]
for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j] > num[j +1]:
            tem = num[j]
            num[j] = num[j + 1]
            num[j+1] = tem
print(num)
