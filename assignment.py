#  Given an array of Red Green Blue balls.You have to sort it. 
# Constraint : Time complexity O(n) 
# Constraint : Space complexity O(1) 
# Example: 
# Input: [R, G, B, G, G, R, B, B, G] 
# Output : [B,B,B,G,G,G,G,R, R] 

#python

def sort_List(list_a):

    count_B = list_a.count("B")
    count_G = list_a.count("G")
    count_R = list_a.count("R")

    list_a[:count_B] = ["B"]* count_B
    list_a[count_B:count_B+count_G] = ["G"] * count_G
    list_a[count_B+count_G:] = ["R"] * count_R

    return list_a

list_a = ["R", "G", "B","G,","G","R","B","B","G"]
result = sort_List(list_a)


