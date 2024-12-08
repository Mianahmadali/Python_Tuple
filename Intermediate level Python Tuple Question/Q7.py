"""Join two tuples using a loop.

Write a loop to join two tuples t1 = (1, 2) and t2 = (3, 4) into a single tuple."""

t1 = (1,2)
t2 = (3,4)
result = ()
for items in t1:
  result +=(items,)

for items in t2:
    result += (items,) 


print(result)   