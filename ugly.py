#reverse an int: 321->123 (32bits)

def purely_procedural(x):
    """reverse an int: 321->123 (32bits) """
    z=[None]*10 #this becomes the reverse of the input
    y=str(x)
    a=10-len(y) #
    a='.'*a     #
    y=a+y       # these 3 lines pad out the length to 10
    #copying in reverse order
    z[0]=y[-1]
    z[1]=y[-2]
    z[2]=y[-3]
    z[3]=y[-4]
    z[4]=y[-5]
    z[5]=y[-6]
    z[6]=y[-7]
    z[7]=y[-8]
    z[8]=y[-9]
    z[9]=y[-10]
    zz = '' #this becomes a string version of z
    zz+=z[0]
    zz+=z[1]
    zz+=z[2]
    zz+=z[3]
    zz+=z[4]
    zz+=z[5]
    zz+=z[6]
    zz+=z[7]
    zz+=z[8]
    zz+=z[9]
    out=zz.split('.')
    return int(out[0])


def variabled(forward):
    """reverse an int: 321->123 (32bits) """
    backward=[None]*10
    forward_str=str(forward)
    padding_length=10-len(forward_str)
    padding='.'*padding_length
    forward_string=padding+forward_str
    backward[0]=forward_str[-1]
    backward[0]=forward_str[-1]
    backward[1]=forward_str[-2]
    backward[1]=forward_str[-2]
    backward[2]=forward_str[-3]
    backward[2]=forward_str[-3]
    backward[3]=forward_str[-4]
    backward[3]=forward_str[-4]
    backward[4]=forward_str[-5]
    backward[4]=forward_str[-5]
    backward[5]=forward_str[-6]
    backward[5]=forward_str[-6]
    backward[6]=forward_str[-7]
    backward[6]=forward_str[-7]
    backward[7]=forward_str[-8]
    backward[7]=forward_str[-8]
    backward[8]=forward_str[-9]
    backward[8]=forward_str[-9]
    backward[9]=forward_str[-10]
    backward[9]=forward_str[-10]
    backward_str = ''
    backward_str+=backward[0]
    backward_str+=backward[1]
    backward_str+=backward[2]
    backward_str+=backward[3]
    backward_str+=backward[4]
    backward_str+=backward[5]
    backward_str+=backward[6]
    backward_str+=backward[7]
    backward_str+=backward[8]
    backward_str+=backward[9]
    out=backward_str.split('.')
    return int(out[0]) #now you dont need those comments as much


def looped(forward):
    """reverse an int: 321->123 (32bits) """
    forward_str=str(forward)
    padding_length=10-len(forward_str)
    padding='.'*padding_length
    forward_string=padding+forward_str
    backward=[None]*10 #moved this down to loop so its easier to find
    for i in range(10):  #now you dont have to look at those blocks of code
        backward[i]=forward_str[-(i+1)]
    backward_str = ''
    for i in range(10):
        backward_str+=backward[i]
    out=backward_str.split('.')
    return int(out[0])

def looped_renamed(forward):
    """reverse an int: 321->123 (32bits) """
    forward=str(forward)
    padding_length=10-len(forward)
    padding='.'*padding_length
    forward_string=padding+forward
    backward=[None]*10
    for i in range(10):
        backward[i]=forward[-(i+1)]
    backward_str = ''
    for i in range(10):
        backward_str+=backward[i]
    out=backward_str.split('.')
    return int(out[0])


def looped_and_functioned():
    """reverse an int: 321->123 (32bits) """
    backward=[None]*10
    forward = pad_left(str(forward), '.', 10) #kind of trivial but see how the function name preserves meaning while reducing clutter
    for i in range(10):
        backward[i]=forward[-(i+1)]
    backward_str = ''
    for i in range(10):
        backward_str+=backward[i]
    out=backward_str.split('.')
    return int(out[0])

def pad_left(string, pad_char, target_length):
    padding_length = target_length - len(string)
    padding = padding_length * pad_char
    return padding + string


def looped_w_thought(forward):
    """reverse an int: 321->123 (32bits) """
    forward=str(forward)
    backward=[None] * len(forward) # we can just put these in a variable ask them to spot that
    for i in range(len(forward)):
        backward[i]=forward[-(i+1)]
    backward_str = ''
    for i in range(len(forward)):
        backward_str+=backward[i]
    out=backward_str.split('.')
    return int(out[0])


def brained(forward):
    """reverse an int: 321->123 (32bits) """
    forward = str(forward)
    backward=''
    for i in range(10):
        backward+=forward[-(i+1)]
    return int(backward)


def big_brained(forward):
    string = str(forward)
    reversed = string[::-1] #this is just a faster way of doing our earlier for loop
    return int(reversed)
