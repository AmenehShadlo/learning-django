
num=int(input())

numbers=list(range(1,num+1))

print(numbers)

for i in range(1,num + 2):
    print(numbers[len(numbers) - 1:-i:-1])

for i in range(num +2):
    print(*numbers[len(numbers) - 1:i:-1])


