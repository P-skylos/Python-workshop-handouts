# this document contains a bunch of snippets
# meant to test and build your intuitions about how python works.
# in general you should look at a given code snippet
# and predict what it does, then check that prediction
# by copy and pasting the snippet to run it in the python shell
# the shell is what comes up when you type python3 into the terminal/command line

#there will be some exercises at the end of some of these sections.
#I've included a couple example answers to those exercises at the end of the file


# indexing:
#what will the following lines return?
"Hello World!"[3]

['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!'][3]

{0:'H', 1:'e', 2:'l', 3:'l', 4:'o', 5:' ', 6:'W', 7:'o', 8:'r', 9:'l', 10:'d', 11:'!'}[3]

{'zero':'H', 'one':'e', 'two':'l', 'three':'l', 'four':'o', 'five':' ', 'six':'W', 'seven':'o', 'eight':'r', 'nine':'l', 'ten':'d', 'eleven':'!'}['three']

#loops
#predict the output of each of these for loops
for i in "Hello World!":
    print(i)

for i in [0,1,2,3,4,5,6,7,8]:
    print(i)

for i in range(9):
    print(i)

for i in range(len("Hello world")):
    print(i)

for i in {0:'H', 1:'e', 2:'l', 3:'l', 4:'o'}:
    print(i)

#predict the output of these while loops
#note that not all of these end
i = 0
while i < 9:
    print(i)
    i+=1

i = 0
while i < 9:
    i+=1
    print(i)

i = 9
while i > 0:
    print(i)
    i+=1

string = "Hello"
i=0
while i < len(string):
    print(i)

string = "Hello"
i=0
while i < len(string):
    print(i)
    i+=1

string = "Hello"
i=0
while i < len(string):
    print(string[i])
    i+=1



#exercise: try rewriting some of the for loops as while loops and vice versa

#booleans
def true_false(bool):
    if bool:
        print('true')
    else:
        print('false')

true_false(3>4)

true_false(False == True)
true_false(True == True)

true_false(0)
true_false(1)

true_false((3>4) + (4>3))
true_false((3>4) or (4>3))

true_false((3>4) * (4>3))
true_false((3>4) and (4>3))

counter=0
for i in range(10):
    counter += int(True)
print(counter)

#exercises
#write a funcion that runs through a list and decrements every even number (no if statements)
#write a function that increments even numbers by 1 and subtracts 3 from odd numbers (still no if statements)

#functions
#to test this section don't for get to run the function defs and variable assignments
#before calling the functions
x = "this is string x"
y = "this is string y"
a = "this is string a"
b = "this is string b"

def f1(x):
    print(x)

f1(x) #what does this print?
f1(y) #what does this print?
#was it what you expected? if not this case might be more intuitive:
f1(a) #what does this print?
f1(b) #what does this print?


def f2(x,y):
    print((x,y))

f2(y,x) #what do we expect this to print?
f2(a,b)

# the lesson here is that once were inside the function that's
# the name that matters even if its the same data
# when we call f1(a) the data in a "this is string a"
# gets mapped to the variable x inside f1


#classes
#don't forget to run the class defs before running the other stuff
class BaseClass():
    variable_we_control = 0
    baseClass_var = 3

    def __init__(self, user_val):
        print("base class init")
        self.variable_user_sets = user_val

    def display_vars(self):
        print(self.variable_we_control)
        print(self.variable_user_sets)

    def display_home(self):
        print("I'm defined in BaseClass!")

bc = BaseClass(5)
bc.display_vars() #what do we predict here?

class Incrementable(BaseClass): #the class we inherit from goes inside the parens
    # notice how we don't define an __init__ since BaseClass already has one
    increment_count = 0
    incrementableClass_var = 0

    def increment_by(self, n):
        self.variable_we_control += n
        self.variable_user_sets += n
        self.increment_count += 1


    def display_vars(self):
        super().display_vars() #note how we don't need to pass in self
        print("variables have been incremented" + str(self.increment_count) + "times")

    def display_home(self):
        print("I'm defined in IncrementableClass!")

ic = IncrementableClass(5)
ic.display_vars() #what do you think gets printed

bc.display_home() #what should this print?
ic.display_home() #what does this print?

bc.baseClass_var #this should return 3
ic.incrementableClass_var #this returns 0
bc.incrementableClass_var #this causes an error
ic.baseClass_var #what do you think this does?

# The point of this section is to build some intuition for inheritance.
# You'll notice that for ic.display_vars it does everything bc.display_vars() does and a little bit more
# that's the utility of super(), it lets us extend and reuse code from the class we inherit from
# in this case we overwrite display_vars in order to extend it but still preserve the original functionality

#comparing bc.display_home() and ic.display_home() we see that we have completely overwritten
#the base class function by redefining it in IncrementableClass without using super

#for the final 4 statements where we look at variables you'll see that IncrementableClass still inherits the baseClass_var





#loop rewrites:
for i in "Hello World!":
    print(i)
# can be rewritten
string = "Hello World!"
counter = 0
while counter < len(string):
    i = string[counter]
    print(i)
    counter+=1

#and the loop:
string = "Hello"
i=0
while i < len(string):
    print(i)
    i+=1
#can be rewritten
for i in range(len(string)):
    print(i)

#boolean exercise 1:
def make_odd(list):
    for i in range(len(list)): #note we need to index in to the list for our desired side effect
        list[i] -= (list[i]%2)== 0
    return list
