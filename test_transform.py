
from extract import extract
from transform import transform

raw = extract()
clean = transform(raw)
print(clean.head())
print(clean.shape)
print(clean.isnull().sum())
