##Finding the percentages
'''if __name__ == '__main__':
    n = int(input("Enter numbers: "))
    student_data ={}
    print("Enter stundent data: ")
    for _ in range(n):
        name, *line = input().split()
        marks = list(map(float, line))
        student_data[name]=marks
    user_query = input("enter user query: ")
    avg=0
    for key, value in student_data.items():
        if key == user_query:
            avg = sum(value)/len(value)
    print(f'{avg:.2f}')
            '''

##Tuple
'''n=int(input())
data = tuple(map(int, input().split()))
print(hash(data))'''


##largest value in list
'''n=int(input("enter array size: "))
array = []
for _ in range(n):
    ele = input()
    array.append(ele)
print(array)
array.sort()
print(array)
print(max(array))
print(min(array))'''

#Second largest in aray
'''array = list(input("enter array element: ").split())
array.sort()
print(array[1])
'''
## Reverse a string with slicing
'''str1 = "This is Anku Srivastava"
print(str1)
str2 = str1[::-1]
print(str2)
str3 = str1.split()
print(str3)
str4=""
for i in str3: 
    i=i[::-1]
    str4+=i
    str4+=" "
print(str3)
print(str4)
'''
##Reverse a string without slicing
'''str1 = "This is Anku Srivastava"
str2=""
for i in range(len(str1)-1, -1, -1):
    str2+=str1[i]

str3= str1.split()
str4=""
for i in str3:
    str_temp = ""
    for j in range(len(i)-1, -1, -1):
        str_temp+=i[j]
    str4+=str_temp
    str4+=" "
print(str2)
print(str4)'''

##Check if a number is prime
'''num = int(input("Enter a number: "))
print(int(num **0.5)+1)
if num >1:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''

##Find Factorial using recursion
'''def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
    
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {fact(num)}")
'''
##Check Palindrome (string or Number)
'''def CheckPalindrome(item):
    left, right = 0, len(item)-1
    is_palindrome = True
    while left < right:
        if item[left] != item[right]:
            is_palindrome=False
            break
        left+=1
        right-=1
    return is_palindrome

if __name__ == '__main__':
    item = input("Enter Item for Checking Palindrome: ")
    answer = CheckPalindrome(item)
    print("The status of palindome is ", answer)'''


## Count Vowel in string
'''def CountVowel(item):
    count = 0
    for i in string1:
        if i == 'a':
            count+=1
        elif i == 'e':
            count+=1
        elif i == 'i':
            count+=1
        elif i == 'o':
            count+=1
        elif i == 'u':
            count+=1
        else:
            continue
    return count

if __name__ == '__main__':
    string1 = str(input("Enter string: "))
    print(CountVowel(string1))'''



#l1= [int(ele) for ele in input().split()]
'''l1= [1,2]
l1.append("Anku")
l1.insert(0, "Raj")
print(l1)
hold = l1.pop()
print(l1, hold)
l1.remove("Raj")
print(l1)
l2=l1.copy()
print(l2)
print(l1.count(1))
print(l1.index(1))
l3 = l1.reverse()
print(l3)
l1.clear()
print(l1)
l3=[4,5]
l4= l1.extend(l3)
print(l4)
'''
## Set 
'''s={3,1, 6,2,8}
s1={9,7,5,1,2,4}
print(s | s1)
print(s.update(s))
print(s)'''

##Dictionary
'''d= {"name":["anku", "Sona", "tanu"], "age":[26, 23, 21]}
print(d.keys())
print(d.values())
print(d.items())
#print(d.fromkeys("name"))
print(d.get("name"))
print(d.get("age"))
print(d.update({"qualifications":['bca', 'mca', 'ba']}))
print(d.items())
print(d.pop("name"))
print(d)
print(d.popitem())
print(d)'''

#string
'''s="anku"
s1="Srivastava"
s3 = s+" "+s1
print("into this") if "anku" in s3 else print("isn't into")
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.replace("a", "B"))
print(s.find('k'))
print(s1.count('a'))
print(s.startswith('a'))
print(s.endswith('u'))
l1=[1,2,3]
s4=' '.join(['1','2','3'])
print(s4)
'''

## Second minimum in list
'''l1 = [3,2,4,1,7,5]
mini_2 = 99999
mini_1 = 99999
for i in range(len(l1)):
    if l1[i] < mini_1:
        mini_1=l1[i]
print(mini_1)
for i in range(len(l1)):
    if l1[i] > mini_1 and l1[i] < mini_2:
        mini_2=l1[i]
print(mini_2) '''

## Nested List
'''if __name__ == '__main__':
    n = int(input())
    student_data =[]
    for _ in range(n):
        name = input()
        marks = float(input())
        l=[name, marks]
        student_data.append(l)
    minimum_score = 99999
    second_minimum_score = 99999
    for i in student_data:
        if i[1] < minimum_score:
            minimum_score = i[1]
    for i in student_data:
        if i[1] > minimum_score and i[1] < second_minimum_score:
            second_minimum_score = i[1]

    data = []
    for i in student_data:
        if i[1] == second_minimum_score:
            data.append(i[0])
    data.sort()
    for i in data:
        print(i)'''

## Capitalize

def solve(s):
    return '-'.join(s.split())



if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)


    



    



