def palindrome(value):
    temp = str(value)
    temp = int(temp[::-1])
    return(value == temp)

def isPrime(value):
    if(value % 2 == 0 and value != 2):
        return(False)
    i = 3
    while(i*i <= value):
        if(value % i == 0):
            return(False)
        i += 1
    return(True)

def getValue(value):
    if(palindrome(value)):
        if(isPrime(value)):
            print(value)
            return(True)

start = 100000000
last = 999999999
count = 0

for i in range(999999999, 100000000, -1):
    if(getValue(i)):
        count += 1
    if(count == 3):
        break
