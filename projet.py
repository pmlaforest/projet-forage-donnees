import pickle
pickle_in = open("informationFile5.pickle","rb")
test = pickle.load(pickle_in)
print(test)