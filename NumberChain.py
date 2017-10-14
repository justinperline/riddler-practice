import random

#Checks if a number is a factor of another number
def check_factor(firstnum, secondnum):
    if firstnum % secondnum == 0:
        return True
    else:
        return False
    pass

#Checks if a number is a multiple of another number
def check_multiple(firstnum, secondnum):
    if secondnum % firstnum == 0:
        return True
    else:
        return False
    pass

#Checks if a number is either a factor or multiple of another number
def check_numbers(firstnum, secondnum):
    if check_factor(firstnum, secondnum) is True or check_multiple(firstnum, secondnum) is True:
        return True
    else:
        return False
    pass

#Generates a random number from 1 to 100, inclusive
def gen_random():
    return random.randint(1,100)
    pass

#Checks if the number has already appeared in the list
def check_use(num, list):
    if num in list:
        return False
    else:
        return True
    pass

###########################################################
#Begin Program
chain = []
counter = 0

while True:
    #Deletes the contents of the chain on every iteration
    del chain[:]
    #Begins with a random start point
    num_start = gen_random()
    chain.append(num_start)

    for i in range(1,5000):
        #Loops through the numbers 1-to-100 5000 times to ensure no possible integer is missed
        num_pending = gen_random()
        if check_numbers(chain[-1], num_pending) is True and check_use(num_pending, chain) is True:
            chain.append(num_pending)

    print("Length of Chain is: {}" .format(len(chain)))
    counter += 1
    if len(chain) > 49:
        #Number above is desired minimum chain length needed to break loop. Set for current record holder
        break

print(chain)
print("Created {} chains" .format (counter))

