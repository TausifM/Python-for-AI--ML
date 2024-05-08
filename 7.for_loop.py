expenses = [1200, 1300, 1400]

total = 0

for expense in expenses: 
    total= total + expense
    
print(total) # 3900

key_location=  'chair'
locations=['chair', 'table', 'sofas']

for key in locations : 
    if key == key_location:
        print(f'key found on {key}')
        break # break use
    else:
        print('key not found')
        
        
# print odd number 0 to 10

for i in range(11): 
    if i%2==0:
        continue # continue
    print(i)
    
    
# while loop - in for loop numbers are adding and shown serially automatically but here we have to add manually
n=0

while n<=10:
    print(n)
    n=n+1