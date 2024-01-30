# 1. define a class Cat
# 2. define a constructor for each Cat object
    # 2.5. define Cat attributes as name, color, age
# 3. define properties for all Cat attributes
    # 3.5. how would you define these with the property function?
    # 3.5. how would you define these with decorators?
# 4. define methods for each Cat object
    # 4.5. define Cat methods as meow(), have_a_birthday()
# [OPTIONAL] 5. define overriding str magic method

class Cat:
    def __init__(self, name, color, age = 1): #magic method if has 2 underscores on both sides of the method name; can set defaults as well like JS
        self.name = name
        self.color = color
        self.age = age

    #setting properties
    #using the property function
    def get_name(self): #getter
        return self._name
    
    def set_name(self, new_name): #setter
        self._name = new_name

    name = property(get_name, set_name)

    #setting with decorator, this is a process called overloading
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

    #instance methods
    def meow(self):
        print('Meow!')

    def have_a_birthday(self):
        self._age += 1 #same as writing self.age = self.age + 1
        print('Happy Birthday!')
    
    #str magic method to print the objects themselves. its called overriding the default method of printing out the object and makes the return human readable
    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nAge: {self.age}"
    pass

#each of the below is an instance of the class Cat
cinammon = Cat("Cinammon", "Orange", 3)
peanut = Cat("Peanut", "Brown", 5)
prenup = Cat("Prenup", "black", 4)

prenup.age = -2
cinammon.name = "C" #to reset the name of a property; most languages you can not do this and would normally need to underscore to do it

#printing out the instances
print(cinammon.age)
print(peanut.age)
print(prenup.age)
peanut.meow() #to call the instance method (if has a print in the method dont need to do a print again)
peanut.have_a_birthday()
print(peanut.age)
print(prenup)