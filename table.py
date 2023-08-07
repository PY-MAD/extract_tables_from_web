from urllib.request import Request, urlopen
import pandas as pd
import os
import csv

list_dir = os.listdir()
check = False
for i in list_dir:
    if(i == ".DataBase"):
        check = True
if check == False:
    os.mkdir(".DataBase")
input_url = input(str("put the url here please >>> "))
input_match = input(str("please write the first name in your list >>> "))
url = input_url

#Create an abstraction of URL request
request = Request(url)

#Add headers to the request
request.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')

#Open the URL
page = urlopen(request)

#Read HTML content
html_content = page.read()
table = pd.read_html(url, match=f"{input_match}")
print("wating. . .")
print(f"you have {len(table)} tables")
names = True
named = []
while names:
    name = input(str("Named For First One >>> "))
    named.append(name)
    q_name = input(str("do you want to named all your tables ? { yes } { no } >>> "))
    if q_name.lower() == "yes":
        for i in range(len(table)):
            nameList = input(str(f"please named all of them start with {i+1}"))
            named.append(nameList)
    else:
        names = False

for i, tables in enumerate(table, start=1):
    file_name = f'.DataBase/unreadable{i}.csv'
    tables.to_csv(file_name)
    read_file = pd.read_csv(f".DataBase/unreadable{i}.csv")
    if len(named) > 1:
        read_file.to_excel(f"{named[i]}{i}.xlsx", index=None, header=True)
    else:
        read_file.to_excel(f"{named[0]}{i}.xlsx", index=None, header=True)
print("all tables has been created")