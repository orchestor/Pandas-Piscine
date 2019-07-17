import pandas as pd
from io import StringIO

csv_data = \
    '''A, B, C, D
       1.0, 2.0, 3.0, 4.0
5.0, 6.0, , 8.0
10,11,0.23 '''

# Handle space with skipinitialspace = True option
df = pd.read_csv(StringIO(csv_data), skipinitialspace=True)
print(df)
stats_df = df.isnull().sum()
print(stats_df)

# Convert to numpy object
print(df.values)
