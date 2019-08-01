import helper
import postfix
import sort


def test_sort(sort_func=sort.flash_sort, a = None, num_sample = 20):
    if not a:
        a = helper.init_arr(length=num_sample)

    print("----------Array----------")
    print(a)
    sort_func(a)
    print("-------Sorted Array------")
    print(a)
    print(helper.check_order(a))


def test_postfix(s="  5.5  /2 + 3*(4/8 -2)  ", expected_result=-1.75):
    print("-----------Input-----------")
    print(s)
    result = postfix.calculate(s)
    print("-----------Result-----------")
    print(result)
    print("-------Expected Result-------")
    print(expected_result)


