class Food: 

    def __init__(self, name) -> None:

        self.name = name

        print(f"{self.name} Is Created From Base Class")

    def eat(self):
        
        print("Eat Method From Base Class")

class Apple(Food): 

    def __init__(self) -> None:
        print("Apple is Created from Derived Class")


food_one = Food("Pizza")
