import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Groceries"]
revenue = [150000, 90000, 120000]

plt.bar(categories, revenue)
plt.title("Revenue by Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue (LKR)")
plt.show()