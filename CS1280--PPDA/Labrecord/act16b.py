import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Ad_Spend": [100, 200, 300, 400, 500, 600, 700],
    "Sales": [20, 40, 55, 70, 90, 110, 130]
})

# **Scatter Plot**
plt.figure(figsize=(7, 5))
sns.scatterplot(x="Ad_Spend", y="Sales", data=df, color="r", s=100)
plt.title("Relationship Between Advertising Spend and Sales")
plt.xlabel("Advertising Spend ($)")
plt.ylabel("Sales")
plt.show()
