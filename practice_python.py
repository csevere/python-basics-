# .split CUTS STRINGS

fullname = "Carla Severe"
split_name = fullname.split()
print (split_name)


#[] calls the 0 place in the string which is Carla
name = "Carla Severe"
def say_name():

      print ("Hello, " + split_name[0])

say_name()

############ FOR LOOP  ###############

#USING "break" in FOR LOOP
for letter in 'Python':     # First Example
   if letter == 'h':
      break
print 'Current Letter :', letter #prints string comma then prints letter

# SECOND EXAMPLE
var = 10
while var > 0:
   print 'Current variable value :', var
   # var = var -1 or
   var -= 1
   if var == 5:
      break

print "Good bye!"

# THIRD EXAMPLE WITH DICTIONARY
user_input = raw_input("Enter state: " )
for s in states: #for item in list of states
    if user_input == s: #if user_input equals that item
        print  "Hello, %s." % states[s] #don't put variable in quotes
        break #put break to stop it from continuing once it finds the item
else:
    print "Sorry, %s is not in list." % (user_input)


#USING RANGE
for i in range (1,10):
    if i > 0:
        print 'Current variable value:', i
    i -= 1
    if i == 4:
        break
print "Good bye!"


# #MEASURE NUMBER OF LETTERS IN STRINGS USING "FOR LOOP"
words = ['cat', 'window', 'defenestrate'] #use brackets for lists #this is a list
for letter in words: #you can use i or w or letter to count in for loop to count item in list
    print(letter, len(letter))

#TO MAKE A COPY AND MODIFY THE SEQUEENCE

words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w) #.insert adds the word and puts it at 0 position

print words



# USING elif STATEMENT
x = int(input("Please enter an integer: "))
# Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#THIS IS THE SAME AS ABOVE, BUT ABOVE IS BETTER
if x < 0:
    print('Negative changed to zero')
if x == 0:
    print('Zero')
if x == 1:
    print('Single')
else:
    print('More')


###############  DICTIONARY #####################
# create a "mapping" or "associating" of state to abbreviation

states = {
    'Oregon': 'OR', #'key': value
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': "Jacksonville"

}

#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#
# #print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
#
#
# #do it by using then cities dictionary
print '-' * 10 # printing ten dashes
print "Michigan has: ", cities[states['Michigan']] #so cities grabbing
#value in states grabbing value in the key Michigan
#print "Michigan has: ", cities['MI'] same as above
print "Florida has: ", cities[states['Florida']]
#
# #print every state abbreviation
print '-' * 10
for state, abbrev in states.items(): #for item 1 and item 2 in states
#which is turned into an item's list using .item() go through length
#all the pairs of items
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
    # cities([abbrev]) #getting values of each city, proxy abbrev

print '-' * 10
state = states.get('Florida') #the method .get() grabs the value of Michigan
# the method .get() needs a string in it
if  state:
    print "Hello, %s." % state
else:
    print "Sorry, Texas not in list."

#task: user enters a state, if state is in the list, grab the key
#if not in lists send message saying not in lists

user_input = raw_input("Enter state: " )
for s in states: #for item in list of states
    if user_input == s: #if user_input equals that item
        print  "Hello, %s." % states[s] #don't put variable in quotes
        break #put break to stop it from continuing once it finds the item
else:
    print "Sorry, %s is not in list." % (user_input)


print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities. get('TX', 'Does Not Exist')
print "this city for the state 'TX' is: %s" % city
