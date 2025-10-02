# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# name="Taukir Sheikh"
# nameone='Taukir SHeikh'
# name2="Taukir's Sheikh"
# name3="Taukir"s Sheikh"
# name4='Tukir"s Sheikh'
# name5='Taukir'sheikh Sheikh'

# adress="""Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."
# """

# Slicing
# ==========
# string[start:stop:step]

#name="Taukir Sheikh 2001"
# namehalf=name[0:4]
# year=name[-4:]

# upper()  lower()  strip() replace()  split()
# print(name.upper())
# print(name.lower())
# print(name.strip())
# print(name.replace("u","v"))
# print(name.split())


# String Format

# name="Zubiya"
# age = 25
# gretting =f"Happy birthday {name} congo to turn {age+1}"
# print(gretting)

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# H.W join() capitalize() center() count() endswith() find() format() index() isalnum() isalpha() isnumeric() isupper() split() upper()
# ==============================================================

# join() :- combine a list (or tuple) of strings into one string
# separator string like " " or "-"

# words = ["hey", "zubiya", "urooj"]
#sentence = " ".join(words)
# print(sentence)

#capitalize() 
# makes the first character uppercase and makes the rest lowercase and Works on a string

#word = "hello, and welcome to my world"
#x = word.capitalize()
#print (x)

#center() if e need in center

#txt = "zubiii"
#x = txt.center(20)

#x = txt.center(20,"s")
#print(x)

#count (how many times a specific value or substring appears in a string, list, or tuple)

#txt = "I love apples, apple are my favorite fruit"
#x = txt.count("apple")
#peint(x)

#endswith() a string method that checks whether a string ends with a particular substring

#text = "hello world"
#print(text.endswith("world"))
#print(text.endswith("hello"))  
#print(text.endswith("lo", 0, 5)) (checks only 'hello')

#find()used to find the index (position) of the first occurrence of a substring inside a string

#text = "hello world"
#print(text.find("world"))       
#print(text.find("o"))
#print(text.find("x"))       # -1 (not found)

#format() :

#name = "Zubiya"
#age = 22
#text = "My name is {} and I am {} years old".format(name, age)
#print(text)

#index() :that returns the position (index number) of the first occurrence of a given value in a string, list, or tuple.
#text = "hello world"
#print(text.index("world"))

#isalnum() all characters in a string are letters (A–Z, a–z) or digits (0–9).if yes → returns True, otherwise False

#print("Hello123".isalnum())
#print("Hello 123".isalnum()) False (space is not alphanumeric)
#print("12345".isalnum())  True (only numbers)
#print("Hello!".isalnum())     False (exclamation mark is not alphanumeric)

#isalpha()all characters in a string are alphabetic letters (A–Z or a–z) true-false

#print("Hello".isalpha()) -True (only letters)
#print("Hello123".isalpha())-False (numbers included)
#print("Hello World".isalpha()) -False (space included)
#print("".isalpha())       -False(empty string)

#isnumeric() all characters in a string are numeric characters.
#print("12345".isnumeric())     # True (all digits)
#print("½".isnumeric())         # True (fraction character is numeric)
#print("²".isnumeric())         # True (superscript 2 is numeric)

#isupper() :all the alphabetic characters in a string are uppercase (A–Z)
#print("HELLO".isupper())     # True (all uppercase letters)
#print("HELLO123".isupper())  # True (letters uppercase, digits allowed)
#print("Hello".isupper())     # False (mixed case)

#split()list of parts based on a separator (default = space)

#text = "apple banana orange" 
#print(text.split())  

#upper() :all letters in a string to uppercase.

#text = "hello world"
#print(text.upper())  





