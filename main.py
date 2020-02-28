from planetarium import Planetarium
from planet import Planet

planetarium1 = Planetarium()
print(str(planetarium1))

p = {1:"mecury", 2:"venus", 3:"earth", 4:"mars", 5:"jupiter", 6:"saturn", 7:"uranus", 8:"neptune"}


planetInput = input(f'''
    Choose a Planet:
    1: Mecury
    2: Venus
    3: Earth
    4: Mars
    5: Jupiter
    6: Saturn
    7: Uranus
    8: Neptune
    Choice: ''')
planetChoice = planetInput
str(planetChoice)

dataInput = input(f'''
    Choose Data Type:
    1: Name
    2: Diameter
    3: Distance
    4: Moons
    Choice: ''')
dataChoice = dataInput
int(dataChoice)





