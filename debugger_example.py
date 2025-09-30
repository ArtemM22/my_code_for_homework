
'''
У нас є список (1, 2, 3, 4, 5, 6, 7, 8, 9)
потрібно написати функцію, яка буде проходити по цьому списку та 
виводити лише непартні числа
'''

def is_odd(number: int) -> bool:
    '''
    funcions that receives a number and return if it is odd
    '''
    # if number % 2 != 0:
    #     return True
    # else:
    #     return False
    return number % 2 != 0


# print only odd numbers
def print_odd_numbers(numbers_list: list[int]):
    ''' 
    A function that recives a list of numbers and prints only odd numbers
    '''
    # пройтися по усіх числах
    for number in numbers_list:
    # Перевірити чи конкретне число є парне чи ні
        if number % 2 != 0:
           print(number)
    # Якщо не парне, то винести у термінал

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_odd_numbers(number)

print(is_odd(4))