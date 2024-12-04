#List Assignment
first_name="Emmanuel"
middle_name = "Manasoko"
last_name = "Mamman"
martic_num = "BHU/24/04/10/0037"

list= [1,2,3,4,5,6,7,8,9,10]
list_sum= 0
for number in list:
    list_sum += number
    print(list_sum)

# Another method of the reverse function
for i in range(len(list)):
    list.insert(i,list.pop())
    print(i,list)

