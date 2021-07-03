def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for pa_num in leaves:
            tmp.append(pa_num + num)
            tmp.append(pa_num - num)
        leaves = tmp
        print(leaves)
    answer = leaves.count(target)
    return answer