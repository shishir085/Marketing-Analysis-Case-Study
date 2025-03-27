import pandas as pd
from operations import *


best_s = (
    m_df.groupby("PROD_NAME")["TOT_SALES"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("Top 3 Most Profitable Products are: \n")
print(best_s)
best_s.to_csv("dataset/best_seller") 
print(f"\nTop 3 Most Profitable Products list saved to 'best_seller.csv'\n")



"""
x = int(input("Enter Number of Top Best Seller Products : "))
best_s = (
    m_df.groupby("PROD_NAME")["TOT_SALES"]
    .sum()
    .sort_values(ascending=False)
    .head(x)
)
print(f"\nTop {x} Most Profitable Products are: \n")
print(best_s)
print(f"\nTop {x} Most Profitable Products list saved to 'best_seller.csv'\n")
"""
