import pandas as pd

#Using Normalizer
df=pd.read_csv('3Salary_Data.csv')

from sklearn.preprocessing import Normalizer

normalizer=Normalizer()
normalized_data=normalizer.fit_transform(df)
normalized_df1=pd.DataFrame(normalized_data,columns=df.columns)
normalized_df1

#Using MinMaxScaler
df=pd.read_csv('3Salary_Data.csv')

from sklearn.preprocessing import MinMaxScaler

minmaxscaler=MinMaxScaler()
minmaxscaled_data=minmaxscaler.fit_transform(df)
minmaxscaled_df1=pd.DataFrame(minmaxscaled_data,columns=df.columns)
minmaxscaled_df1

