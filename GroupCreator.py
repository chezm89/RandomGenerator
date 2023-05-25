import random
#asks user to enter 15 Names

group_members_names = input("Enter a list of 15 Names.").split()
#prints original group order
print()
print(group_members_names)
print()
#randomly Shuffles the names
random.shuffle(group_members_names)

#creates 3 empty List to store names
group1 = []
group2 = []
group3 = []

#appneds and slice the random list of names into 3 groups
group1.append(group_members_names[0 : 5])
group2.append(group_members_names[5 : 10])
group3.append(group_members_names[10 : 15])


print("group1")
print(group1)
print()
print("group2")
print(group2)
print()
print("Group3")
print(group3)
print("Press enter to End")