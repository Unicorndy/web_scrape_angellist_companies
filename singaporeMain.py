#main program

from config import db_sg
from clean import clean
from scrape import scrape,results

singapore = "https://angel.co/companies?locations[]=1682-Singapore"
singapore2 = "https://angel.co/companies?locations[]=413928-Singapore,+Singapore"


if __name__ == "__main__":

    urls = [#singapore,
            singapore2
           ]
    for url in urls:
        html = scrape(url,11)  #use 20 click for singapore url and 11 click for singapore2 url
        data = results(html)
        for result in data:
            company = clean(result)
            #print(company['location'])
            if db_sg.companies.find({"name":company['name']}).count() > 0:
                # to prevent duplicates of company
                pass
            elif company['location'] == 'Singapore':
                db_sg.companies.insert_one(company)
        print('Added companies from different url')