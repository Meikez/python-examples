one = [1,2,4]
two = [1,3,4]
# we order the both lists
for o in range(len(one)):
    for t in range(len(one)-1):
        if one[t] > one[t+1]:
            aux = one[t+1]
            one[t+1] = one[t]
            one[t] = aux
        if two[t] > two[t+1]:
            aux = two[t+1]
            two[t+1] = two[t]
            two[t] = aux

# create a new with both list order
new_list = []
for o in range(len(one)):
    for t in range(len(one)):
        if one[t] > two[t]:
            smaller = one[t]
            new_list.append(new_list)

print(new_list)




# Bubble method sort
# example = [3,2,4,1,5]
#
# for n in range(len(example)-1):
#     for itr in range(len(example)-1):
#         if example[itr] > example[itr+1]:
#             aux = example[itr+1]
#             example[itr+1] = example[itr]
#             example[itr] = aux
#             print(f"itr {itr} {example}")
#     print(f"n {example}")
#
#
# print(f"Fina: {example}")


