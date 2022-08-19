
from lib2to3.pytree import convert
import urllib.request
import json
import csv
from datetime import date

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as url:
    data = json.loads(url.read().decode())
    print(data)
    print("")

# x = "\"" + str(data) + "\""
# x = ' """ ' + str(data) + ' """ '
x = data
s1 = json.dumps(x)
x = json.loads(s1)
todaydate = date.today()
fileName = "Report_" + str(todaydate)
f = csv.writer(open(fileName + ".csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["ID", "NAME", "USERNAME", "EMAIL", "STREET",
           "CITY", "ZIPCODE", "LATITUDE", "LNG"])

for x in x:
    f.writerow([x["id"],
                x["name"],
                x["username"],
                x["email"],
                x["address"]["street"],
                x["address"]["city"],
                x["address"]["zipcode"],
                x["address"]["geo"]["lat"],
                x["address"]["geo"]["lng"]])
