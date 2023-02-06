def calc(base,power):
    assert power>=0 and int(power)==power, 'number not positive integer'
    if power==0: 
        return 1
    else:
        return base * calc(base,power-1)
    
print(calc(2,1))