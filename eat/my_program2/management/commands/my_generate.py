"""
Генерирует случайные имена, телефоны, адреса
"""

import random

def generate_name():
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"
    name = ""
    length = random.randint(3, 8)
    for i in range(length):
        if i % 2 == 0:  #
            name += random.choice(consonants).upper()
        else:
            name += random.choice(vowels)
    return name

def generate_phone_number():
    number = '+7'
    for _ in range(10):
        number += str(random.randint(0, 9))
    return number

def generate_adres():
    streets = ['Main Street', 'Park Avenue', 'Broadway', 'Elm Street', 'Maple Avenue']
    cities = ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami']
    states = ['NY', 'CA', 'IL', 'FL', 'TX']
    zip_codes = ['10001', '90210', '60611', '94102', '33101']
    street = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.choice(zip_codes)
    address = f"{street}, {city}, {state} {zip_code}"
    return address


if __name__ == "__main__":
    print(generate_name())
    print(generate_phone_number())
    print(generate_adres())