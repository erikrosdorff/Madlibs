# The following are examples of how to input text:
# from contextlib import nullcontext
# shepherd = "Mary"
# age = 32
# stuff_in_string = "Shepherd {} is {} years old.".format(shepherd, age)
# print(stuff_in_string)

#Another example of text input
# Adj = input("Adjective: ")
# some_text = "Text"
# print(str("Here is some text -> ") + some_text)
# print("Here is some text -> {}".format(some_text))
# print(f"Here is some text -> {some_text}")

#Using different classes to insert into the code. Idealily "Fill in the gap"

adjective = input("Enter an Adjective: ")
adjective2 = input("Enter another Adjective: ")
type_of_bird = input("Enter a type of a bird: ")
room = input("Enter a room in the house ")
second_form = input("Enter the second form of a verb: ")
base_form = input("Enter the base form of a verb: ")
relative = input("Enter the name of a relative: ")
liquid = input("Enter a liquid: ")
verb_ing_form = input("Enter a verb in 'ing' form: ")
part_of_body = input("Enter a part of the body")
plural_noun = input("Enter a plural noun: ")
verb_ing_form2 = input ("Enter a verb in 'ing' form: ")
noun = input ("Enter a noun: ")


madlib = f"""It was a {adjective}, cold November day.  \
I woke up to the {adjective2} smell of {type_of_bird} roasting in the {room} downstairs. \
 I {second_form} down the stairs to see if I could help {base_form} the dinner. \
  My mom said, 'See if {relative} needs a fresh __noun__'  \
  So I carried a tray of glasses full of {liquid} inot the ___{verb_ing_form}___ room. \
  When I got there, I couldn't believe my ___{part_of_body}___! \
  There were {plural_noun} {verb_ing_form2} on the {noun}!"""

print(madlib)