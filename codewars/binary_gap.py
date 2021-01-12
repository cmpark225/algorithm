def solution(N):
    index = [ i for i, value in enumerate(N) if value == '1']

    gap = 0
    for i in xrange(1, len(index)):
        gap = max([index[i] - index[i-1] -1, gap])

    return gap




if __name__ == '__main__':
    print solution(9) == 2
    print solution(529) == 4
    print solution(20) == 1
    print solution(15) == 0
