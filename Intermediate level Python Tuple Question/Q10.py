"""Find the common elements between two tuples.

Given two tuples t1 = (1, 2, 3) and t2 = (3, 4, 5), find the common elements."""

t1 = (1,2,3)
t2 = (3,4,5)
common_elements = set(t1) & set(t2)
common_elements_tuple = tuple(common_elements)
print("Common elements:", common_elements_tuple)