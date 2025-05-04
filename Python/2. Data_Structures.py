'''

List - Ordered Collections of Items, Mutable
     - Heterogeneous data elements

Tuple - Ordered Collection of Items, Immutable

Set - Unordered Collection of Items, unique Item, Mutable

Dictionaries - Unordered Collections of key-value pair, Mutable


'''

list1 = [1,2,3]  # list with same data type
list1 = ['rohit', 23, True] #List with multiple data type

list2 = [1, [2,3,4], [5,6,7,8]] # nested list
print(list2[1]) #[2,3,4]
print(list2[1][1])

letters = ['a', 'b', 'c', 'd', 'e','f', 'g']
print(letters[-1:-4]) # you can't move forward from index -1 to index -4. if you want to then give the step to -1 then it will go in reverse 
print(letters[-1:-4:-1])
print(letters[-4: -1])

num_list = [1,2,3,4,5,6,7,8, True, False]
print(max(num_list))
print(min(num_list)) #False
print(sum(num_list)) #37

str_list = ['abc', 'abd', 'abe']
print(max(str_list))
print(min(str_list))
# print(sum(str_list))  Error unsupported operand type(s) for +: 'int' and 'str'


# Inbuilt Functions of List
#      1. append()
#      2. extent()
#      3. insert()
#      4. remove()
#      5. pop()
#      6. del()
#      7. clear()
#      8. sort()
#      9. count()
#      10. index()
#      11. reverse()
#      12. join()




num_list.append(69)
print(num_list)

list4 = [1,2,13,4]
list5 = [5,6,7,8,9]

list4.append(list5) #[1, 2, 13, 4, [5, 6, 7, 8, 9]]
list4.extend(list5) # [1, 2, 13, 4,[5, 6, 7, 8, 9], 5, 6, 7, 8, 9]

print(list4)

num_list.insert(0, 6)
print(num_list)
num_list.insert(0, list4)
print(num_list)

n_list = list4 + list5
print(n_list)


# extend can extend list with tuple but concatenate doesn't it need same data type

a = [1,2]
a.append((3,4)) # [1, 2, (3, 4)]
a.extend((3,4)) # [1, 2, 3, 4]   converts tuple into list
#  a + (3, 4) gives error as same data type requirs while concatenting
print(a)

popped_elemnt = num_list.pop(0)
print(popped_elemnt)

del num_list[0]
print(num_list)

# num_list.clear()
print(num_list)

num_list.sort()
print(num_list)

num_list.sort(reverse= True)
print(num_list)

alpha_list = ['as', 'df', 'kj']
result = "- ".join(alpha_list)
print(result)



'''

Tuples

BuitIn Functions
     1. min()
     2. max()
     3. count()
     4. index()

'''

my_tuple = (1, 2, 3)
print(my_tuple[2])

tuplee = (1, 2, 3, 56, True, False, [11, 12, 13])
print(tuplee[-1][1])
print(tuplee[1:7])
print(tuplee[:-1])
print(min(my_tuple))
print(max(my_tuple))


#  Convert Tuple into List

tuplee2 = ('Rohit', 'Rohan', 'Pranav', 'Kunal')
list1 = list(tuplee2)
print(list1)

list1.extend(['Hardik', 'Shyam'])
n_tuple = tuple(list1)
print(n_tuple)

my_tuple = (1, 2, 3, 4, 5, 6, 7)
a, *b, c = my_tuple
print(a, b, c) # 1 [2, 3, 4, 5, 6] 7   b will take as list as by default

combined = my_tuple + tuplee2
print(combined)

'''
     List      |      Tuple
----------------------------------
     Mutable   |     Immutable
     []        |         ()
     Slower    |     Faster - better performance



'''








'''
Sets
     - unordered
     - mutable
     - unindexed
     - dupicates not allowed 
'''


set1 = {1, 2, 3, 5, 34,1, 2, 3, 11}
print(set1)

my_set = 'Hello'
print(set(my_set))

my_sett = {[1,2,3,4]}
print(my_sett) #TypeError: unhashable type: 'list'


