import helper

def test_sort(sort_func, a = None, num_sample = 20):
    if not a:
        a = helper.init_arr(length=num_sample)

    print(a)
    sort_func(a)
    print(a)
    print(helper.check_order(a))


