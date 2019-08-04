import test
import linked_list as list

a1 = [0, 0, 0, 9876, 5432, 1999]
a2 = [1, 8001]
l1 = list.create_list(a1)
l2 = list.create_list(a2)
list.print_list(l1)
list.print_list(l2)
print('-------process-------')
result = list.addTwoHugeNumbers(l1, l2)

list.print_list(result)

