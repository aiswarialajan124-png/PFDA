import requests

# Get bank holidya data from UK government website
response = requests.get("https://www.gov.uk/bank-holidays.json")
data = response.json()

# Pick out list of Northern Ireland holidays
ni = data["northern-ireland"]
events = ni["events"]

# Print every Northern Ireland Bank Holiday
print("All Northern Ireland bank holiday:")
for event in events:
     print(event["title"], event["date"])

# Collect titles of holidays from England/Wales and Scotland
other_titles = set()
for event in data["england-and-wales"]["events"]:
    other_titles.add(event["title"])

for event in data["scotland"]["events"]:
    other_titles.add(event["title"])

# Print holidays that are unique to Northern Ireland
print()
print("Bank Holidays unique to Northern Ireland:")
for event in events:
    if event["title"] not in other_titles:
            print(event["title"], event["date"])

    