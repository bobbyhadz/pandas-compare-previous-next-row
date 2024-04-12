# Comparing Previous row values in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'experience': [1, 1, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

df['prev_equal'] = df['experience'].eq(df['experience'].shift())

#     name  experience  salary  prev_equal
# 0  Alice           1   175.1       False
# 1  Bobby           1   180.2        True
# 2   Carl           5   190.3       False
# 3    Dan           7   205.4       False
# 4  Ethan           7   210.5        True
print(df)