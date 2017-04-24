# print "Hello, World!"
# You can print two different things on the same line
# print ("Hello, World" , "Again")

#This will work
#print """This
#will ignore the new lines
#unitl it sees another
#three quotes """

#Variables - string, number, letters, any other stuff that you can make with a
#keyboard and you want to stash something that's not fast, inot something that
#is fast.

#in JS ... var name = "Shane"
# name = "Carla Severe"
# name = "Carla" + "Severe"
# first_name = "Carla";
# last_name = "Severe";
# full_name = first_name + " " + last_name
# print full_name

#python is not heavily typed

#Arithmitic
#the_meaning_of_life = 40 + 2
#print the_meaning_of_life
#print the_meaning_of_life / 2
#print the_meaning_of_life % 5
#print int(30.5 / 5.2) #int turns into integer

#print 4 + "Joe"
#print 4 * "Joe"

#Data types (variable types)
#-Strings - written type for humans
#-Numbers - something with digits and stuff goes with digits (. -)
#-- floats (number with a decimal pt) , integers
#--- Booleans - True or False, 1 or 0, yes or no, on or off
# lists - lists of variables in on variable
# dictionary - variable of variables
# objects - dwl

#Strings

# first_name = "Carla"
# last_name = "Severe"
# print "Hello, {} {}".format(first_name, last_name) #placeholders  #could also

 #use %s



#print "Hello" + first_name _ " " + last_name

# .format - running a method, a bit of code someone else has wrriten that can be used for your benefit

# #placeholders #%d are for digits
# print "Hello, %s %s" % (first_name, last_name) #%s is for a strong
# print "Hello, %s %s" % (first_name, last_name) #%s is for a strong
#
# #floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type (pi_the_magic_float) #type tells you what it is
#
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer
#
# #Booleans - true or False
# the_truth = True
# print type (the_truth)
# the_lie = False
# print type (the_lie)

# true = true #can't work


# #Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

#Conditonals
#1 = means you want to assign something
#2 = means you want to compare with whats on the left with whats on the right

# if(first_name == last_name):
#     print "Your first name is the same as your last name?"
#
# age = raw_input("How old are you?")
# age_as_int = int(age)
# #print type (age)
# if(age_as_int >= 21):
#     print "You can buy beer."
# else:
#     print "You are underage."

#raw_input will always be a string
#if(age == 21):
    #print "You can buy beer"

# import random
# random_number = random.randint (1,10) #generate a random number between 1 and 10
# print random_number
#
# #loop
# not_guessed = True
# while not_guessed:
#     guess_a_number = raw_input("Guess a number between 1 and 10.")
#     if (int(guess_a_number) == random_number):
#         print "You guessed the number!";
#
#         not_guessed = False; #if you guess wrong it loops until you guess right

#Day 3 lists

# student1 = "Marissa"
# student2 = "Merilee"
# student3 = "Daniel"
# student4 = "Chris"
#
# print(student1, student2, student4, student4)

#list is a single variable with a munch of numbered parts; the number that an element is in, in called the "index"
#tuples are()
#
# students = [
#     "Marissa",
#     "Merilee",
#     "Daniel",
#     "Chris",
#     "Shane",
#     "Stephen",
#     "Drew",
#     "Blake"
# ] #can put lists, booleans, numbers within lists
#must print elements
# print(students[1])
# print(students[5])

#first element is always 0
#second element is alwasy

# atlantaTeams = [
#     "Falcons",
#     "Braves",
#     "Hawks",
#     "Thrashers"
# ]
# #print (atlantaTeams[0])
# #to add an element to the End of a list, you can use the append method
# print (atlantaTeams)
# atlantaTeams.append("Atl United")
# print (atlantaTeams)
#
# #to delete an index, you can use remove method
# atlantaTeams.remove("Thrashers")
# print (atlantaTeams)

