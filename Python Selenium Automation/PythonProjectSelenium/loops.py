num=[1,2,3,3]
for i in num:
    print(i)

sum = 0
for j in range(1,11):
    sum+=j
print(sum)


for i in range(1,11,2):
    print(i)


print("while loop starting")
p = 4
while p>1:
    print(p, end="  ")
    p = p -1 
print()
print("While loop executed")


print("while loop2 starting")
p = 5
while p>1:
    if p!= 3: #skips 3 in series
        print(p, end="  ")
    p = p -1 
print()
print("While loop2 executed")



n = 7
while n>1:
    if n==5:
        n=n-1
        continue
    if n==3:
        break
    print(n)
    n -=1
print("**************")
n = 7
while n>0:
    if n!=3:
        print(n)
    n -=1


