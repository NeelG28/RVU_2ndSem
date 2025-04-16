import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating Sample Time-Series Data
df = pd.DataFrame({
    'Year': range(2010, 2021),
    'Sales': [50, 60, 75, 85, 90, 120, 130, 140, 150, 165, 180]
})

# **Line Chart**
plt.figure(figsize=(8, 5))
sns.lineplot(x="Year", y="Sales", data=df, marker="o", color="b")
plt.title("Sales Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()
