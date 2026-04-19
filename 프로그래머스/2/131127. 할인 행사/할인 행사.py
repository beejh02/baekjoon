def solution(want, number, discount):
    answer = 0
    arr = dict(zip(want, number))

    now = {}
    for i in range(10):
        now[discount[i]] = now.get(discount[i], 0) + 1

    if now == arr:
        answer += 1

    for i in range(1, len(discount) - 9):
        out_item = discount[i - 1]
        now[out_item] -= 1
        if now[out_item] == 0:
            del now[out_item]

        in_item = discount[i + 9]
        now[in_item] = now.get(in_item, 0) + 1

        if now == arr:
            answer += 1
    return answer