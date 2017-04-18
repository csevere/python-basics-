# print "Hello, World!"
# You can print two different things on the same line
print ("Hello, World" , "Again")

#This will work
#print """This
#will ignore the new lines
#unitl it sees another
#three quotes """

#Variables - string, number, letters, any other stuff that you can make with a
#keyboard and you want to stash something that's not fast, inot something that
#is fast.

#in JS ... var name = "Shane"
name = "Carla Severe"
name = "Carla" + "Severe"
first_name = "Carla";
last_name = "Severe";
full_name = first_name + " " + last_name
print full_name

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

first_name = "Carla"
last_name = "Severe"
print "Hello, {} {}".format(first_name, last_name) #placeholders  #could also

 #use %s



#print "Hello" + first_name _ " " + last_name

# .format - running a method, a bit of code someone else has wrriten that can be used for your benefit

#placeholders #%d are for digits
print "Hello, %s %s" % (first_name, last_name) #%s is for a strong
print "Hello, %s %s" % (first_name, last_name) #%s is for a strong

#floats
pi_the_magic_float = 3.14
print pi_the_magic_float
print type (pi_the_magic_float) #type tells you what it is

make_me_an_integer = int(pi_the_magic_float)
print make_me_an_integer

#Booleans - true or False
the_truth = True
print type (the_truth)
the_lie = False
print type (the_lie)

# true = true #can't work


#Raw Input
first_name = raw_input("First Name: ")
last_name = raw_input("Last Name: ")

#Conditonals
#1 = means you want to assign something
#2 = means you want to compare with whats on the left with whats on the right

if(first_name == last_name):
    print "Your first name is the same as your last name?"

age = raw_input("How old are you?")
age_as_int = int(age)
#print type (age)
if(age_as_int >= 21):
    print "You can buy beer."

#raw_input will always be a string
#if(age == 21):
    #print "You can buy beer"
