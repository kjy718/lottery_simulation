from random import randint

def generate_numbers(length):
    '''(int) -> list
    
    Generate a list of unique random numbers between 1 and 45.
    
    >>> len(generate_numbers(6))
    6
    >>> all(1 <= num <= 45 for num in generate_numbers(6))
    True
    '''
    numbers = []

    while len(numbers) < length:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers
    
def draw_winning_numbers():
    '''(None) -> list
    
    Generate a sorted list of 6 unique winning numbers and 1 bonus number.
    
    >>> result = draw_winning_numbers()
    >>> len(result)
    7
    >>> all(1 <= num <= 45 for num in result)
    True
    >>> result[:6] == sorted(result[:6])
    True
    >>> result[6] not in result[:6]
    True
    '''
    winning_numbers = generate_numbers(6)  
    bonus_number = randint(1, 45)  

    while bonus_number in winning_numbers:  
        bonus_number = randint(1, 45)
    
    return sorted(winning_numbers) + [bonus_number]

def count_matching_numbers(numbers, winning_numbers):
    '''(list, list) -> int
    
    Count the number of matching elements between two lists.
    
    >>> count_matching_numbers([1, 2, 3, 4, 5, 6], [1, 2, 3, 7, 8, 9, 10])
    3
    >>> count_matching_numbers([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13])
    0
    '''
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count += 1 
    
    return count
    
def check_prize_money(numbers, winning_numbers):
    '''(list, list) -> int
    
    Calculate the prize money based on the number of matching numbers and bonus number.
    
    
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = winning_numbers[6] in numbers

    >>> check_prize_money([1, 2, 3, 4, 7, 8], [1, 2, 3, 4, 5, 6, 7])
    50000
    '''
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


