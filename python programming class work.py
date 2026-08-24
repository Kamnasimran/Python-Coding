Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
scores = [88,89,79,97,59,40]

print(scores[1:4])
[89, 79, 97]
print(scores[0:6:2])
[88, 79, 59]

letters = ['a', 'b', 'c', 'd', 'e']

print(letters[1:3])
['b', 'c']
print(len(letters[1:3]))
2

nums = ]0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SyntaxError: unmatched ']'

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[0:10:2])
[0, 2, 4, 6, 8]
print(nums[1:8:3])
[1, 4, 7]
print(nums[::-1])
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

word = 'PYTHON'
print(word[::2])
PTO
print(word[::-1])
NOHTYP
NOHTYP
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    NOHTYP
NameError: name 'NOHTYP' is not defined

original = [10, 20, 30, 40, 50]
fragment = original[1:4]

fragment.append(999)

print
<built-in function print>

readings = [12.5, 13.1, 11.8, 14.2, 15.0, 13.7, 12.9, 16.1]

first_half = readings[:4]
second_half = readings[4:]
every_other = readings[::2]
reversed_r = readings[::-1]

print(first_half)
print(second_half)
print(every_other)
print(reversed_r)
print(readings)
SyntaxError: multiple statements found while compiling a single statement


given data = [5, 10, 15, 20, 25, 30, 35, 40]
SyntaxError: invalid syntax

scores = [5, 10, 15, 20, 25, 30, 35, 40]

print(scores[::3])
[5, 20, 35]

scores = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(scores[0:4])
[1, 2, 3, 4]

scores = [5, 10, 15, 20, 25, 30, 35, 40]

print(scores[0:3])
[5, 10, 15]

scores = [5, 10, 15, 20, 25, 30, 35, 40]

print(scores[5:])
[30, 35, 40]

scores = [5, 10, 15, 20, 25, 30, 35, 40]

print(scores[


scores = [22.5, "error", 23.0, 21.8, "error"]
SyntaxError: '[' was never closed

sensor_data = [22.5, "ERROR", 23.0, 21.8, "ERROR", 24.5]
print(sensor_data)
[22.5, 'ERROR', 23.0, 21.8, 'ERROR', 24.5]

sensor_data = [22.5, "ERROR", 23.0, 21.8, "ERROR"]

sensor_data.remove("ERROR")

print(sensor_data)
[22.5, 23.0, 21.8, 'ERROR']

count = 1
while count <= 5:
    print(count)
    count += 1

    
1
2
3
4
5
5
5

count = 1
while count <= 5:
    print(count)
    count += 1
print('Done!')
SyntaxError: invalid syntax
while count <= 5:
    print(count)
    count += 1
print('Done!')
SyntaxError: invalid syntax

count = 1
while count <= 5:
    print(count)
    count += 1

    
1
2
3
4
5
print('Done!')
Done!

cats = ['Tom', 'Whiskers', 'Luna']

for cat in cats:
    print(cats, 'says meow')

    
['Tom', 'Whiskers', 'Luna'] says meow
['Tom', 'Whiskers', 'Luna'] says meow
['Tom', 'Whiskers', 'Luna'] says meow
for letter in 'AI':
    print(letter)

    
A
I

cats = ['Tom', 'Whiskers', 'Luna']

for cat in cats:
    print(cat, 'says meow')

    
Tom says meow
Whiskers says meow
Luna says meow

for letter in 'AI':
    print(letter)

    
A
I

numbers = [0, 0, 2, 4, 6, 8]
for Num in numbers:
    if Num==0:
        numbers.reserve(0)

        
Traceback (most recent call last):
  File "<pyshell#113>", line 3, in <module>
    numbers.reserve(0)
AttributeError: 'list' object has no attribute 'reserve'. Did you mean: 'reverse'?
File "<pyshell#113>", line 3, in <module>
SyntaxError: invalid syntax

for i in range(5):
    print(i, 'Hello!')

    
0 Hello!
1 Hello!
2 Hello!
3 Hello!
4 Hello!

for day in range(1, 5):
    print('Day', day)

    
Day 1
Day 2
Day 3
Day 4

for num in range(1, 10):
    if num == 5:
        break
    print(num)

    
1
2
3
4

for num in range(1, 6):
    if num == 3:
        pass
    print(num)

    
1
2
3
4
5

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

    
1
2
4
5

for cat in cats:
    print(cat)
    print('---')
print('done')
SyntaxError: invalid syntax

for cat in cats:
    print(cat)
    print('---')

    
Tom
---
Whiskers
---
Luna
---


print('done!')
done!

for num in [2, 4, 6, 8]:
    if num % 2 != 0:
        break
else:
    print('All numbers were even.')

    
All numbers were even.

>>> enrolled = ['Asha', 'Raj', 'Meera', 'Kabir']
>>> target = 'Meera'
>>> 
>>> for name in enrolled:
...     if name == target:
...         print(target, 'found!')
...         break
... else:
...     print(target, 'not found in the list']
...     
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> 
>>> enrolled = ['Asha', 'Raj', 'Meera', 'Kabir']
>>> target = 'Meera'
>>> 
>>> for name in enrolled:
...     if name == target:
...         print(target, 'found!')
...         break
... else:
...     print(target, 'not found in the list')
... 
...     
Meera found!
>>> 
>>> numbers = [4, 9, 15, 22, 7, 3, 18]
>>> for i in range(0, 31, 3):
...     print(i)
... 
...     
0
3
6
9
12
15
18
21
24
27
30
