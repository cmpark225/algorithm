
# task path

https://app.codility.com/programmers/lessons/1-iterations/


# my code

```
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    index = [i for i, value in enumerate(bin(N)[2:]) if value == '1']
    
    max = 0
    for i in range(1, len(index)):
        max = max(index[i] - index[i-1] -1, max)

    return max
```


# Todo 

Complexity:
* expected worst-case time complexity is O(log(N));
* expected worst-case space complexity is O(1).

