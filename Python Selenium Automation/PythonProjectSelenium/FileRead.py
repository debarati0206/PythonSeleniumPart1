file = open("test.txt")
# print(file.read(3))
print(file.readline())
file.close()
print("--------------------")

with open('test.txt','r') as f:
    lines = f.read()
    print(lines, end="")

print("--------------------")
   
file = open('test.txt')
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

print("---------------")
file = open('test.txt')

for line in file.readlines():
    print(line)
file.close()
print("---------------")
file = open('test.txt')
print(file.readlines())
file.close()