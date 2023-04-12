from random import randint

#dictionaries can have functions in them!
powers={1:lambda x: x, 2: lambda x: x*x, 3:lambda x: x*x*x}
powers[3](2)

# python can do a clever thing called list comprehensions
[i for i in range(10)]
#equiv to:
list = []
for i in range(10):
    list.append(i)

#ternary statements (one line if else):
print("true") if True else print(false) #note you need both an if and an else for this

#you can pass functions around like objects and also return them
def dice_maker(sides):
    def die():
        return randint(1,sides)
    return die

def function(logger):
    logger("hey we logged something!")

def write_to_file(path):
    def writer(content):
        file = open(path, 'a')
        file.write(content)
        file.close()
    return writer

function(print)
function(write_to_file("log.txt"))
