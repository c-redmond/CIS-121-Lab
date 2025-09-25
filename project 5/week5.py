#Charles Redmond

def pyramid_volume(base,height):
    volume = (base**2)*height/3
    return volume


#question 8
def pool_times(grade,time):

    time = ''
    if grade == 'K':
        grade = 0
    if grade == "k" or grade == "1" or grade == "2" or grade == "3":
        if time == "morning":
            pool_time = "9 am"
        elif time == "afternoon":
            pool_time = "1 pm"
    elif 4 <= int(grade) <= 8:
        if time == "morning":
            pool_time = "10 am"
        elif time == "afternoon":
            pool_time = "2 pm"
    elif 9 <= int(grade) <= 12:
        if time == "morning":
            pool_time = "11 am"
        elif time == "afternoon":
            pool_time = "3 pm"
    return pool_time



#question 11

def conver_knuts(knuts):
    galleons = knuts // (29*17)
    remaining_knuts = knuts - (galleons * 29 * 17)
    sickles = remaining_knuts // 29
    remaining_knuts = remaining_knuts - (sickles * 29)

    output = ''

    if galleons > 0:
        output += f'{galleons} galleons'
    if sickles > 0:
        output += f'{sickles} sickles'
    if knuts > 0:
        output += f'{knuts} knuts'

#question 14
from random import randint

def guess_num(user_guess):
    output = ''
    value = randint(0,9)
    if value % 2 == 0 and user_guess == "even":
        return 'correct'
    if value % 2 == 0 and user_guess == "odd":
        return 'incorrect'
    if value % 2 != 0 and user_guess == "even":
        return 'correct'
    if value % 2 != 0 and user_guess == "odd":
        return 'incorrect'
    return output


#question 1

def is_fever(input):
    if input[-1] == 'F':
        if input[:-1] >= 98.6:
            return True
        else:
            return False
    if input[-1] == 'C':
        if input[:-1] >= 37:
            return True
        else: return False
