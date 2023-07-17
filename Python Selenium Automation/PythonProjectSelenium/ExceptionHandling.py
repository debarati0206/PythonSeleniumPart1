#NEED OF TRY _ EXCEPT --try -except is used in cases like - while doing automation of any website there may or may
# not be popups. In try block you have written code to click on the popup button. If popup is not there, it'll throw
# error. To avoid interrupted execution we use try - except block where the exception is catched in except block.

'''NEED OF FINALLY - > let's suppose you've written statements to create record in try block and if there's any exception
while validating the data it'll be catched at except block. There's requirements to delete all junk data at the end. 
and you write code for that at the end. But if the code fails in the try block it'll be catched at except and will 
not go below to clean up the junk records. so when there's such requirement that you dont want to store all this 
data after this try-except write finally block for cleaning up records. '''

'''By this way before reaching to the next test all the junk data or cookies accepted will be deleted which you've 
mentioned to delete in finally block.'''

ItemsinCart =1

# if ItemsinCart !=2:
#     raise Exception("not fulfilled requirement")

'''assert(ItemsinCart == 2) # assertion condition inside () if not fulfilled will give assertion error.'''


try:
    with open('test.txt') as f:
        print(f.readline())
except Exception as e:
    print(e)

try:
    with open('tests.txt') as f:
        print(f.readline())
except Exception as e:
    print(e)

try:
    with open('test.txt') as f:
        print(f.readline())
except Exception as e:
    print(e)

finally:
    print("Cleaning up records")

