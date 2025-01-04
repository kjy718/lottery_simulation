from random import randint

def generate_numbers(length):
    '''(int) -> list'''
    numbers = []

    while len(numbers) < length:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers
    
def draw_winning_numbers():
    '''(None) -> list'''
    winning_numbers = generate_numbers(6)  
    bonus_number = randint(1, 45)  

    while bonus_number in winning_numbers:  
        bonus_number = randint(1, 45)
    
    return sorted(winning_numbers) + [bonus_number]

def count_matching_numbers(numbers, winning_numbers):
    '''(list, list) -> int'''
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count += 1 
    
    return count
    
def check_prize_money(numbers, winning_numbers):
    '''(list, list) -> int'''
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = winning_numbers[6] in numbers

    match count:
        case 6:
            return 1000000000
        case 5 if bonus:
            return 50000000
        case 5:
            return 1000000
        case 4:
            return 50000
        case 3:
            return 5000
        case _:
            return 0


