import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/"
r = requests.get(url)
#print(r.status_code)
soup = BeautifulSoup(r.text, "html.parser")

table = soup.find("table", class_="table table-sm table-hover screenertable")
headers = table.find_all("th")
#print(headers)
titles = []
for i in headers:
    names = i.getText()
    titles.append(names)

df = pd.DataFrame(columns=titles)

#print(titles)
row = table.find_all("tr")
#print(row)
    
#print(df)
for i in row[1:]:
    data = i.find_all("td")
    rows = [tr.text.strip() for tr in data]
    #print(rows)
    l = len(df)
    df.loc[l] = rows
        
print(df)

df.to_csv("stock_market_data.csv", index=False)