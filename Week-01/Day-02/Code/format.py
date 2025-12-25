# format specifier in python
import math
print("The mangy, scrawny stray dog %s gobbled down" %'hurriedly' + 
      "the grain-free, organic dog food.")
x = 'Humans'
y = 'turn'

print("Misha %s and %s around"%('walked',y))
print('The value of pi is: %5.2f' %(math.pi))  #  3.14

print('We all are {}.'.format('equal')) # format string method
print(f'We all are {x}.')  # f-string
print('{2} {1} {0}'.format('directions',
                           'the', 'Read'))

price1 = 424.3534
price2 = 23.5343
price3 = 1234.1234

print(f"Prices are: {price1:.2f}, {price2:.3f}, and {price3:.1f}")
print(f"Prices are: {price1:.<10}, {price2:<10}, and {price3:<10}")
print(f"Prices are: {price1:*>10}, {price2:*>10}, and {price3:*>10}")
print(f"Prices are: {price1:^10}, {price2:^10}, and {price3:^10}")