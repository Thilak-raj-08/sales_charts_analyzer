import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Month": [
        "Jan", "Jan", "Jan",
        "Feb", "Feb", "Feb",
        "Mar", "Mar", "Mar",
        "Apr", "Apr", "Apr",
        "May", "May", "May",
        "Jun", "Jun", "Jun",
        "Jul", "Jul", "Jul",
        "Aug", "Aug", "Aug",
        "Sep", "Sep", "Sep",
        "Oct", "Oct", "Oct",
        "Nov", "Nov", "Nov",
        "Dec", "Dec", "Dec"
    ],
    "Product_Category": [
        "Electronics", "Clothing", "Groceries"
    ] * 12,
    "Revenue": [
        150000, 90000, 120000,
        165000, 95000, 125000,
        140000, 85000, 118000,
        190000, 140000, 150000,
        170000, 100000, 130000,
        180000, 110000, 135000,
        195000, 115000, 140000,
        185000, 120000, 145000,
        210000, 125000, 150000,
        225000, 130000, 155000,
        250000, 145000, 165000,
        300000, 180000, 190000
    ],
    "Orders": [
        150, 180, 400,
        165, 190, 420,
        140, 170, 390,
        190, 280, 500,
        170, 200, 430,
        180, 220, 450,
        195, 230, 470,
        185, 240, 480,
        210, 250, 500,
        225, 260, 520,
        250, 290, 550,
        300, 360, 630
    ],
    "Profit": [
        30000, 27000, 12000,
        33000, 28500, 12500,
        28000, 25500, 11800,
        38000, 42000, 15000,
        34000, 30000, 13000,
        36000, 33000, 13500,
        39000, 34500, 14000,
        37000, 36000, 14500,
        42000, 37500, 15000,
        45000, 39000, 15500,
        50000, 43500, 16500,
        60000, 54000, 19000
    ]
}

df = pd.DataFrame(data)
print(df.shape)

monthly_revenue = df.groupby("Month", sort=False)["Revenue"].sum()
print(monthly_revenue)

plt.figure(figsize=(10,5))
plt.plot(monthly_revenue.index, monthly_revenue.values , label = "Revenue")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()
plt.show()


category_revenue = df.groupby("Product_Category")["Revenue"].sum()
print(category_revenue)

plt.figure(figsize=(8,5))
plt.bar(category_revenue.index, category_revenue.values, label="Revenue")
plt.title("Revenue by Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()
plt.show()


category_orders = df.groupby("Product_Category")["Orders"].sum()
print(category_orders)

plt.figure(figsize=(7,7))
plt.pie(category_orders.values, labels = category_orders.index, autopct="%1.1f%%")
plt.title("Orders by Category")
plt.legend()
plt.tight_layout()
plt.show()


highest_revenue_month = monthly_revenue.idxmax()
print(monthly_revenue.loc[highest_revenue_month])
print(highest_revenue_month)

lowest_revenue_month = monthly_revenue.idxmin()
print(monthly_revenue.loc[lowest_revenue_month])
print(lowest_revenue_month)

category_profit = df.groupby("Product_Category")["Profit"].sum()
most_profitable_category = category_profit.idxmax()
print(category_profit)
print(category_profit.loc[most_profitable_category])
print(most_profitable_category)

highest_orders_category = category_orders.idxmax()
print(category_orders.loc[highest_orders_category])
print(highest_orders_category)

monthly_profit = df.groupby("Month", sort=False)["Profit"].sum()
print(monthly_profit)


plt.figure(figsize=(10,5))
plt.plot(monthly_revenue.index, monthly_revenue.values, label = "Revenue")
plt.plot(monthly_profit.index, monthly_profit.values, label = "Profit")
plt.title("Monthly Revenue vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()