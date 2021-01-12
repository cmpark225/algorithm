import unittest

def longest_consec(strarr, k):
    if k <= 0 or k >len(strarr):
        return ""
        
    index = 0
    for i in range(len(strarr)-k+1):
        if sum(len(x) for x in strarr[i:i+k]) > sum(len(x) for x in strarr[index:index+k]):
            index = i

    return ''.join(strarr[index:index+k])
    




 
if __name__ == '__main__':
    Test = unittest.TestCase()

    def testing(actual, expected):
        Test.assertEquals(actual, expected)

    testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
    testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
    testing(longest_consec([], 3), "")
    testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
    testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
    testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
    testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
    testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
