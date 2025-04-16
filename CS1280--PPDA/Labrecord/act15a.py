import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(10, 4), columns=["A", "B", "C", "D"])

corr_matrix = df.corr()

# **Plot Heatmap**
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
