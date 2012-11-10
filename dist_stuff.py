def bucket(nums, n):
    ma = max(nums)
    mi = min(nums)
    buckets = [mi+i*(ma-mi)/float(n) for i in range(n)]
    return buckets

def hist(nums, n):
    hist = range(n)
    b = bucket(nums, n)
    for i in range(n):
        hist[i] = [x for x in nums if x > b[i] and (i == n-1 or x < b[i+1])]
    return hist
