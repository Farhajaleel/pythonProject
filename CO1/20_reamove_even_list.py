# From a list of integers , create a list removing even numbers

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_lst = [i for i in list1 if i % 2 != 0]
print("list elements are: ",list1)
print("List after removing even numbers: ",even_lst)
