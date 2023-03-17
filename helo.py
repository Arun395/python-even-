marks=[89,67,89,78,45]
friends=['bhaskar', 'nandhu', 'arun', 'srinu', 'raja']
print(marks)
print(friends*2)
print(friends[1:2])
print(marks+friends)
friends.append('robbin')
print(friends)
friends.extend(['prem','ramu'])
print(friends)
 
friends.insert(1,'hareesh')
print(friends)

friends[1:1]=['a','b','c']
print(friends)

del friends[1]
print(friends)

friends.remove('b')
print(friends)
print(friends.pop(0))
