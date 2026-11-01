import random
import string
import allure

@allure.step("Генерация случайного строкового значения")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step("Генерация случайного числового значения")
def generate_random_number(start, finish):
    random_number = random.randint(start, finish)
    return random_number
