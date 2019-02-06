test = "Google,STOCK,10,50,0,Microsoft,STOCK,15,50,0,IBM,BOND,15,100,0.05,IBM,BOND,20,100,0.05,Google,STOCK,15,50,0,Microsoft,STOCK,10,50,0.05"
a = test.split(',')
# print(a)
prices ={}
tracker = 0
# print(a[::5])

prices = {}
price_index = 2
company_index = 0
for i in range(6):
    if a[company_index] in prices:
        prices[a[company_index]] -= int(a[price_index])
    else:
        prices[a[company_index]] = int(a[price_index])
    # print(a[company_index] ,a[price_index])
    price_index += 5
    company_index += 5

for i in prices:
    if prices[i] > 0:
        print ('SELL', i, abs(prices[i]))
    elif prices[i] < 0:
        print ('BUY', i, abs(prices[i]))



    
        
    




