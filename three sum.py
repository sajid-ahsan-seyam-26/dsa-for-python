def three_sum(num,target):
    n=len(num)
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if num[i]+num[j]+num[k]==target:
                    return[i,j,k]
                
num=[1,4,2,10,5]
target=7

result=three_sum(num,target)
print("result",result)