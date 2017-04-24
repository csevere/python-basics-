##practice 1##
#
###### 1. create a class ########
# class Song(object):
#
######2. create the main constructor function w/ def __init__ ########
#     def __init__(self, lyrics): #specify the variables you want to initialize using self, in this case lyrics
#         self.lyrics = lyrics
#
#####3. initalize objects here/ create more relevant functions; don't forget self;
#don't forget to indent ############
#     def sing_me_a_song(self):
#         for line in self.lyrics: #methods of the object
#             print line
#
#
# happy_bday = Song(["Happy birthday to you",
#                     "I don't want to get sued",
#                     "So I'll stop right there"]) #putting strings in the Song class
#
# bulls_on_parade = Song(["They rally around the family",
#                         "With pockets full of shells"])
#
# #It's applying the key in happy_bday
# #to the function sing_me_a_song by grabbing that function
#
# happy_bday.sing_me_a_song()
#
# #same thing here
# bulls_on_parade.sing_me_a_song()
#
# # Write some more songs using this and make sure you understand
# #that you're passing a list of strings as the lyrics.
#
# fireworks_song = Song(["Baby, you're like fireworks",
#                        "Come on and say OH OH OH!"])
#
# fireworks_song.sing_me_a_song() #call the method

###### GLOBAL VARIABLE COUNTER EXAMPLE: global variables are gross #########

# hello_count = 0
#
# def say_hello():
#     global hello_count
#     print 'hello'
#     hello_count += 1
#
# print 'Hello count %d' % hello_count
# say_hello()

###### DO IT WITH AN OBJECT #########

# class Hello(object): #create a class called Hello
#     def __init__(self): #constructor function use to set up initial state of object
#         self.count = 0 #count initialized to zero in dunder init method
#
#     def say_it(self):
#         print 'hello'
#         self.count += 1 #count incremented by 1 in say_it method
#
#
# myhello = Hello()
# print 'Hello count %d' % myhello.count
# myhello.say_it()
# myhello.say_it()
# print 'Hello count %d' % myhello.count


### MAKE A CLASS ###
#
# class Person(object):
#     def greet(self):
#         print "Hello"
#
#
# carla = Person() #create an instance of a person object
# carla.greet() #call the greet method present in the person object
#
# #THE CONSTRUCTOR AND INSTANCE VARIABLES##
# class Person(object):
#     def __init__(self, name): #add a parameter to dunder called name
#         # self.name = 'Janice'
#         self.name = name
#
#     def greet(self, other_person): #add a parameter to greet method
#         print 'Hello %s, I am %s' % (other_person.name, self.name)
#
# #now time to call the class and its methods/functions
# janice = Person('Janice') #pass a name in class Person
# carla = Person('Carla') #order matters, declare variables then call
# janice.greet(carla) #pass a person in the call
# carla.greet(janice)

######### OBJECTS AS RECORDS ###############
# class Contact(object):
#     def __init__(self,first_name,last_name, email, phone): #has four parameters
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#
# contact = Contact('Carla', 'Severe', 'carla.severe@gmail.com', '404-618-8049')
#
# print 'First name: %s' % contact.first_name
# print 'Last name: %s' % contact.last_name
# print 'Email: %s' % contact.email
# print 'Phone: %s' % contact.phone


############ PROBLEM SETS ################

#### 1
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet (self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
#
# sonny = Person('Sonny', 'sonny.hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# sonny.greet(jordan)
# jordan.greet(sonny)
#
# print "Sonny's email and phone are: %s and %s" % (sonny.email, sonny.phone)
# print "Jordan's email and phone are: %s and %s" % (jordan.email, jordan.phone)


#### 2 Make your own class

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self, year, make, model):
        print  "Car info: %s %s %s " % (car.year, car.make, car.model)

car = Vehicle('Honda', 'Civic', '2012')

print car.make
print car.model
print car.year
car.print_info('2012', 'Honda', 'Civic')

#when printing it variable.attribute
