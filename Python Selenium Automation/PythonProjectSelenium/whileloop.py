it = 7
while it>1:
    if it ==3: #starts from 7, when it becomes 3 loop exits for break statement
        break
    print(it)
    it = it - 1
print("break statement executed")


#Continue to skip current iteration

# when point becomes 4 , 4==4 then skips rest all statement, point doesn't decrement anymore. So it enters into 
# infinite loop. o/p : 9 8 7 5 . to avoid this need to decrement it before continue statement.
points = 10
while points>0:
    if points == 7:
        points -=1
        continue 
    # if points ==2:
    #     break
    print(points)
    points -=1

print("continue statement executed")

point = 9
while point>1:
    if point == 4:
        continue # when point becomes 4 , 4==4 then skips rest all statement, point doesn't decrement anymore. So it
                    #enters into infinite loop. o/p : 9 8 7 5 
    print(point, end=" ")
    point = point-1
point("continue statement executed")