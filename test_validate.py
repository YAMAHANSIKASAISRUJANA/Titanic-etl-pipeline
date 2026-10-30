
from extract import extract
from transform import transform
from validate import validate

raw = extract()
clean = transform(raw)
validate(clean)
