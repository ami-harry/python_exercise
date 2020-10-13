# pickle module
import pickle


'''
# pickling a python object in a file
names = ["hariom", "mohak", "nitish", "ronik", "pandey", "mayank", "alok"]
file_name = "names.pkl"
file_ptr = open(file_name, "wb")
# it accepts the object and the file pointer in which the object is going to pickle
pickle.dump(names, file_ptr)
file_ptr.close()

'''

# reading the pickled file/ or undumping
file_name = "names.pkl"
file_ptr = open(file_name, "rb")  # opening the file as read binary mode
name_file = pickle.load(file_ptr)
print(name_file)
print(type(name_file))


# read more about pickle module
