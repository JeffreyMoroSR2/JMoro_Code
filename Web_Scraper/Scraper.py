import requests, bs4, datetime

class Scraper:
    def __init__(self, site):
        self.site = site

    def getSite(self):
        s = requests.get(self.site)
        b = bs4.BeautifulSoup(s.text, "html.parser")
        p1 = b.select('.temperature .p1')
        weather = p1[0].getText()
        p2 = b.select('.temperature .p2')
        weather0 = p2[0].getText()
        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()
        p7 = b.select('.temperature .p7')
        weather5 = p7[0].getText()
        p8 = b.select('.temperature .p8')
        weather6 = p8[0].getText()


        self.weather = weather
        self.weather0 = weather0
        self.weather1 = weather1
        self.weather2 = weather2
        self.weather3 = weather3
        self.weather4 = weather4
        self.weather5 = weather5
        self.weather6 = weather6

    def printInfo(self):
        self.getSite()
        print("Today is", datetime.datetime.today().strftime('%Y-%m-%d'))
        print('Night: ' + self.weather + ' ' +  self.weather0)
        print('Morning: ' + self.weather1 + ' ' + self.weather2)
        print('Day: ' + self.weather3 + ' ' + self.weather4)
        print('Evening: ' + self.weather5 + ' ' + self.weather6)




scraper = Scraper("https://ua.sinoptik.ua/")
scraper.printInfo()
input()

