import json
import yaml
import csv

#example of json
#e date reported, countries and territories, number of cases, and deaths

header = ['dateRep', 'countryountriesAndTerritories','cases', 'deaths']
data = ['04/10/2021', 'Austria', 1532, 5]
f = open('/home/devasc/labs/devnet-src/python/Prelim Skills Exam/covid_cases.json', 'w')
#writer = csv.writer(f)
#writer.writerow()

#x = '{ "name": "John", "age": "30", "city": "New York City"}'
#parse json
y=json.loads(data)

print("The output of json file is ", y)
print("Data", y["Data"])