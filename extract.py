import requests
import pandas as pd


resp=requests.get("https://jsonplaceholder.typicode.com/users")
data=resp.json()
df = pd.DataFrame(data)
print(df)
