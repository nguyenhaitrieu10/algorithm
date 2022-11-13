# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def create_list(a):
    l = ListNode(0)
    p = l
    for i in a:
        p.next = ListNode(i)
        p = p.next

    if l.next != None:
        l = l.next
    return l


def print_list(l):
    p = l
    while p:
        print(p.value, end=" ")
        p = p.next
    print()

def formatList(l):
    if l.next == None:
        return l

    p = l
    while p and p.value == 0:
        p = p.next

    if p != None:
        l = p
    else:
        l = ListNode(0)

    return l


def reverseList(l):
    p = l
    p_prev = None
    while p != None:
        p_next = p.next
        p.next = p_prev
        p_prev = p
        p = p_next

    return p_prev


def addTwoHugeNumbers(a, b):
    if a == None or b == None:
        return None

    a_reversed = reverseList(formatList(a))
    b_reversed = reverseList(formatList(b))

    pa = a_reversed
    pb = b_reversed

    result = ListNode(0)
    p = result
    rem = 0
    while pa and pb:
        p.value = (pa.value + pb.value + rem) % 10000
        rem = (pa.value + pb.value + rem) // 10000

        pa = pa.next
        pb = pb.next
        p.next = ListNode(0)
        p = p.next

    while pa:
        p.value = (pa.value + rem) % 10000
        rem = (pa.value + rem) // 10000

        pa = pa.next
        p.next = ListNode(0)
        p = p.next

    while pb:
        p.value = (pb.value + rem) % 10000
        rem = (pb.value + rem) // 10000

        pb = pb.next
        p.next = ListNode(0)
        p = p.next

    if rem > 0:
        p.value = rem

    result = reverseList(result)

    if rem == 0:
        result = result.next

    return result

