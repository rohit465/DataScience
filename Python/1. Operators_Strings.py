'''
Operators  -  

1. Arithmetics Operaotrs

'''

x = 10
y= 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # Floor Devision
print(x%y) #    Modulud (Remainder)
print(x**y) #Exponential

# 
# print(10 + '20') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10 + 34.55)



'''

 Comparison Operators - always return boolean

'''

a = 5
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



'''

Logical Operators - AND/OR/NOT - returns boolean

'''

k = 11
l = 12
m = 23

print(k<l and l < m)
print(k<l and l>m)
print(not(k<l))



'''

BitWise Operators - AND/OR/XOR/LeftShift(<<) / Right Shift(>>)

'''
o = 10
p = 6

print("*****  BitWise Operators *****")
print( o & p)
print(o | p)
print(o ^ p)
print(~ o)
print(o << 1)
print(o >> 1)



'''

Assignment Operators

'''
print("*****  BitWise Operators *****")

q = 20
r = 3

q+=r
print(q)

q-=r
print(q)

q*=r

print(q)

q /= r
print(q)

q %= r
print(q)


'''
Membership Operator

in , not in

'''

print('***** MemberShip operator*******')

print('a' in 'Rohit')
print('a' not in 'Rohit')


'''
Identity Operators

'''

print("****** Identoty operators *******")

s = 10
t = 10

print(s is t)
print(s is not t)

print(id(s)) # to find address of variables
print(id(t))







'''

Strings 

- Data Structure
- List functionality
- Sequence of Characters
- Immutable


'''

name = 'rohit'
print(type(name))

string = 'Rohit Nimangre'
print(string[1])
print(string[-1])

print(string[0:5])
print(string[3:9:2])
print(string[3:15:2])

print(string[-8:-1])
print(string[-5:])
print(string[::-1]) # Reversal of String



# String in-built functions

print(string.upper())
print(string.lower())
title_string = 'Lower the person higher it will rise'
print(title_string.title())
print(title_string.capitalize())
print(string +' ' + title_string)
print(string * 5)

#print('2' + 3) # type error

string1 = "apple"
string2 = "banana"

print(string1 == string2)
print(string1 != string2)
print(string1 < string2)
print(string1 > string2)
print(string1 <= string2)
print(string1 >= string2)

'''  
In String Comparison happens with the unicode 
a = 97, b = 98  then, a < b

'''

print(ord('a')) #97
print(ord('b')) # 98

print(a < b)

print("cat" > "catalog") # till cat it's equal but later 'a' in catalog is is greater

print("Zebra" < "apple") # Z = 90

# replace()

og_string = "Hello,World!" 
new_string = og_string.replace("World", "Rohit")  
print(new_string)


#split()
print(og_string.split())


#strip() - removes whitespace in beginneing or end

line = '       Ich trinke gern Wasser, Milch, Orangenzaft    '
stripped_line = line.strip();
print(line, stripped_line)
print(id(line))
print(id(stripped_line))


# index() -  return the initial index of letter/world or valueError if not present 
print(stripped_line.index('Milch'))


# find() - returns the initial index of letter/word or returns -1
print(stripped_line.find('Rohit'))

#count() - returns the no. of terms present in string
print(stripped_line.count('a')) # 3
print(stripped_line.count('Rohit')) # 0

'''
isalpha() - "stripped line" contains a space character (' '), which is not an alphabetic character.
The .isalpha() method returns True only if all characters in the string are alphabetic (i.e., only letters, no spaces, numbers, or symbols).

'''
print("stripped line".isalpha())

# isnum
#isdigit
#isupper
#islower


# Formatting String
age = 24
text = f'Mein Name ist Rohit und Ich bin {age} (vierundzwanzig) years old.'
print(text)




