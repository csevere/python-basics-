#beginner notes throughout

# Practice 1: 1-10

#for i in range (1, 11):
#     print i

# Practice 2: n to m
# n = int(raw_input("Start from: "))
# m = int(raw_input("End on: "))
# for i in range (n, m + 1):
#    print i


#Practice 3: odd numbers
# i = 0
# for i in range(1, 11, 2):
#     print i

#Practice 4: Print a square
# size = 5
# for i in range(size):
#     print ("*" * size)

#Practice 5: Print a square II
# pick_width = int(raw_input("Width? ")
# pick_height = int(raw_input("Height? ")
# for i in range(pick_height):
#     print ("*" if i in [0, pick_height-1])
# for j in range(pick_width):
#     print ("*" if j in [0, pick_width-1])
# print()

#Practice 6: Print a square
# width = int(raw_input("Width? "))
# height = int(raw_input("Height? "))
# for i in range(1, height+1): #so for i (starts at 1) and ends within range limit of input height
#     if(i == 1): #if i = 1 print the top row of square
#         print ("*" * width)
#     elif(i > 1 and i< height):
#         print("*" + (width -2)* " " + "*")
#     else:
#         print ("*" * width)

#both sides of box already accounted for so just need w - 2 for spaces
#loops back goes to 2 which satifies condition and both conditions
#must be true


#Practice 7: Print a triangle
# height = 4
# for i in range (1, height+1):
#     spaces = ((2*height-i)* ' ')
#     stars = (1+2*(i-1))* "*"
#     print  spaces + stars


# print the number of spaces for each row first
# then add the number of asterisks on the same line
# dont forget to indent
#
# Practice 8: Print a triangle 2
user_height = int(raw_input("Give me a height: "))
for i in range (1, user_height+1):
    spaces = ((2*user_height-i)* ' ')
    stars = (1+2*(i-1))* "*" #use variables to make code easer to read
    print  (spaces + stars)

    # ((2*user_height-i)* ' ') + (1+2*(i-1))* "*"


#Practice 9: multiplication table
#
# user_number = int(raw_input("Pick a number? "))
# for i in range (1,11):
#     print(user_number,  "x", i, "=", user_number *i)

# input_text = "Good morning, DigitalCrafts"
# for i in input_text:
#     print (len(text) * "*" + "**")
#     print ("*" + input_text + "*")
#     print (len(input_text) * "*" + "**"
#     break
