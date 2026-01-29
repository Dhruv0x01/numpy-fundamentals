import numpy as np

# Random number is useful for simulations, modeling, applying random transformations and testing purposes 
# variable = np.random.default_rng()
# and now in printing, variable.integers(starting value, ending value+1) as 2nd number you send is not included
# You can use keyword value too, to make it more readable, 
# rng.integers(1, 7) works too

# For Integers

rng = np.random.default_rng()

#print(rng.integers(1, 7)) #Prints random number between 1 and 6, not including 7
#print(rng.integers(low=1, high=101)) #Prints random number between 1 and 100, not including 101

#If you need multiple random numbers, add size thing too, they will come in 1d matrix
#print(rng.integers(low=1, high=101, size=3))

#If you want them in some specific dimensions
#print(rng.integers(low=1, high=101, size=(4,3)))  #size = (layers,rows,columns) or (rows, columns) or just one number


# We can set seed so we can reproduce some result, rng = np.random.default_rng(seed = 1)
# Basically as long as you have seed = 1, the result will keep repeating
# The result get saved with that specific seed number, so even if you came back to that seed later, 
# we will still have the result we did first with that seed


# -------------------------------------

# For Floating Point Number
# We will use different method, np.random.uniform() function
# uniform means uniform distribution, each value has equal chance of being selected

# To set the seed
#np.random.seed(seed = 10)

#print(np.random.uniform()) #Prints random floating point number between 0 to 1
#print(np.random.uniform(low=-1, high=1, size=3)) #Prints between ranges and give three random floating number here in 1d array
#print(np.random.uniform(low=-2, high=2, size=(2,4))) #Gave in 2d array 2x4

# -------------------------------------

# How to suffle an array
# Use rng.shuffle() function

rng1 = np.random.default_rng()

array = np.array([1, 2, 3, 4, 5])
rng1.shuffle(array)
print(array)

# --------------------------------------------------

# To choose random element of the array
# Use rng.choice() function
fruits = np.array(["apple", "banana", "orange", "watermelon", "coconut"])
fruit = rng1.choice(fruits)
multiple_fruits = rng1.choice(fruits, size = (3, 3))
print(fruits)
print(fruit)
print(multiple_fruits)

emojis = np.array(["🤭", "😍", "😖", "😭", "😈"])
emoji = rng1.choice(emojis, size=(3,3))
print(emoji)


