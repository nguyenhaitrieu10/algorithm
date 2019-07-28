import sort

N = 45
a = [0] * N
sort.init_arr(a)
print(a)

sort.flash_sort(a)

print(a)
print(sort.check_order(a))


