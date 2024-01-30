class Puppy:
    def __init__(self, name, color, age, isGoodBoy = True):
        self.name = name
        self.color = color
        self.age = age
        self.isGoodBoy = isGoodBoy

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and len(new_name) > 2:
            self._name = new_name
        else:
            raise ValueError("Name must be a string and longer than 2 characters") #can do exception
            #raise Exception("Name must be a string and longer than 2 characters!")
            #ValueError will be more in phase 4 so would mainly want to do raise Exception
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            print("That's not a valid age")
        else:
            self._age = new_age

    @property
    def isGoodBoy(self):
        return self._isGoodBoy
    
    @isGoodBoy.setter
    def isGoodBoy(self, new_isGoodBoy):
        #if new_isGoodBoy == True or new_isGoodBoy == False: #could have done this too
        if type(new_isGoodBoy) == bool:
            self._isGoodBoy = new_isGoodBoy
        else:
            raise Exception("isGoodBoy must be a Boolean value")
        
    def bark(self):
        print('WOOF!')

    def have_a_birthday(self):
        self._age += 1
        print('Happy Birthday!')

    def make_a_collar(self):
        print(f"You now have a new collar {self.name}")

    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nAge: {self.age}"
    pass

Rio = Puppy("Rio", "Black and White", 4)
Bailey = Puppy("Bailey", "Multicolor", 1, False)

print(Bailey.name)
print(Rio.age)
Rio.bark()
Bailey.bark()
Rio.have_a_birthday()
Bailey.have_a_birthday()
print(Rio)
print(Bailey)
print(Rio.isGoodBoy)
print(Bailey.isGoodBoy)
Rio.make_a_collar()
Bailey.make_a_collar()