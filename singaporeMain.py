#main program

from configSingapore import db
from clean import clean
from scrape import scrape,results

singapore = "https://angel.co/companies?locations[]=1682-Singapore"
singapore2 = "https://angel.co/companies?locations[]=413928-Singapore,+Singapore"


if __name__ == "__main__":

    urls = [singapore,
            #singapore2
           ]
    for url in urls:
        html = scrape(url,20)
        data = results(html)
        for result in data:
            company = clean(result)
            #print(company['location'])
            if db.companies.find({"name":company['name']}).count() > 0:
                # to prevent duplicates of company
                pass
            elif company['location'] == 'Singapore':
                db.companies.insert_one(company)
        print('Added companies from different url')