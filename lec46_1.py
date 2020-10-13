import lec46

# suppose if we want to access some particular function from the imported file, or didn't want what operations were performed in that original file, we want the fresh function here, then we will use if __name__="__main__"

# print(lec46.a)  # this will  give all the previous outputs of the function
b = lec46.wrong_sum(2, 5)
print(b)



