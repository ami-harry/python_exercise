# lec 62 quiz


# make 3 classes
# 1. electronic device
# 2. pocket gadget
# 3. phone


class Electronic_device():
    cheap_rate = "yes, these are very cheap"

    def rate(self):
        return f"electronic device are cheap, {self.cheap_rate}"


class Pocket_gadget(Electronic_device):
    easy_to_use = "yes, these are very easy to use"

    def use(self):
        return f"pocket gadgets are easy to use, {self.cheap_rate}"


class Phone(Pocket_gadget):
    pass


p1 = Phone()
print(p1.cheap_rate)  # accessing grand father level class variable
print(p1.easy_to_use)  # accessing father level class variable

a = p1.rate()  # accessing grand father level class method
b = p1.use()  # accessing father level class method
print(a)
print(b)
