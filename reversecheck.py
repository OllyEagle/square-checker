power = 2
maxVal = 100000
results = []

def splitString(inString):
    return [char for char in inString]

def reverseFn(inNum):
    numArr = splitString(str(inNum))
    revNumArr = numArr[::-1]
    num = ''
    for i in range(0, len(revNumArr)):
        num += revNumArr[i]
    return int(num)

def splitString(inString):
    return [char for char in inString]

filename = "power"+str(power)+"maxVal"+str(maxVal)+".txt"
file = open(filename,'w')

for i in range(1,maxVal):
    num1 = i
    num2 = reverseFn(num1)

    if((num1**power) == reverseFn(num2**power)):
        file.writelines(str(num1) + "^2 reversed is " + str(num2) + "^2\n")

file.close()
