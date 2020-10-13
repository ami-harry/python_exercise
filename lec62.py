# multilevel inheritance

class Dad():
    basket_ball = 5


class Son(Dad):
    dance = 1

    def is_dance(self):
        return f"yes i dance {self.dance} times"


class GrandSon(Son):
    dance = 5

    def is_dance(self):
        return f"oh yeah, yes i dance {self.dance} times  very beautifully"


darry = Dad()
larry = Son()
harry = GrandSon()

a = harry.is_dance()
print(a)
# print(harry.basket_ball)
# if the same method in parent class and in son class, then the priopity will be given to son class,
