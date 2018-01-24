##Rebecca TeKolste
##Problem 4

yours = ["Yale", "MIT", "Berkeley"]
mine = ["Northwestern", "Indiana", "Purdue"]

ours1 = mine + yours

ours2 = []
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)

#1. ours1 and ours2 are visibly different from each other in that
#there are two sets of brackets in ours2 and only 1 set in ours1.
#This is because ours2 is a list of lists. That is to say that the
# ours2 takes the form [[list],[list]],
#whereas ours1 takes the form [entry, entry, entry....].

#2. Code below.
print (yours[1])
yours[1] = "Sanford"
print(ours1)
print(ours2)

#ours1 did not change because it was assigned when I created
#it as a variable. ours2 changed becuase it is formed by taking
#each list as an item and pulling that list into the new list.
#Therefore, when yours is changed, ours2 is changed as well.
