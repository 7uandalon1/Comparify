# We need to import pandas as pd
import pandas as pd

df = pd.read_excel(r'./datos.xlsx')
print(df.to_json())