#main program

from config import db
from clean import clean
from scrape import scrape,results

#scraping from all possible type
url = "https://angel.co/companies"
startup = "https://angel.co/companies?company_types[]=Startup"
vcfirm = "https://angel.co/companies?company_types[]=VC+Firm"
privatecompany ="https://angel.co/companies?company_types[]=Private+Company"
saas ="https://angel.co/companies?company_types[]=SaaS"
incubator ="https://angel.co/companies?company_types[]=Incubator"
mobileapp ="https://angel.co/companies?company_types[]=Mobile+App"
singapore = "https://angel.co/companies?locations[]=1682-Singapore"
ecommerce ="https://angel.co/companies?markets[]=E-Commerce"
education = "https://angel.co/companies?markets[]=Education"
games = "https://angel.co/companies?markets[]=Games"
healthcare = "https://angel.co/companies?markets[]=Healthcare"
mobile ="https://angel.co/companies?markets[]=Mobile"
datamining = "https://angel.co/companies?markets[]=Data+Mining"
seed = "https://angel.co/companies?stage=Seed"
seriesa = "https://angel.co/companies?stage[]=Series+A"
seriesb = "https://angel.co/companies?stage=Series+B"
seriesc = "https://angel.co/companies?stage=Series+C"
acquired = "https://angel.co/companies?stage[]=Acquired"



if __name__ == "__main__":

    urls = [#url,
            #startup,
            #vcfirm,
            privatecompany,
            saas,
            incubator,
            mobileapp,
            singapore,
            ecommerce,
            education,
            games,
            healthcare,
            mobile,
            datamining,
            seed,
            seriesa,
            seriesb,
            seriesc,
            acquired]
    for url in urls:
        html = scrape(url,20) #scrape from top 5 pages of the search type
        data = results(html)
        for result in data:
            company = clean(result)
            if db.companies.find({"name":company['name']}).count() > 0:
                # to prevent duplicates of company
                pass
            else:
                db.companies.insert_one(company)
        print('Added companies from different url')