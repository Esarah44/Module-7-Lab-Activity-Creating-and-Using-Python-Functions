# Create Python function Unique(lst)
# Sara Hernandez
# 11/13/2022
# append function to create a new list where elements are unique

lst = [1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]

def Unique(lst):
    unique_lst=[]
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

x=Unique(lst)
print(x)