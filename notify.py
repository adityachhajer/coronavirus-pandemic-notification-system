from plyer import notification
import requests
from bs4 import BeautifulSoup
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C://Users//Admin//Desktop//Project//ml//download.ico",
        timeout=10
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    notifyMe("Aditya","Details about this virus")
    myHtmlData=getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    myData=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myData+=tr.get_text()
    myData=myData[1:]

    states=['Rajasthan']

    itemlist= myData.split("\n\n")
    for item in itemlist[0:30]:
        datalist = item.split('\n')
        if datalist[1] in states:
            title='cases of covid-19'
            text=f"{datalist[0]} Indian:{datalist[1]} \nForeign:{datalist[2]} \ncured:{datalist[3]} \nDeaths:{datalist[4]}"
            notifyMe(title,text)

