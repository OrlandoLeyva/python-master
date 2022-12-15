# lists methods

countries = ['mexico', 'italia','australia', 'canada']

# add new elements
countries.append('usa')

# works to add a new item but you got to indicate the index.
countries.insert(1, 'peru')

# empty the list
countries.clear()

countries = ['mexico', 'italia','australia', 'canada']

# order a list
countries.sort()

# remove items
countries.remove('mexico') # indicate the value you want to remove 
countries.pop(1) # remove an item by its index.
countries.clear() # remove all the items

countries = ['mexico', 'italia','australia', 'canada', 'italia']

# reverse a lists
countries.reverse()
countries.reverse()

# determinate if some value is in the list
isInTheList = 'mexico' in countries # returns False or True.

# count the number of items
numberOfItems = len(countries)

# determinate how many times one item appears in the list.
result = countries.count('italia')

# get the index of some item. NOTE: if you have duplicate items will return the index of the first one that was found
index = countries.index('italia')

#join two lists
countries.extend(['brazil', 'norway'])
print(countries)