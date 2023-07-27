"""
    you can use comments for psudeo code
    I mean structring the program before you write actual code

"""

# Ask the user for their name
name = input("What's your name? ")

# Say hello to user
print("Hello, " + name)
print("Hello" , name) #it will add space automatically

print("hello", end=" ")# ends with a space not new line
print(name)

print("hello" , name , sep="!!!!")# use !!!! instead of a space for seperator

# printing quotes
print("Hello , \"friend\"")
print('Hello , "friend"')

# foramt strings
print(f"hello {name}")