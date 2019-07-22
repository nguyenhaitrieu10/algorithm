import sort

a = [0] * 45
sort.init_arr(a)
print(a)

sort.merge_sort(a, 0, len(a) - 1)

print(a)
print(sort.check_order(a))


