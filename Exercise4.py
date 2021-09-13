#Print a string that uses double quotation marks inside the string.
string1 = 'He said, "When will you be available?"'
print(string1)
#OR
string2 = "He said, \"When will you be available?\""
print(string2)

#Print a string that uses an apostrophe inside the string.
string3 = "I don't anything about the money"
print(string3)

#Print a string that spans multiple lines with whitespace preserved.
print("""Bola called Ade to asked about their discussion
        but unfortunately Ade couldn't remember any discussion
            and this make Bola to be angry""" )

#Print a string that is coded on multiple lines but gets printed on a single line.
print("Bola called Ade to asked about their discussion\
 but unfortunately Ade couldn't remember any discussion\
 and this make Bola to be angry")

#Create a string and print its length using len().
fruit = "pineapple"
print(len(fruit))

#Create two strings, concatenate them, and print the resulting string
word1 = "foot"
word2 = "ball"
word = word1 +word2
print(word)

#Create two strings, use concatenation to add a space between them, and print the result.
firstname = "Haonat"
lastname = "Araromi"
fullname = firstname + " " + lastname
print(fullname)

#Print the string "zing" by using slice notation to specify the correct range of characters in the string "bazinga".
string = "bazinga"
print(string[2:6])

#Write a program that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honey Badger". Print each lowercase string on a separate line.
print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honey Badger".lower())

#Repeat exercise 1, but convert each string to uppercase instead of lowercase.
print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honey Badger".upper())

#Write a program that removes whitespace from the following strings, then print out the strings with the whitespace removed:
string1 = " Filet Mignon"
print(string1.lstrip())
string2 = "Brisket "
print(string2.rstrip())
string3 = " Cheeseburger "
print(string3.strip())

#Write a program that prints out the result of .startswith("be") on each of the following strings:
string1 = "Becomes"
print(string1.startswith("be"))
string2 = "becomes"
print(string2.startswith("be"))
string3 = "BEAR"
print(string3.startswith("be"))
string4 = " bEautiful"
print(string4.startswith("be"))

#Using the same four strings from exercise 4, write a program that uses string methods to alter each string so that .startswith("be") returns True for all of them.
string1 = "Becomes"
string1 = string1.lower()
print(string1.startswith("be"))
string2 = "becomes"
print(string2.startswith("be"))
string3 = "BEAR"
string3 = string3.lower()
print(string3.startswith("be"))
string4 = " bEautiful"
string4 = string4.lower().lstrip()
print(string4.startswith("be"))

#Write a program that takes input from the user and displays that input back.
user_input1 = input("what is going on?")
print("She said: " + user_input1)

#Write a program that takes input from the user and displays the input in lowercase.
greeting = input("How should I greet?")
new_greeting = greeting.lower()
print("Well, if you want to know..." + new_greeting)

#Write a program that takes input from the user and displays the number of characters in the input.
user_input = input("What is going on?")
print(len(user_input))

#Write a program named first_letter.py that prompts the user for input with the string "Tell me your password:". The program should then determine the first letter of the user’s input, convert that letter to uppercase, and display it back
user_input = input("Tell me your password:")
firstletter = user_input[0]
print("The first letter you entered was: " + firstletter.upper())

#Create a string containing an integer, then convert that string into an actual integer object using int(). Test that your new object is a number by multiplying it by another number and displaying the result.
string_integer = "8"
newstring_integer = int(string_integer)
print(newstring_integer * 5)

#Repeat the previous exercise, but use a floating-point number and float().
string_float = "8.52"
newstring_float = float(string_float)
print(newstring_float * 3)

#Create a string object and an integer object, then display them side by side with a single print statement using str().
string = "The number is "
integer = 3
print(string + str(integer))

#Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, and displays the result. If the user enters 2 and 4, then your program should print the following text: The product of 2 and 4 is 8.0.
firstnum = input("Enter first number: ")
secondnum = input("Enter second number: ")
product = float(firstnum) * float(secondnum)
print("The product of " + firstnum + " and " + secondnum + " is " + str(product) + ".")

#Create a float object named weight with the value 0.2, and create a string object named animal with the value "newt". Then use these objects to print the following string using only string concatenation: 0.2 kg is the weight of the newt.
weight = 0.2
animal = "newt"
print(str(weight) + " kg is the weight of the " + animal)

#Display the same string by using .format() and empty {} placeholders.
weight = 0.2
animal = "newt"
print("{} kg is the weight of the {}" .format(weight, animal))

#Display the same string using an f-string.
weight = 0.2
animal = "newt"
print(f"{weight} kg is the weight of {animal}")

#In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1.
word = "AAA"
print(word.find("a"))

#Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha."
string = "Somebody said something to Samantha."
print(string.replace("s","x"))

#Write a program that accepts user input with input() and displays the result of trying to .find() a particular letter in that input.
myinput = input("Type something: ")
print(myinput.find("a"))

#Write a program called translate.py that asks the user for some input with the following prompt: Enter some text: Use .replace() to convert the text entered by the user into leetspeak by making the following changes to lowercase letters:
mytext = input("Enter some text: ")

mytext = mytext.replace("a", "4")
mytext = mytext.replace("b", "8")
mytext = mytext.replace("e", "3")
mytext = mytext.replace("l", "1")
mytext = mytext.replace("o", "0")
mytext = mytext.replace("s", "5")
mytext = mytext.replace("t", "7")

print(mytext)