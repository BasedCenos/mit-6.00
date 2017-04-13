##def nestEgg(salary, save, growth, years):
##    b = []
##    b.append(salary * save * 0.01)
##    if years != 1:
##        current = 0
##        
##        return nestEggFixed(salary,save,growth, years, b)
##    else: return b
##def nestEggFixed(salary, save ,growth, years,b):
##    
##    b.append(b[-1]*(1+0.01*growth)+salary*save*0.01)
##    
##    if len(b) != years:
##        
##        nestEggFixed(salary,save,growth,years, b)
##    return b
##
##def fakeEgg(salary,save,growth,years):
##    answer = [0]
##    for each in range(0,years):
##        print(answer[-1])
##        temp = answer[-1]*(1+0.01*growth)+salary*save*0.01
##        answer.append(temp)
##    
##    return answer

####salary     = 10000
####save       = 10
####growthRate = 15
####years      = 5
####a = nestEgg(salary, save, growthRate, years)
####
####print(a)


def variableEgg(salary, save, growth):
    b = []
    b.append(salary * save * 0.01)
    if len(growth)-1 != 1:
        current = 1
        
        return testVar(salary,save,growth, current, b)
    else: return b
def testVar(salary, save ,growth, current, b):
    
    b.append(b[-1]*(1+0.01*growth[current])+salary*save*0.01)
    current += 1
    if len(b) != len(growth):
        
        testVar(salary,save,growth,current, b)
    return b

##salary      = 10000
##save        = 10
##growth = [3, 4, 5, 0, 3]
##a = variableEgg(salary, save, growth)

def postRetirement(savings, growth, expenses):
    a = [savings]
    for i in range(len(growth)):
        temp = a[-1]*(1+0.01*growth[i])-expenses
        a.append(temp)
    del a[0]
    return a
##savings     = 100000
##growth = [10, 5, 0, 5, 1]
##expenses    = 30000
##a = postRetirement(savings, growth, expenses)
##
def testMax(salary, save, preRetire, postRetire, epsilon):
    a = variableEgg(salary, save, preRetire)[-1]
    first = 0
    last = a + epsilon
    return findMaxExpenses(a, postRetire, epsilon, first, last)
def findMaxExpenses(savings, postRetire, epsilon, first, last):
    
    mid = first + ((last - first) / 2)
##    print(mid)
    b = postRetirement(savings, postRetire, mid)
##    print(b[-1])
    if abs(b[-1]) > epsilon:
        if b[-1] >= epsilon:
            return findMaxExpenses(savings, postRetire, epsilon, mid, last)
        else: return findMaxExpenses(savings, postRetire, epsilon, first, mid)
       
    return mid, b[-1]

salary = 10000
save = 10
preRetire = [3, 4, 5, 0, 3]
postRetire = [10, 5, 0, 5, 1]
epsilon = 1
a,b = testMax(salary, save, preRetire, postRetire, epsilon)




