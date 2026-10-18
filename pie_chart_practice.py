import matplotlib.pyplot as plt
categories = ["Electronics", "Clothing", "Groceries"]
orders = [150, 90, 120]

plt.pie(orders, labels=categories, autopct="%1.1f%%")
plt.title("Orders By Category")
plt.show()