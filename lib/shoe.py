#!/usr/bin/env python3

class Shoe:
    
    def __init__(self,brand,size) -> None:
        self.brand = brand
        self.size = size
        self._condition = "New" #initialize condition attribute = initial state of the shoe

    
    def brand(self):
        """The brand property"""
        return self._brand

    @property
    def size(self):
        """The size property"""
        return self._size
    
    @size.setter
    def size(self,size):
        """size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    
    def cobble(self):
        """Method that says the shoe has been repaired""" #called when the shoe needs to be repaired
        print("Your shoe is as good as new!") #indicates the shoe has been repaired
        self._condition = "New" #update condition after repair to new

    @property
    def condition(self):
        """The shoe condition property"""
        return self._condition  #underscore indicates method is private and can't be modified or accessed outside the class, it should be accessed using the condition property
               

shoe = Shoe("Adidas", 9)
print(shoe.brand)
print(shoe.size)
shoe.cobble()




        