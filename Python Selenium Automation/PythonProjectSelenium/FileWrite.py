with open('test.txt', 'r') as reader:
    content = reader.readlines()
    print(reversed(content))
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

with open('test.txt', 'r') as file:
    for line in file.readlines():
        print(line)           
