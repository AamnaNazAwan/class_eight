import pandas as pd

df = pd.read_csv('pandas.csv')
print("DataFrame read from CSV:")
print(df)

df['cumulative sales'] = df['sale'].cumsum()
print("\nDataFrame after manipulation:")
print(df)

df.to_excel('pandas1.xlsx', sheet_name='salesData', index = False)
print("\nData written to 'pandas.xlsx'.")

print(df.to_excel)

data = {
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
}
df = pd.DataFrame(data, index=['a','b','c'])
print("DataFrame:")
print(df)
#select a single column
column_a = df.A
print(column_a)

#select a multiple columns df[['A
columns_ab= df[['A','B']]
print("column A and B:\n",columns_ab)

#FOR ANY SPECIFIC DATA WE USE(.at)
value_at = df.at['b','A']
print("Value at row 'a' and column 'A':",value_at)

#access the value in the first row and first column
value_iat = df.iat[0,0]
print("Value at first row and first column:",value_iat)

#filter the dataFrame where values in column 'A' are greater than 1
filtered_df= df[df['A'] > 1]
print("\nRows where 'A' > 1")
print(filtered_df)

filtered_df= df[(df['A'] > 1) & (df['B'] > 1)]
print("\nRows where 'A' > 1")
print(filtered_df)

filtered_df = df.query('A > 1 and B < 8')
print("Rows where 'A > 1 and B < 8' using query:\n",filtered_df)


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age' : [22,30,35],
    'City' : ['New York', 'Los Angles', 'Chicago']
}
df = pd.DataFrame(data)
#SELECT SPECIFIC COLUMN
df_filetered_columns = df[['Name','Age']]

#filter rows where Age is greater than 25
df_filetered = df_filetered_columns[df_filetered_columns['Age'] > 25]
print("Filtered DataFrame:\n",df_filetered)

df.to_excel('new.xlsx', sheet_name='salesData', index = False)
print("\nData written to 'pandas.xlsx'.")