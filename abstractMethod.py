from abc import ABCMeta, abstractmethod


class Dog(metaclass=ABCMeta):

    @abstractmethod
    def eat(self):
        return NotImplemented

    @staticmethod
    @abstractmethod
    def bark(self):
        return NotImplemented

    @classmethod
    @abstractmethod
    def belong_to_what(cls):
        return NotImplemented


class Husky(Dog):
    # need to override Class Dog methods
    def eat(self):
        print("Husky is eating.")

    @staticmethod
    def bark():
        print("Husky is barking!")

    @classmethod
    def belong_to_what(cls):
        print(f"Husky is belonging to {cls.__base__}.")


class Golden(Dog):
    def eat(self):
        print("Golden is eating.")

    @staticmethod
    def bark():
        print("Golden is barking!")

    @classmethod
    def belong_to_what(cls):
        print(f"Golden is belonging to {cls.__base__}.")


if __name__ == '__main__':
    Husky().eat()
    Husky().bark()
    Husky().belong_to_what()
    print("-"*20)
    Golden().eat()
    Golden().bark()
    Golden().belong_to_what()
