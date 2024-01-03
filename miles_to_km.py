# Hello, today I will show you how to create your own program that converts miles to km, the easy way

# As you can see we have created a function called miles_to_km with the parameter "miles"
def miles_to_km(miles):
    km = miles * 1.609
    return km

# here we have now defined kilometers to be equal to miles * 1.609 (1 mile) and have returned the variable "km".


print("Enter the number of miles: ")
# now we print the number of kilometers in the miles, but wait, we need input right?
print(miles_to_km(int(input("> "))))

# we have used the print function to print the kilometers that have been converted from miles using the input function
# take note that the input function has been defined as an integer

# now lets run the code

# We don't have any code telling us what to input!

# nevertheless, the code still works... but let's fix the program to make it easier to understand

# after all, we don't want to confuse the program user, do we?

# ok, so we changed it, let's run the code again!

# as you can see, it now asks the user to enter the number of miles.

# let's use 100 again

# We get the expected result. but we are not done yet.

# how do we make this program more appealing to the user?

# we have just added an extra print function to print out the request to the user.

# by adding the extra step, this allows us to use the > symbol to indicate the user should add something here

# let's run the code

# so you can see, it now provides an indication of where the information or data should be typed

# we enter 100 miles for quality testing purposes. this is our use case

# The program works!

# Congrats, this is the end of the tutorial, I hope you had fun and learnt something along the way.

# Feel free to subscribe to my channel for more content like this!

