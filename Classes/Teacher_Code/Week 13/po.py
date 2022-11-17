class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def speak(self):
        if self.species=='Cat':
            print('Meow')
        elif self.species=='Dog':
            print('Bark')
        else:
            print('Roar')
new_animal=animal("Z","Weasel")
print(new_animal)
new_animal.speak()