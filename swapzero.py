# given list [0,1,0,3,12]   swap zeros to last without changing the order of other numbers   : output should be like that [1,3,12,0,0]

list1 = [0,1,0,3,12]

list2 = [] 
list3 = []

for i in list1 :
    if i == 0 :
        list2.append(i)
    else :
        list3.append(i)
        
print(list3 + list2 )  