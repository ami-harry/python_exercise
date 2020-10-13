# if__name__="main"


def ret_str(string):
    print(f"ye string mujhe dede thakur {string}")


def wrong_sum(a, b):
    return a+b+2


# if __name__="main"
# this is used when we want some function to work anywhere, in any file without any interrution.


# this will give the name of imported file as output
print("And the name is ", __name__)
# here these functions will not execute in another file when we import this file


if __name__ == "__main__":
    ret_str("mera string ")
    a = wrong_sum(54, 23)
    print(a)
