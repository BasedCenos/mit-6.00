##Hello world
import string
def Stringy(string, search):
    b = [] 
    return Stringy1(string, search, 0 , b)

def Stringy1(string, search, start, b):
    if str.find(string, search, start) == -1:
        return b
    temp = str.find(string, search, start)
    b.append(temp)
    
    if temp < len(string)-1:
        Stringy1(string, search, temp + 1, b)
    
    return b
    

##def countSubStringMatch(target, key):
##    loop = True
##    a = 0
##    start = 0
##    while loop:
##        if str.find(target, key, start) != -1:
##            a += 1
##            start = str.find(target,key,start)+1
##        if str.find(target,key,start) == -1:
##            loop = False
##    return a        

def tuple2(string, search):
    a = tuple(Stringy(string, search))
    return a

target2 = 'atgaatgcatggatgtaaatgcag'
key = 'atg'
