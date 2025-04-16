import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample DataFrame
df = sns.load_dataset("iris")  

sns.pairplot(df, hue="species")  
plt.show()
