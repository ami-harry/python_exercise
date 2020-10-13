# multi inheritance
class Student():
    no_of_students = 10

    # constructor
    def __init__(self, s_name, s_roll, s_marks):
        self.name = s_name
        self.roll = s_roll
        self.marks = s_marks

    # method to show the details
    def show_details(self):
        print(
            f"Student name is {self.name}, roll is {self.roll} and marks is {self.marks}")

    # class method to change the no of students
    @classmethod
    def total_students(cls, new_students):
        cls.no_of_students = new_students

    # class method////alternative constructor
    @classmethod
    def constructor_class(cls, str):
        return cls(*str.split("-"))

    # normal class method
    @classmethod
    def good_str(cls, str):
        return f"{str} is returning"

    @staticmethod
    def stat_meth(str):
        return f"{str} is returning from static method"


class Player():
    no_of_game = 4  # class variable

    # constructor
    def __init__(self, name, game):
        self.name = name
        self.game = game

    # instance method
    def game(self):
        return f"Player name is {self.name} and game is {self.game}"


# concept of multiple inheritance
class CoolProgrammer(Student, Player):  # inheriting order is very important
    pass


s1 = Student("harry", 21, 54)
s2 = Student.constructor_class("mohak-34-65")

p1 = Player("shubham", "[cricket]")
cp = CoolProgrammer("Nitish", 38, 58)
# here it wll require the constructor details of first class, means student
# cp.show_details()

# if a class method is in all the classes, then while printing the variable using instance will depened upon order of inhertance
