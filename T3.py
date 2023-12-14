#Write a python code for the following:
#1. Create a list of 5 elements
#2. Add an element to the list (Any element)
#3. Delete an element from the list (The middle element)
#4. Sort the list
#5. Print the list
#6. Print the length of the list
#7. Print the largest number in the list
#8. Print the smallest number in the list
#9. Print the sum of the elements of the list

#1. Create a list of 5 elements
#Take a list input from the user
list1 = [5,10,15,80,90,100,600]
"""for i in range(5):
    list1.append(int(input("Enter a number:")))
print("List 1: ",list1)"""

#2. Add an element to the list (Any element)
list1.append(6)
print("List 1 after adding 6: ",list1)

#3. Delete an element from the list (The middle element)
list1.pop(3)
print("List 1 after deleting the 4th element: ",list1)

#4. Sort the list
list1.sort()
print("List 1 after sorting: ",list1)

#5. Print the list
print("List 1: ",list1)

#6. Print the length of the list
print("Length of List 1: ",len(list1))

#7. Print the largest number in the list
print("Largest number in List 1: ",max(list1))

#8. Print the smallest number in the list
print("Smallest number in List 1: ",min(list1))

#9. Print the sum of the elements of the list
print("Sum of elements of List 1: ",sum(list1))

#10. Print the list in reverse order
print("List 1 in reverse order: ",list1[::-1])

#11. Print the list in reverse order without using the reverse function
print("List 1 in reverse order without using reverse function: ",list1[-1:-len(list1)-1:-1])

#12. Print the list in reverse order without using the reverse function and without using the negative indexing
print("List 1 in reverse order without using reverse function and negative indexing: ",list1[len(list1)::-1])

#13. Print the list in reverse order without using the reverse function and without using the negative indexing and without using the len function
print("List 1 in reverse order without using reverse function, negative indexing and len function: ",list1[4::-1])
