class Planet(object):
    name = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    diameter = ["3031", "7520", "7917", "4212", "86881", "72367", "31518", "30599"]
    moons = ["0", "0", "1", "2", "79", "53", "27", "14"]
    distance = ["35.98", "67.24", "92.96", "141.6", "483.8", "890.8", "1784", "2793"]
    
    def __init__(self, name, diameter, moons, distance):
        self.nameindex = name
        self.diameterindex = diameter
        self.moonindex = moons
        self.distanceindex = distance
        
    def __str__(self):
        name = Planet.name[self.nameindex]
        diameter = Planet.diameter[self.diameterindex]
        moons = Planet.moons[self.moonindex]
        distance = Planet.distance[self.distanceindex]
        return [name, diameter, moons, distance]
