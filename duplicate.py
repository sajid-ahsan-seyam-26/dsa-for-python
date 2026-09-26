def find_duplicate(num):
    n=len(num)
    
    for i in range(n):
        for j in range(i+1,n):
            if num[i]==num[j]:
                return num[i]
            
num=[4,2,7,2,9]
result=find_duplicate(num)
print("duplicate find",result)

