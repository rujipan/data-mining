import matplotlib.pyplot as plt

# Example data
years = [2018, 2019, 2020, 2021, 2022]
sales = [150, 200, 250, 300, 400]

# Create a line chart
plt.plot(years, sales, marker='o', linestyle='-', color='blue', label='Sales')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Annual Sales Over Time')
plt.grid(True)
plt.legend()

# Show the chart
plt.show()
