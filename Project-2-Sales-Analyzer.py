#Project #2
#E-Commerce Sales Analyzer
import numpy as np
from numpy import random

sales=np.random.randint(500,5001,size=30)
total_sale=np.sum(sales)
avg=np.mean(sales)
max_sale=np.argmax(sales)+1
min_sale=np.argmin(sales)+1
normalised_sales=np.round((sales/5000),2)
above_4000=sales>4000


print(f"Sales of the Month:\n{sales}")
print(f"Total Sale: {total_sale}")
print(f"Daily Average Sale: {avg}")
print(f"Day with Maximum Sale: {max_sale}")
print(f"Day with Minimum Sale: {min_sale}")
print(f"Normalized Sales (0-1): {normalised_sales}")
print(f"All Sales above 4000:\n{sales[above_4000]}")