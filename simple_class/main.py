"""
idea:
1) create class Animal and Cat
2) create init, gt, str methods in Animal
3) create init and str methods in Cat

Complexity: N/A
"""
from absl import app

class Animal:
    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight

    def __gt__(self, animal2):
        if self.weight > animal2.weight:
            return True
        else:
            return False

    def __str__(self):
        return('name: {}, weight: {}'.format(self.name, self.weight))

class Cat(Animal):
    def __init__(self, name='', weight=0, color=''):
        super().__init__(name, weight)
        self.color = color

    def __str__(self):
        return(super().__str__() + ', color: ' + self.color)

def main(argv):
    dog = Animal('dog', 23)
    yellow_cat = Cat('cat', 15, 'yellow')
    print(dog > yellow_cat)
    print(dog)
    print(yellow_cat)


if __name__ == '__main__':
    app.run(main)

