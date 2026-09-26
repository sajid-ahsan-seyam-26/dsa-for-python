def two_sum(num, target):
    n = len(num) #list er mot upadan ber kora 
    for i in range(n): #first loop first number ber korar jonno
        for j in range(i + 1, n):
            if num[i] + num[j] == target:
                return [i, j]  # target না ফিরিয়ে ইনডেক্স [i, j] রিটার্ন করতে হবে

num = [8, 7, 11, 15]
target = 19

result = two_sum(num, target)
print("result is ", result)  # result() এর বদলে শুধু result হবে