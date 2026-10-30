from extract import extract

df = extract()
print(df.head())
print(df.shape)
print(df.isnull().sum())