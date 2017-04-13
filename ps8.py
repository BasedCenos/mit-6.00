# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

sub_file = "subjects pset 8.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    d = dict()
    count = 0
    for line in inputFile:
        temp = line.strip('\n').split(',')
        for i in range(1,len(temp)):
            temp[i] = float(temp[i])
        a = temp.pop(0)
        d[a]= tuple(temp)
        count += 1
        
    return d

##a = loadSubjects(sub_file)
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    sorted(subNames)
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

def value_work(dictionary):
    memo = {}
    return value_work_memo(dictionary, memo)
def value_work_memo(dictionary, memo):
    
    for subject in dictionary.keys():
        if dictionary[subject] in memo.keys():
           
            temp = memo[dictionary[subject]]
            new_temp = []
            for item in temp:
                new_temp.append(item)
            new_temp.append(subject)
            
         
            memo[dictionary[subject]] = new_temp
            continue
        a = [subject]
        memo[dictionary[subject]] = a
        
    return memo


def mergeSort1(value_work_dict):
    vw = []
    for i in value_work_dict:
        vw.append(i)
    return mergeSort(vw)

def mergeSort(vw):
    if len(vw) < 2:
        return vw[:]
    else:
        mid = len(vw) // 2
        left = mergeSort(vw[:mid])
        right = mergeSort(vw[mid:])
        together = merge(left,right)
        
        return together
def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if cmpRatio(left[i],right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


    
## Problem 2: Subject Selection By Greedy Optimization
##a = loadSubjects(sub_file)
##vw = value_work(a)
##b = mergeSort1(vw)




def greedyAdvisor(v_w_dict,maxWork,comparator):
    subject = {}
    starting_work = maxWork
    for i in v_w_dict:
        for j in v_w_dict:
            if i in subject:
                break
            if i != j:
                if comparator(v_w_dict[i],v_w_dict[j]) and maxWork - v_w_dict[i][WORK] > 0 and i not in subject:
                    maxWork -= v_w_dict[i][WORK]
                    subject[i] = v_w_dict[i]
                    
                else:
                    if maxWork - v_w_dict[j][WORK] > 0 and j not in subject:
                        subject[j] = v_w_dict[j]
                        maxWork -= v_w_dict[j][WORK]
    print(starting_work - maxWork)
    return subject
    

##Z = greedyAdvisor(test_load, 63, cmpRatio)





def greedyAdvisor1(v_w, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    subjects = []
    for k,i in enumerate(v_w):
        if maxWork - i[1] > 0:
            subjects.append(i)
            maxWork -= i[1]
        if maxWork <= 5:
            print(k)
            return subjects
    
    return subjects
##subjects = greedyAdvisor1(b,100)
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    dp_dict = {}
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0, dp_dict)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork, dp_dict):
    # Hit the end of the list. if new path is better than current best, return it.
    #otherwise return best
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)

            if (i+1,subsetValue + s[VALUE]) not in dp_dict:
#### if path with item isn't in dp_dict, run that test.
                bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK], dp_dict)
            ### add the result into the dictionary
                dp_dict[i+1,bestSubsetValue] = bestSubset
    ### get value from the dictionary
            else:
                bestSubset, bestSubsetValue = dp_dict[(i+1, subsetValue + s[VALUE])],subsetValue + s[VALUE]
            subset.pop()

        if (i+1,subsetValue) not in dp_dict:

            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork, dp_dict)

            dp_dict[(i+1,subsetValue)] = bestSubset

        else:
            tempSet, tempValue = dp_dict[(i+1,subsetValue)], subsetValue

            if tempValue > bestSubsetValue:
                return tempSet, tempValue

        return bestSubset, bestSubsetValue


def bruteyfrooty(subjects, maxWork):

    classes = list(subjects.keys())
    vW = list(subjects.values())
    memo = {}
    return brootisfrootis(classes, vW, len(vW)-1, [], 0, None, None, maxWork, memo)

def brootisfrootis(classes, vW, i, subset, subsetValue, bestSubset, bestValue, work, memo):

    if i == 0:
        if subsetValue > bestSubset or bestSubset  == None:
            return subset[:], subsetValue
        else: return bestSubset, bestValue
    s = classes[i]     
    if maxWork - vW[i - 1][WORK] > 0:
        if (i, subsetValue + s[VALUE]) not in memo:
           bestSubset, bestValue = \
                       brootisfrootis(classes, vW, i - 1, subset, subsetValue + s[VALUE], bestSubset, bestValue, work - s[WORK], memo)
           memo[(i-1, bestValue)] = bestSubset
        else: bestSubset, bestValue = memo[(i-1, subsetValue + s[VALUE])], subsetValue + s[VALUE]
    if (i, subsetValue) not in memo:
        bestSubset, bestValue = brootisfrootis(classes, vW, i - 1, subset, subsetValue, bestSubset, bestValue, work, memo)
        memo[(i-1,subsetValue)] = bestSubset
    else:
        tempSet, tempValue = memo[(i-1,subsetValue)], subsetValue

    if tempValue > bestValue:
        return tempSet, tempValue

    return bestSubset, bestValue




#
# Problem 3: Subject Selection By Brute Force
import time

test_load = loadSubjects(sub_file)
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    start_time = time.time()
    answer_dict = bruteForceAdvisor(test_load,100)
    end_time = time.time()
    print(end_time - start_time)
    return answer_dict

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
