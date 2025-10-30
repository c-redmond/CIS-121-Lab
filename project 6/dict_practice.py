'''
#1
letter_dict = {}
user_input = input()
for letter in user_input:
    if letter in letter_dict:
        letter_dict[letter] = 2
    else:
        letter_dict[letter] = 1

if 2 in letter_dict.values():
    print(False)
else:
    print(True)

    
    #3
num_dict = {}
user_input = input()
for number in user_input:
    if number in num_dict:
        num_dict[number] = 2
    else:
        num_dict[number] = 1

for key, value in num_dict.items():
    if value ==1:
        print(key)

        #4
names = {}
for key, value in names.items():
    print(value)


#5
people = {}
age = 0
for value in people.values():
    if value >= age:
        age = value

for key, value in people.items():
    if value == age:
        print(key)



def majority_element(nums):
nums = [4,5,6,7,7,7,8,9]
nums_dict = {}
for number in nums:
    if number in nums_dict:
            nums_dict[number] += 1
    else:
        nums_dict[number] = 1
    for key, value in nums_dict.items():
        if value >= (len(nums)/2):
            return key
for key, value in nums_dict.items():
    print(key, value)

#14
employee_salary = {}
cut_off = int(input())
for key, value in employee_salary.items():
    if value >= cut_off:
        print(key)

#15
donations = { "John": 100, "Sarah": 200, "Mike": 50}
total = 0
for value in donations.values():
    total += value

print(total)'''


print("type anything here")