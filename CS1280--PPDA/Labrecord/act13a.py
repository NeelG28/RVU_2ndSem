import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Salary': [50000, 60000, 70000]})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Department': ['HR', 'IT', 'Finance']})

merged_df = pd.merge(df1, df2, on='ID')
print("\nMerged DataFrame:\n", merged_df)

grouped_df = merged_df.groupby("Department").mean(numeric_only=True)
print("\nGrouped Data:\n", grouped_df)

df3 = pd.DataFrame({'ID': [4, 5], 'Name': ['David', 'Emma'], 'Salary': [80000, 90000]})

concatenated_df = pd.concat([df1, df3], ignore_index=True)
print("\nConcatenated DataFrame:\n", concatenated_df)
