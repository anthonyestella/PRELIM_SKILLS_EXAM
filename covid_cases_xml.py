import xml.etree.cElementTree as et

tree = et.parse("covid_cases_xml.xml")

root = tree.getroot()
#e date reported, countries and territories, number of cases, and deaths
#header = ['dateRep', 'countryountriesAndTerritories','cases', 'deaths']
dateRep = []
countriesAndTerritories = []
cases = []
deaths = []

for title in root.iter('Date Reported'):
    dateRep.append(title.text)

for title in root.iter('Countries and Territories'):
    countriesAndTerritories.append(title.text)

for title in root.iter('Cases'):
    cases.append(title.text)

for title in root.iter('Deaths'):
    deaths.append(title.text)

print(dateRep)
print(countriesAndTerritories)
print(cases)
print(deaths)



