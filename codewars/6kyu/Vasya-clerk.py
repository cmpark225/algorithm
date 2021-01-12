import unittest

a = { 
    100:[[-1,-1, 1],[-3, 0, 1]],
    50:[[-1, 1, 0], ],
    25:[[1, 0, 0], ]
}

def tickets(people):
    change = [0, 0, 0]
    flag = True
    for i in people:
        for index, tmp in enumerate(a[i]) :
            res = [sum(x) for x in zip(change, tmp)]
            if any( n < 0 for n in res ):
                flag = False
            else:
                change = res
                flag = True
                break;
        if not flag :
            return "NO"
    return "YES"




# b = { 
#     100:[[-1,-1, 1],[-3, 0, 1]],
#     50:[[-1, 1, 0], ],
#     25:[[1, 0, 0], ]
# }

# def tickets(people):
#     change = [0, 0, 0]
#     for i in people:
#         for t in b[i]:
#             if filter(lambda i, n: change[i]-n < 0 , enumerate(t)) :
#                 break;




if __name__ == '__main__':

    test = unittest.TestCase()

    test.assertEquals(tickets([25, 25, 50]), "YES")
    test.assertEquals(tickets([25, 100]), "NO")
    test.assertEquals(tickets([25, 25, 25, 25, 50, 100, 50]), "YES")
    test.assertEquals(tickets([25, 25, 25, 100]), "YES")
    # test.assertEquals(tickets([25, 50, 25, 100]), "YES")

    # [25, 50, 25, 100] 'NO' should equal 'YES'
# [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
# [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
# [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
# [25, 25, 25, 25, 50, 100, 50] 'NO' should equal 'YES'
# [50, 100, 100]
# [25, 25, 100]
# [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]
# [25, 25, 50, 50, 100]
# [25, 50, 50]
# [25, 25, 25, 100] 'NO' should equal 'YES'
# [25, 50, 25, 100] 'NO' should equal 'YES'
# [25, 25, 25, 25, 25, 100, 100]
# [25, 50, 25, 100, 25, 25, 50, 100, 25, 25, 25, 100, 25, 25, 50, 100, 25, 50, 25, 100, 25, 50, 50, 50]
# [25, 25, 25, 100, 25, 25, 25, 100, 25, 25, 50, 100, 25, 25, 50, 100, 50, 50]
# [25, 50, 25, 100, 25, 25, 50, 100, 25, 50, 25, 100, 50, 25]
