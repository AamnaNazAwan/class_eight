import pandas as pd
'''data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age' : [22,30,35],
    'City' : ['New York', 'Los Angles', 'Chicago']
}
df = pd.DataFrame(data)
df.to_excel('new.xlsx', sheet_name='saleData', index = False)
print("\nData written to sale 'new.xlsx'.")

df_filetered_columns = df[['Name','Age']]
df_filetered = df_filetered_columns[df_filetered_columns['Age'] > 25]
print("Filtered DataFrame:\n",df_filetered)


df_filetered.to_excel('output.xlsx', sheet_name='AgeData', index = False)
print("\nData written to 'output.xlsx'.")'''

df = pd.read_csv('mARCqc.csv')
print(df)


type_counts = df['type'].value_counts()
print("\nCounts of each type(Movie and TV Show:")
print(type_counts)

country_counts = df['country'].value_counts('type'== 'Movie')
print(country_counts)

country_counts.to_excel('four.xlsx', sheet_name='AgeData', index = False)
print("\nData written to 'four.xlsx'.")

print(country_counts.to_excel)
