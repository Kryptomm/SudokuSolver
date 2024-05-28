# Define the three sets
set1 = {1,2,3}
set2 = set()
set3 = set()

# Step 1: Find the union of all sets
union_all = set1 | set2 | set3

# Step 2: Find the intersection of each pair of sets
intersection_12 = set1 & set2
intersection_13 = set1 & set3
intersection_23 = set2 & set3

# Step 3: Find all numbers that are in more than one set
common_elements = intersection_12 | intersection_13 | intersection_23

# Step 4: Subtract common elements from the union to find unique elements
unique_elements = union_all - common_elements

# Step 5: Determine which set each unique element belongs to
unique_in_set1 = unique_elements & set1
unique_in_set2 = unique_elements & set2
unique_in_set3 = unique_elements & set3

# Output the results
print("Numbers only in set1:", unique_in_set1)
print("Numbers only in set2:", unique_in_set2)
print("Numbers only in set3:", unique_in_set3)
