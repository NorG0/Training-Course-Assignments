from email.policy import default
from enum import unique


def printStars(n):
    for i in range(1, len(n)+1):
        for j in range(0, i):
            print(n[j], end=' ')
        print()

#a = printStars(n=[1,2,3,4,5])


def printSumofFractorial(n):
    sum = 0
    for i in range(n, 0, -1):
        sum += i
    return  sum


def condition5(list):
    for ele in list:
        if ele == 150: continue
        elif ele > 500: break
        elif ele % 5 == 0: print(ele)


def countNumbers(num):
    count = 0
    while(1):

        num = num//10
        count += 1
        if(num//10 == 0) : count += 1; break

    print(count)


def triangle(n):
    for i in range(n, 0 , -1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print()

def reverse(list):
    for i in range(len(list)-1,-1,-1):
        print(list[i], end=' ')

def primeNumbers():
    for i in range(25,51,1):
        for j in range(2,10,1):
            if(i%j == 0): break
        else:
            print(i)

def fibonacci():
    num1 = 0
    num2 = 1
    print(num1)
    for i in range(10):
        fibo = num1 + num2
        num2 = num1
        num1 = fibo

        print(fibo)

def oddindex(list):
    for i in range(1,len(list),2):
        print(list[i])

def sumSeries(n, num):
    sum_temp = 0
    sum = 0
    for i in range(1,n+1,1):
        sum_temp = sum_temp * 10 + num
        sum+= sum_temp
    return  sum

def printvalues(**kwargs):
    for i in kwargs:
        print(i)

def oddevenlist(l1,l2):
    l_odd = l1[1::2]
    l_even = l2[0::2]

    return l_odd + l_even

def occurencesElements(list):
    count_dic = dict()
    for i in list:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1

    return count_dic

def listpair(l1,l2):
    return set(zip(l1,l2))

def intersectionEles(l1,l2):
    l1 = set(l1)
    l2 = set(l2)

    inter = l1.intersection(l2)
    for i in inter:
        l1.remove(i)
    return l1

def checksubset(s1,s2):
    s1 = set(s1)
    s2 = set(s2)


def removeEles(l,dict1):
    l[:] = [item for item in dict1.values() if item in l]
    return l

def removeduplicates(dict1):
    check_list = list()
    for item in dict1.values():
        if item not in check_list:
            check_list.append(item)
    return check_list
   # return set(dict1.values())

def listfuncs(l):
    uniq_list = list(dict.fromkeys(l))
    tupl_list = tuple(l)
    minValue = min(l)
    maxValue = max(l)

    return  minValue, maxValue, uniq_list,tupl_list

def modlist(l):
    l1 = l
    l = [1,2,3]
    print(l, l1)

def newString(s1, s2):
    s2 = s2[::-1]
    rs = ""
    length = len(s1) if (len(s1) > len(s2)) else len(s2)
    for i in range(length):
        if i >= len(s1) or i >= len(s2):
            break
        else:
            rs = rs+ s1[i] + s2[i]
    return  rs

def stringBalanced(s1,s2):
    for char in s1:
        if char not in s2: return False
    return True

def findStrCount(s1, s2):
    rs = s1.lower().count(s2.lower())
    return rs

def sumSTRdigits(str):
    rs = 0
    count = 0.0
    for c in str:
        if c.isdigit():
            count += 1
            rs += int(c)
    return rs, rs/count

def countChar(str):
    rs = dict()
    count = 0
    for c in str:
        count = str.lower().count(c.lower())
        rs[c] = count
        count = 0
    return rs

def reversestr(s):
    return s[::-1]

def findstrIndex(str, findstr):
    last_pos = 0
    # Indexing way to solve
    # for i in range(0,len(str),1):
    #     if str[i] == findstr[0]:
    #         for j in range(i,i+len(findstr),1):
    #             if str[j] != findstr[j-i]:
    #                 break
    #             else:
    #                 last_pos = i

    # Check string way the same
    for i in range(0,len(str) - len(findstr) + 1,1):
        if str[i:i+len(findstr)] == findstr:
            last_pos = i

    #Using Rfind
    last_pos = str.rfind(findstr)

    return last_pos

def checkDigit(str):
    rs = ''
    rs = "".join([item for item in str if item.isdigit()])
    return rs

def checkbothDigitsAlphabet(str):
    rs = []
    split_str = str.split(' ')
    for item in split_str:
        if any( char.isalpha() for char in item ) and any(char.isdigit() for char in item):
            rs.append(item)
    return rs



l1 = ["1","3","4","5"]
l2 = ["Jimmy","Jane"]

l3 = [i + j for i,j in zip(l1,l2)]

num = [1,2,3,4]
num1 = [5,6,7,8]

# print([item*item for item in num1 ])
# print([i+j for i in l1 for j in l2])


list1 = ["a","b",["c",["d","e",["f","g"]]]]
list1[2][1][2].extend(["h","j","k"])


key = ['ten', 'nine', 'seven']
values = [1,9,7]

def convert2list(l1,l2):
    dict1 = dict()
    for i in range (len(l1)):
        dict1.update({l1[i] : l2[i]})

    return dict1

def merge2dict(dic1, dic2):
    return {**dic1, **dic2}

# print(merge2dict({'a':1,'b':2},{'c':3,'d':4}))


d = {'a':1,'b':2, 'c':{'name': 'Jim', 'add': 'no1 A street'}}


employees = ['Kelly','Emma']
defaults = {"designation":'Developer',"salary":8000}

rs = dict.fromkeys(employees,defaults)


def extract_dict(sample_dict, keys):
    rs_dict = {}
    for key in keys:
        if key in sample_dict:
            rs_dict.update({key:sample_dict[key]})

    rs_dict = { key:sample_dict[key] for key in keys if key in sample_dict}

    return rs_dict


def remove_keyIndict(sample_dict,keys):
    for key in keys:
            sample_dict.pop(key)
    return  sample_dict

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
#print(remove_keyIndict(sample_dict,keys))

def findvalue(sample_d, value):
    if value in sample_d.values():
       return True
    return False

sample_dict["location"] = sample_dict.pop("city")

sample_dict1 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
a = sample_set.update(sample_list)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40}

set1.difference_update(set2)
#print(set1)
#print(set1.symmetric_difference_update(set2))

t1 = (11, 22, 33, 44, 55, 66)

t2 = t1[3:5]
print(t2)
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

tuple1[1][2] = 50
tuple11 = (50, 10, 60,[50,10,2], 70, 50)
print(tuple11.count(50))
print(tuple1)
a,b,c = tuple1

tuple3 = (11, 22)
tuple4 = (99, 88)

tuple3,tuple4 = tuple4,tuple3

































