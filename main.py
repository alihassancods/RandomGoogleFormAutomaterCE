from pyautogui import *
from random import choice,randint
from webbrowser import open
def pressTab():
    sleep(0.1)
    press('tab')
def pressDown():
    sleep(0.1)
    press('down')
def selector(options):
    sleep(0.1)
    for i in range(randint(1,options)):
        pressDown()
    press('space')
    pressTab()

first_names = [
    "Amelia", "Olivia", "Isla", "Emily", "Sophia", "Ava", "Lily", "Mia", "Isabella", "Grace",
    "Freya", "Charlotte", "Daisy", "Florence", "Poppy", "Ella", "Evie", "Scarlett", "Sophie", "Ruby",
    "Ivy", "Millie", "Evelyn", "Elsie", "Rosie", "Maisie", "Holly", "Alice", "Harper", "Emilia",
    "Matilda", "Chloe", "Lucy", "Eliza", "Eleanor", "Luna", "Hannah", "Bella", "Maddison", "Willow",
    "Georgia", "Lottie", "Zara", "Amelie", "Violet", "Esme", "Jasmine", "Maya", "Amber", "Erin"
]

last_names = [
    "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright",
    "Thompson", "Evans", "Walker", "White", "Roberts", "Green", "Hall", "Wood", "Harris", "Martin",
    "Jackson", "Clarke", "James", "Turner", "Hill", "Scott", "Moore", "Cooper", "Morris", "Ward",
    "King", "Watson", "Baker", "Hughes", "Edwards", "Lewis", "Morgan", "Bell", "Miller", "Phillips",
    "Allen", "Carter", "Parker", "Griffiths", "Harrison", "Stewart", "Howard", "Simpson", "Cook", "Ellis"
]

def giveName():
    first_name = choice(first_names)
    second_name = choice(last_names)
    while first_name == second_name:
        second_name = choice(names)
    return f"{first_name} {second_name}"
def main():
    URL = "Enter your url here"
    if input():
        open(URL)
        countdown(5)
        click(500,500)
        for i in range(99):
            pressTab()
            pressTab()
            pressTab()
            name = giveName()
            print(name)
            typewrite(name)
            pressTab()
            typewrite(str(randint(20,50)))
            pressTab()
            selector(3)
            selector(3)
            # 0
            selector(2) #1
            selector(4) #2
            selector(5) #3
            selector(5) #4
            selector(5) #5
            selector(4) #6
            selector(5) #7
            selector(4) #8
            selector(4) #9
            selector(2) #10
            selector(5) #11
            selector(5) #12
            selector(2) #13
            selector(5) #14
            selector(5) #15
            selector(5) #16
            selector(2) #17
            selector(5) #18
            selector(5) #19
            selector(2) #20
            selector(5) #21
            print("ended")
            print("now submitting")
            press('space')
            countdown(3)
            pressTab()
            pressTab()
            press('return')
            countdown(3)
            print(f"completed {i}")
if __name__ == '__main__':
    main()