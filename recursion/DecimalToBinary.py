def DecToBin(n):
    assert int(n)==n, 'Number is negative'
    if n ==0:
        return 0
    else:
        return n%2 + 10 * DecToBin(int(n/2))
    
print(DecToBin(5))