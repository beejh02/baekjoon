def solution(arr, delete_list):
    delete_set = set(delete_list)
    return [item for item in arr if item not in delete_set]