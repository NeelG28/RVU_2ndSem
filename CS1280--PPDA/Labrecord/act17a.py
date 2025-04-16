import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Department": ["HR", "IT", "Finance", "Marketing"],
    "Salary": [55000, 80000, 75000, 65000]
})

# **Bar Plot**
plt.figure(figsize=(8, 5))
sns.barplot(x="Department", y="Salary", data=df, palette="viridis")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()
