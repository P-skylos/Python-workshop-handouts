#booleans
#booleans are anything that returns either a true or a false, note that true and false are equivalent to 1 and 0
#examples:
3>4 == False
1 == True
0+1 == True
'a' in 'abc' == True

#iterables
#These are anything you can use in the definition of a for loop
#examples
"this string is iterable"
[1,2,3,6]
range(8)
("tuples", "are", "also", "iterable")

# to get a specific element from an iterable we use square brackets
"hello world"[3] == 'l'

#Dictionaries!
#dictionaries are made of key:value pairs where the key is sort of the "name" for the value
dict = {'a':'a value', 'b':'another value', 'c':'another value'}
dict[a] == 'a value'
#note dictionaries are not ordered
{'a':'a value', 'b':'another value', 'c':'another value'} == {'a':'a value', 'c':'another value', 'b':'another value'}
#to add a value to a dictionary
dict['new val'] = 'a value'

#loops
#loops are useful anytime you need to do something multiple times,
#if you need to do something with every item in a list you can use
for i in list:
#or
for i in range(len(list)):

#example: finding the max element in a list of numbers
def for_loop_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

#if you need to keep doing something until a certain point use
while condition:

#example: max of a list of numbers
def while_loop_max(list):
    i = 0
    max = list[0]
    while i < len(list):
        if i > max:
            max = i
        i+=1
    return max

#functions
#functions are also useful when you have to do something multiple times
#but are more like variables than loops in that you can call a function anywhere to reuse that piece of code.
#Similar to how a variable is replaced by its value a function is replaced by whatever it returns
# in other
# define a function by saying:
def funcname(args):
    pass #use pass to say there's no code here while keeping python happy
         #python needs a codeblock after a colon which pass satisfies
# or by saying
lambda x: x+3
#note if we want to reuse a lambda we have to give it a name by binding it to a variable name
new_func = lambda x: x+3 #guess what this does
#this is why i say functions are like variables
#note if we asked for new_func's value (ie print(new_func)) we would get some arcane thing with a bunch of numbers and letters, that's the actual function object

#to call a function and get something useful we have to use parentheses
new_func(3) #this gives us an actual value

#recursion is when you call a function inside itself
#this is useful for something like the fibbonaci sequence which we define as follows
#F(0) = 1
#F(1) = 1
#F(n) = F(n-1)+F(n-2)
#see how we've described the fibbonaci sequence in terms of decremented iterations of itself?
#but we couldn't just say F(n) = F(n-1)+F(n-2)
#we need two known cases otherwise we would just keep asking what F(n-1) is forever down to negative infinity
#that's why we give it F(0) and F(1) which we call the BASE CASES
# and F(n) = F(n-1)+F(n-2) is the INDUCTIVE CASE
#its kind of similar to a proof by induction

#here's what that looks like in python code

def fibbonaci(n):
    if n==0:      
        return 1
    if n==1:
        return 1
    if n < 0:
        print("oh no! fibbonaci only works on positive numbers!")
        return None
    return fibbonaci(n-1) + fibbonaci(n-2)

#those if statements at the top of the function that sheck for our base cases are called GUARD CLAUSES. Notice how we can also use guard clauses to check for bad inputs
#then after the guard clauses we do our inductive case (or sometimes, cases)
#we always have to have the guard clauses first because they protect the function from running away, try calculating fibbonaci(n-1) + fibbonaci(n-2) at the top of the function instead and see what goes wrong.

#now here's how to use recursion to do the samething as those loops

def recursion_max(list, index=0, max_so_far=0):
    if index >= len(list):
        return max_so_far
    if index == 0 or list[index] > max_so_far: 
        max_so_far = list[index]
    return max_of_num_list(list, index+1, max_so_far)

#here our guard clause checks that we haven't gone past the end of the list
#then our inductive case checks to see if we have a new max, which happens if we're at the start of the list or if the current value in the list is greater than the max so far
#we then return the max of the list starting from the next index

#notice how we had to carry around extra data to keep track of what we were doing? that's fine to do, but in this case we didn't have to. we can write this another way like so:
def alt_recursion_max(list):
    if len(list) == 1:
        return list[0]
    return max(list[0], alt_recursion_max(list[1:]))

#which takes advantage of a builtin function: max(a,b) which returns the greater number between a and b
#here we say the maximum of a one element list is that element, and the maximum of a multi-element list is the greater element between the first element and the maximum of the rest of the list
#you might say why not just use a loop
#and you can, but see how much shorter this recursive version is, and at least by a subjective measure its much more mathematically elegant which is why programmers like recursion

