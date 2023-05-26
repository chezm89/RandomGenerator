import random

# This function will ensure that there are 15 names entered
def get_group_members():
    while True:
        group_members = input("Enter a list of 15 names: ").split()
        if len(group_members) == 15:
            return group_members
        else:
            print("Invalid number of names entered. Please enter exactly 15 names.")

# This function will divide the names into 3 groups of 5
def divide_into_groups(group_members):
    random.shuffle(group_members)
    group1 = group_members[:5]
    group2 = group_members[5:10]
    group3 = group_members[10:15]
    return group1, group2, group3

# This function will print the groups
def print_groups(group1, group2, group3):
    groups = [group1, group2, group3]
    group_names = ["Group 1", "Group 2", "Group 3"]

    for name, group in zip(group_names, groups):
        print(f"{name}:")
        print(group)
        print()


# Main program
group_members_names = get_group_members()

print("\nOriginal group order:")
print(group_members_names)

group1, group2, group3 = divide_into_groups(group_members_names)
print_groups(group1, group2, group3)



