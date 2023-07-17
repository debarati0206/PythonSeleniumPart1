import selenium
from selenium import webdriver

print("Hello")

a = 12;
print(type(a))

a,b,c = 1,1.2,'Abc'
print(a)
print(b)
print(c)
print("value is "+str(a)) 
print("{} {}".format("value is",a))


list = [1,2.21,"List"]
print(list)
print(list[0]) #0th index value
print(list[-1]) # last index value
print(list[:1]) # from 0th to (1-0) th index value
list.insert(2,"new value") #INSERT
print(list)
list.append(3) #append value at the end
print(list)
del list[4] #Delete
print(list)
list[3] = "LIST" #update
print(list)

tuplee = (1,2.21,"tuple",1)
print(tuplee.count(1))
# tuplee[2]='abc' --give error as immutable

dic= {1:"firstname" ,2:"lastname", "age":25}
print(dic["age"])
print("{} {}".format("The age is",dic["age"]))

dict = {}
dict["class"] = "IX"
dict["Stu_name"] = "Sumi"
print(dict)