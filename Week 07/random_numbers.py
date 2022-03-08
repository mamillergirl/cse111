import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words = []
    print(words)
    append_random_words(words, 4)
    print(words)
    append_random_words(words)
    print(words)

    
    
    



def append_random_numbers(numbers, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        random_number = round(random_number, 1)
        numbers.append(random_number)

def append_random_words(words, quantity=1):
    word_choice = ["arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"]
    
    for _ in range(quantity):
        random_word = random.choice(word_choice)
        words.append(random_word)

    

main()