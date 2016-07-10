def subset(array, num):
    result = []
    def find(arr, num, path=()):
        if not arr:
            return None
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    return result

print subset([10, 2, 3, 4, 5, 9, 7, 8], 23)



