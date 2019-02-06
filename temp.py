    
def blackrock(PP, CH):
    PP = int(PP*100)
    CH = int(CH*100)    
    coins = { 
    1: 'PENNY',
    5: 'NICKEL',
    10: 'DIME',
    25: 'QUARTER',
    50: 'HALF DOLLAR',
    100: 'ONE',
    200: 'TWO',
    500: 'FIVE',
    1000: 'TEN',
    2000: 'TWENTY',
    5000: 'FIFTY',
    10000: 'ONE HUNDRED'
    }
    coins_array = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 
    25, 10, 5, 1]
    difference = CH - PP
    change = []
    if PP > CH:
        print('ERROR')
    elif PP == CH:
        print('ZERO')
    for coin in coins_array:
        while difference >= coin:
            change.append(coins[coin])
            difference -= coin
    return ",".join(change)

print(blackrock(300, 600))