import pandas as pd
from data_clear import *

df = load_file("products.xlsx")

print("До очистки:")
print(get_shape(df))
print(get_null_info(df))

df = clean_data(df)

print("После очистки:")
print(get_shape(df))
print(get_null_info(df))

print(get_numeric_stats(df))
print(get_top_values(df))