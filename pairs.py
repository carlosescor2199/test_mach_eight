def get_pairs(arr: [int], target_sum: int):
    mydict = dict()
    result = []

    for i in range(len(arr)):
        temp = target_sum - arr[i]

        if temp in mydict:
            count = mydict[temp]
            for j in range(count):
                result.append((temp, arr[i]))

        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1

    return result
