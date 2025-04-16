import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample Data
data = np.random.normal(loc=50, scale=15, size=500)  # Normal Distribution
df = pd.DataFrame({'Values': data})

# **Histogram with KDE (Kernel Density Estimate)**
plt.figure(figsize=(8, 5))
sns.histplot(df['Values'], kde=True, bins=30)
plt.title("Histogram & KDE of Values")
plt.show()

# **Boxplot to Identify Outliers**
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Values'])
plt.title("Box Plot for Value Distribution")
plt.show()
