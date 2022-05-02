#Program to sort a list using Bubble Sort and then reverse the sorted list
num_list = []
n = 0

#Accept numbers from the user
while n != -1:
    n =int(input("Enter a number OR Enter -1 to stop -  "))
    if n > 0:
        num_list.append(n)

print("\tOriginal List - \t",num_list)

for i in range (0,len(num_list)):
    for j in range(i,len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i],num_list[j] = num_list[j],num_list[i]

print("\tSorted List - \t" ,num_list)
num_list.reverse()
print("\tReversed Sorted List - \t\t",num_list)
