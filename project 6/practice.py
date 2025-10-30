'''my_list = list(input())

for index in range(len(my_list)):
    if int(index)%2 == 0: 
        print(my_list[index])'''

'''my_list = list(input())

for index in range(len(my_list)):
    if int(index)%2 != 0: 
        print(my_list[index]) '''

'''num_1 = int(input())
num_2 = int(input())
my_list = []
for  number in range(num_1,num_2+1):
    if number % 2 == 0:
        my_list.append(number)

print(my_list) '''

'''my_list = []
n = int(input())
while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = (3*n)+1
    my_list.append(n)

print(my_list)'''

'''my_list = []
num = int(input())
for number in range (1,(num//2)+1):
        if num % number == 0:
            my_list.append(number)
my_list.append(num)

print(my_list)'''

'''my_list = [10,12,13,14,15,22,79]
max_even = -1
for number in my_list:
    if number % 2 == 0:
     if number >= max_even:
        max_even = number

print(max_even)'''
word = input()
def is_isogram():
    letters_seen = {}
    for letter in word:
        if letter == letters_seen:
            return False
        letters_seen[letter] = True
    return False
