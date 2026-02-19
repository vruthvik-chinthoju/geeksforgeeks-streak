class Solution:
    def missing_element(arr,low,right):
        result = []

        arr = set(arr)

        for i in range(low,right+1):
            if i in arr:
                continue
            else:
                result.append(i)

        return result