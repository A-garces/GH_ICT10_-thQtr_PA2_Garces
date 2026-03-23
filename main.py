# Object-oriented programming
from pyscript import display, document

class Dog:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

        # create a method

def puppy_info(e):
    class Dog:
        def __init__(self, name, age, color, breed):
            self.name = name
            self.age = age
            self.color = color
            self.breed = breed


        def bark(self):
            display('Woof! '*3, target='output')

    name = document.getElementById('Input1').value
    age = int(document.getElementById('Input2').value)
    color = document.getElementById('Input3').value
    breed = document.getElementById('Input4').value

    dog1 = Dog('Luna', 1, 'black', 'German Shepherd')
    dog2 = Dog('Ollie', 7, 'white', 'Maltese Shih tzu')
    dog3 = Dog(name, age, color, breed)

    display(f'{dog1.name} is a {dog1.breed}, the color is {dog1.color}, and it is {dog1.age} year/s old.', target='output')
    display(f'{dog2.name} is a {dog2.breed}, the color is {dog2.color}, and it is {dog2.age} year/s old.', target='output')
    display(f'{dog3.name} is a {dog3.breed}, the color is {dog3.color}, and it is {dog3.age} year/s old.', target='output')

# get the value from a form
#repository link: GH_ICT10_PA2_4thQtr_Garces