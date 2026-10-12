import csv
import requests

FILENAME = "data.csv"
DATADIR = "" # empty means "same direction as this file"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        count += 1

print(f"average is{total/count}")

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data['northern-ireland']['events'][0])
