#1:
for x in range(0,151):
    print(x)

#2:
for x in range(1,1001):
    if (x % 5 == 0):
        print(x)

#3:
for x in range(1,100):
    if(x % 10 == 0):
        print("Coding Dojo")
    elif(x % 5 == 0):
        print("Coding")
    else:
        print(x)

#4:
sum = 0
for x in range(0,500001):
    if(x % 2 == 1):
        sum += x
print(sum)

#5:
for x in range(2018,0,-4):
    print(x)

#6:
def flexibleCounter(lowNum,highNum,mult):
    highNum += 1
    for num in range(lowNum,highNum,1):
        if(lowNum >= highNum):
            print("Value of lowNum must be lower than value of highNum")
        if(num % mult == 0):
            print(num)


x = flexibleCounter(2,9,3)
print(x)
