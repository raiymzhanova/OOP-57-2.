class Animal:
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age
    def speak (self):
        print(f"""
                  Step into my domain, distant traveler.
                  I am {self.name}
                  {self.species} master of the Northern winds, and king of the Southern lands. 
                  I have walked this mortal realm for {self.age} years, and still, my power grows.""")

Dragon = Animal("Balerion","Dragon",3597)
Lion = Animal("Aslan","Lion",2864)

Dragon.speak()
print()
print()
print()
print()
Lion.speak()