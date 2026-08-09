import pandas as pd
import matplotlib.pyplot as plt
# Read the dataset
data = pd.read_csv("sales_data.csv", sep="\t")

# Display the dataset
print(data)
# Calculate total sales
total_sales = data["Sales"].sum()

print("\nTotal Sales:")
print(total_sales)

# Calculate total profit
total_profit = data["Profit"].sum()

print("\nTotal Profit:")
print(round(total_profit, 2))

# Calculate total quantity sold
total_quantity = data["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(total_quantity)

# Calculate average sales
average_sales = data["Sales"].mean()

print("\nAverage Sales:")
print(round(average_sales, 2))
# Product-wise Sales
product_sales = data.groupby("Product Name")["Sales"].sum()

print("\nProduct-wise Sales:")
print(product_sales)

# Best-selling product
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print("\nBest-Selling Product:")
print("Product:", best_product)
print("Sales:", best_product_sales)

# Product-wise Profit
product_profit = data.groupby("Product Name")["Profit"].sum()

print("\nProduct-wise Profit:")
print(product_profit)

# Most profitable product
most_profitable = product_profit.idxmax()
most_profitable_profit = product_profit.max()

print("\nMost Profitable Product:")
print("Product:", most_profitable)
print("Profit:", round(most_profitable_profit, 2))
# Category-wise Sales
category_sales = data.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

# Best-selling category
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\nBest-Selling Category:")
print("Category:", best_category)
print("Sales:", best_category_sales)

# Category-wise Profit
category_profit = data.groupby("Category")["Profit"].sum()

print("\nCategory-wise Profit:")
print(category_profit)

# Most profitable category
most_profitable_category = category_profit.idxmax()
most_profitable_category_profit = category_profit.max()

print("\nMost Profitable Category:")
print("Category:", most_profitable_category)
print("Profit:", round(most_profitable_category_profit, 2))
# Region-wise Sales
region_sales = data.groupby("Region")["Sales"].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Best-selling region
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()

print("\nBest-Selling Region:")
print("Region:", best_region)
print("Sales:", best_region_sales)

# Region-wise Profit
region_profit = data.groupby("Region")["Profit"].sum()

print("\nRegion-wise Profit:")
print(region_profit)

# Most profitable region
most_profitable_region = region_profit.idxmax()
most_profitable_region_profit = region_profit.max()

print("\nMost Profitable Region:")
print("Region:", most_profitable_region)
print("Profit:", round(most_profitable_region_profit, 2))
# Product-wise Sales Graph

plt.figure(figsize=(10, 5))

product_sales.plot(kind="bar", color="teal")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()


# Category-wise Sales Graph

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar", color="royalblue")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()


# Region-wise Sales Graph

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar", color="seagreen")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()


# Product-wise Profit Graph

plt.figure(figsize=(10, 5))

product_profit.plot(kind="bar", color="mediumpurple")

plt.title("Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Total Profit")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_profit.png")
plt.show()


# Category-wise Sales Distribution

plt.figure(figsize=(6, 6))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["skyblue", "seagreen", "mediumpurple"]
)

plt.title("Category-wise Sales Distribution")
plt.savefig("category_distribution.png")
plt.show()