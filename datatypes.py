#create a list
#a=[1,2,3]
#b=[4, "five",6.0]
#c=[5,6,7,[8,9,10]]
#d=[]
#access elements in a list
#print(a[0])
#print(b[2])
#print(c[3][0])
#negative indexing
#print(a[-2])
#print(b[-1])
#print(c[-1][-3])

#slicing a list
# print(a[1:2]) 
#print(a[:]) 
#print(b[1:])  
#print(c[3][1:3])  

#change items of a list
#a[0] = 'one'
#b[2] = 1
#print(a)
#print(b)

#add elements to the list
#a = [1, 2, 3]
#b = ["one", "two", "three"]
#a.append(4)  
#b.append("four")
#print(a)
#print(b)

#new = [11,22,33]
#a.extend(new) 
#print(a)
##print(c)
#a.insert(1,4)
#print(a)

#remove elements from a list
#mylist = [0,1,2,3,4,5,6,7,8,9,10]
#del mylist[0]
#print(mylist)
#mylist.remove(7)
#print(mylist)

#list copy
#a = [1,2,3]
#b = a
#print(a)
#print(b)
#print(a is b)

#a = [1,2,3]
#b = a.copy()
#print(a)
#print(b)
#print(a is b)

#loop through a list
#mylist = [1,2,3,4,5,6,7,8,9,10]
#for i in mylist:
    #print(i)

#print(len(mylist))

#print(1 in mylist) 
#print(11 in mylist) 

#TUPLES
#creating a tuple
#a = (1, 2, 3)
#b = (4, 'five', 6.0)
#c = ('seven', 8, 9.0,[10,11,12])
#d = ()
#e = 3, 4, 5
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
#creating a tuple with one item
##a = (1,)
#print(a)
#b = ('hello',)  
#print(b)
#accessing elements in a tuple
#print(a[0])
#print(b[1])
#print(c[3][1])
#negative indexing
#print(a[-1])
#print(b[-2])
#print(c[-1][-1])

#slicing a tuple
#print(a[0:2])
#print(a[:])
#print(b[1:])
#print(c[3][1:3])

#add elements to a tuple
#t1 = (1,2,3)
#t2 = (4,5,6)
#t3 = t1 + t2
#print(t3)
#tuple methods

#a = (1,2,3)
#result = a.count(1)
#print(result)
#result = a.index(2)
#print(result)

#tuple operations
#t5 = (1,2,3)
#print(2 in t5) #True
#print(2 not in t5) #False

#STRINGS
#escape sequences/characters
#a = 'hello\nworld'
#print(a)

#b = 'hello\tworld'
#print(b)

#c = 'hello\\world'
#print(c)

#format()
#a = 'hello'
#b = 'world'

#print('{} {}'.format(a,b))
#print('{1} {0} {1}'.format(a,b))

#SETS
#l = [1,2,3,3,4,5,5]
#s = set(l)
#print(s)
#iterate through a set
#s2 = {1,2,3,4,5,6}
#for i in s2:
    #print(i)
# check if an element is in a set
#s2 = {1,2,3,4,5,6}
#print(1 in s2) 
#print(7 in s2) 

#DICTIONARIES
#creating a dictionary
#a = {}
#b = {'one':1, 'two':2, 'three':[3,4,5]}

#l = [(1,'python'),(3,'c++'),(2,'java')]
#d = dict(l)
#print(d)

#accessing elements in a dictionary

#person = {'name':'John', 'age':30, 'country':'Norway'}
#print(person['name'])
#print(person['age'])
#print(person['country'])

#name = person.get('name')
#age = person.get('age')
#country = person.get('country')
#print(name)
#print(age)
#print(country)

#update, add items in a dictionary

#person['name'] = 'Jane'  #change
#person['age'] = 31
#person['country'] = 'USA'
#person['city'] = 'New York'  #add
#print(person)

#delete items in a dictionary
#result = person.pop('city')
#print(result)
#print(person)

##del person['age']
#print(person)

#person.clear()
#print(person)

#iterate through a dictionary

#numbers = {'one':1, 'two':2, 'three':3}
#for key in numbers:
  #  print(key)

#for key, value in numbers.items():
 #   print(key, value)

#for key in numbers.keys():
 #   print(key)

#for value in numbers.values():
#    print(value)

