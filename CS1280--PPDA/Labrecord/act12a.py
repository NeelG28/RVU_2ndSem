import matplotlib.pyplot as plt
import seaborn as sns

# Creating a sample dataset with an outlier
df = pd.DataFrame({'Values': [10, 12, 15, 18, 50]})

# Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, y="Values")
plt.title("Boxplot for Outlier Detection")
plt.show()
