def sumofno(n):
    assert n>=0 and int(n)==n, 'The number is negative'
    if n==0:
        return 0
    else:
        return int(n%10)+sumofno(int(n/10))

print(sumofno(12323))