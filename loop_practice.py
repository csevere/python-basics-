# import random #cannot put inside a while loop; must remain outside
# i = "Y" #you can assign strings
# while i == "Y":
#     random_number = random.randint (1,10) #generate a random number between 1 and 10; can be within a while loop
#     print random_number #can be within a while loop
#     i = raw_input("Play again? Y OR N?")
#
#
# #question9
# i = 1 #consider the boundaries of the question always
# while i <= 10: # if i == 10; program can't find ten and continues forever
#     print i, #comma makes it print in one line; no new line
#     i += 1 #increasing by 2 skip by 2s etc
#
#     #consider the starting point and the increment amount b/c reach condition sooner or not at all;
#
#     i = 10 #consider the boundaries of the question always
#     while i >= 10: # if i == 10; program can't find ten and continues
#         print i, #comma makes it print in one line; no new line
#         i += 2
        #consider the starting point and the increment amount b/c reach condition sooner or not at all;

#
# # 1
# for i in range (1, 11):
#     print i
#
# #2
# pick_number1 = int(raw_input("Start from: "))
# pick_number2 = int(raw_input("End on: "))
# for i in range (pick_number1, pick_number2 + 1):
#     print i
#

#3

# i = 0
# for i in range(1, 11, 2):
#     print i

#4

# size = 5
# for i in range(size):
#     print ("*" * size)

#5
# pick_width = int(raw_input("Width? ")
# pick_height = int(raw_input("Height? ")
# for i in range(pick_height):
#     print ("*" if i in [0, pick_height-1])
# for j in range(pick_width):
#     print ("*" if j in [0, pick_width-1])
# print()
#
height = int(raw_input("Height? ")) #look over
width = int(raw_input("Width? "))
for i in range(height):
    if i == 0:  #if i == 0
        print("* " *(width))
    elif i in[(height-1)]:
        print("* " * (width))
    else:
        print("*" + "  " * (width) + " *")
#
# input()

#exercise 6

# for i in range (1, 11):
# #     print i
#  i = 0


# for i in range(1, 9, 2):
#     print (i * "*")

#
# def pyramid(rows = 4):
#     for i in range(rows):
#         print ' ' *(rows-i-1) + '*' *(2*i+1)




height = 4
for i in range (1, height+1):
    # print (2*height-i)* " " #dont forget to indent
    #print on the same line
    print ((2*height-i)* ' ') + (1+2*(i-1))* "*" #you need to print the space padding first




#print a triangle 2

    # else ' ', end =''
    # print()


#
# m, n = 10, 10
# for i in range(m):
#     for j in range(n):
#         print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end='')
#     print()

#print a triangle 2

#multiplication table
#
# user_number = int(raw_input("Pick a number? "))
# for i in range (1,11):
#     print(user_number,  "x", i, "=", user_number *i)

 size = 19
# for x in range(size+1):
#     if(x%size==0):
#        print('*'*size)
#     else:
#         print('*'+' '*(size-2)+'*')
#         #print(' '*3)
#         #print('*')
