n = int(input())

words = list(map(str, input().split()))

def shiritori_valid_check(arr):
    first = arr[0][0]
    for i in range(len(arr)):
        if(first != arr[i][0]):
            return False
        
def palindrome_check(arr):
    for i in arr:
        if(i != i[::-1]):
            return False
        
if(shiritori_valid_check(words) == None and palindrome_check(words) == None):
    print(1)
else:
    print(0)