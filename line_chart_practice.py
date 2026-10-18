import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
revenue = [50000, 65000, 55000, 80000]

plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (LKR)")
plt.show()