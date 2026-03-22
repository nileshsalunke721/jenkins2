import requests
import pandas as pd
import os 


token=os.getenv("API_KEY")
if token == "1234":
    resp=requests.get("https://jsonplaceholder.typicode.com/users")
    data=resp.json()
    df = pd.DataFrame(data)
    print(df)
else:
    print("Invalid API key")