#to insert any index with the insert method
# atlantaTeams.insert (0, "Tom's Brady's Team")
# print (atlantaTeams)
#
#
# teams_as_a_string = "Falcons, Braves, Hawks, Thrashers" #comma separates them
# teams_as_a_list = teams_as_a_string.split (",")
# print (teams_as_a_list)

#***pop method*** will remove the las element
#students.pop

#sort will CHANGE the lists
# atlantaTeams.sort();
# print (atlantaTeams)
#
# copy_atlanta_teams = sorted(atlantaTeams);
# print (copy_atlanta_teams)
#
# length_of_atlanta_teams = len(copy_of_atlanta_teams) #counting the indecies
# print (length_of_atlanta_teams)
# print (copy_of_atlanta_teams [-1])
# print (copy_of_atlanta_teams [length_of_atlanta_teams -1])
# print len(copy_of_atlanta_teams[0])

#the other type of loop...for
# for i in range(1,10): #range will generate a number #runs for 1 - 10
#     print i

#for loop format: [for] [what you want to call the thing you are on] [in] [variable looping through]

# for student in students:
#     #print student
#     if(student == "Chris"):
#         print "Welcome, Chris!"
#     else:
#         print "You are not Chris!"

#Set up a for loop ... but the range, will be 0 to len-1 for i in range(1,10):
# students_length = len(students)
#
# #for i in range(0, len(students)-1) #longer way
#
# for i in range(0, students_length):
#     print(students[i])
# for i in range(0, 10, 2):
#     print(i)

# If you want a portion of a list, you can use the [x,y] format. This will create a copy of the ray, does not mutate or change the original. It will start at the x element, and will stop at the yth

# print(students)
# second_and_third = students[1:3]
# print second_and_third

# all_but_the_first = students[1:]
# print all_but_the_first

#a function is a piece of code that be called from the main body of the program; the upshot is that if you have complicated code or code that is reated often, a function is your answer. Repeating yourself is BAD.
#A function in python is not a function, it is a defintion.
#To declare a function in python, you use "def"
#Functions ALWAYS have ()

# example
# def say_hello(): #need a colon
#     print ("Hello") #not working
#
# say_hello()

# def say_hello_with_name(name):
#     print("Hello, " + name)
# #say_hello_with_a_name
# #say_hello_with_a_name ("Rob", "Chad") this will also fail
# say_hello_with_name("Nick")
# #print name

# def say_hello_with_default(name, in_clas = "Yes"): #notworking
#     print("Hello, " + name)
#     print "Is student in class?" + in_class
#
# say_hello_with_default ("Carla")
# say_hello_with_default ("Max", "No")
# #say_hello_with_name

#function always return something
# def return_user_name (name):
#     return name
#
# print return_user_name("Yingrong")
#
# def make_uppercase(string):
#     return string.upper()

# normailized_string = make_uppercase("I'm a wild and crazy person")
# print normailized_string

# normailized_string = [make_uppercase("I'm a wild and crazy person")]
# normailized_string.append(make_uppercase ("me too"))
# print normailized_string
#
# def sum_odd_number():
#     sum = 0
#     for i in range(1,5001, 2)
#     # for i in range (1, 5000):
#         # if (i %2 == 1):
#
#         sum +=1
#     return sum #becareful of indentation
# print sum_odd_number()

#doing in a loop
#break example
# i = 0
# while 1: #this will run forever...
#     i += 1
#     if (i == 10):
#         break
# print ("We broke out of the loop")
#
# import random
# 1. grab a random index from students
# 2. then remove that student from the list
# 3. repeat until len(list) = 0

#for i in range(0, len(students))
#while students:
#for studen in students

students:

]

def get_student():
    rand_num = random.randint(0,len(students)-1)
    current_student = students[rand_num]
    students.remove(current_student)
    return current_student


while students:
    student1 = get_student()
    student2 = get_Student()
    print (" %s is pared with %s") %s (student1, student2)
