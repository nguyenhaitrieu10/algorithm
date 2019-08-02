import test
import postfix
import search
import helper
import sort
import adhoc

N = 20
# a = [0] * N
a = helper.init_arr(N)
a.sort()
strange = 9
b = a[:strange]
c = a[strange:]
a = c + b
print(a)
print(adhoc.sea_search(a, a[11]))

