from bs4 import BeautifulSoup 

import pandas as pd
import datetime
import csv

columns = ['Index', 'Date', 'Time', 'Person', 'Message']

def main():
    soup = getSoup()
    csvF = createCSV(soup)
    df = createPandaDF(soup, csvF)

def getSoup():
    print('starting soup')
    #with open("../messages/jamesstratford_koy9e4bcga.1/message.html") as fp:
    with open ("../messages/johannaohlman_a8qbtcj2yq.1/message.html") as fp:
        soup = BeautifulSoup(fp, 'lxml')
    name = soup.title.string
    print(f'soup made for conversation with {name}')
    return soup

def createCSV(soup):
    name = soup.title.string
    directory = f'../csv/{name}.csv'
    csvfile = csv.writer(open(directory, 'w'))
    csvfile.writerow(columns)
    print(f'File to be written to {directory}.')
    return csvfile

def createPandaDF(soup, csvfile):
    print('creating pandas')
    messages = soup.body.find_all("div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")
    print(len(messages))
    df2 = pd.DataFrame(columns=columns)
    index=0
    dataList = []
    for message in messages:
        dateTid = message.find("div", class_="_3-94 _2lem").get_text().split(' ')
        date = convertDate(dateTid)
        msg = message.find("div", class_="_3-96 _2let")
        person = message.find("div", class_="_3-96 _2pio _2lek _2lel").get_text()
        try :
            text = msg.get_text()
        except:
            print('no text')
            text = '***NO TEXT***'
        obj = [index, date, dateTid[3], person, text]
        csvfile.writerow(obj)
        diction = {
            'Index': index,
            'Date': date,
            'Time': dateTid[3],
            'Person': person,
            'Message': text
        }
#        tempdf = pd.DataFrame([obj], columns=columns)
#        df = pd.concat(df, tempdf)
        index += 1
        dataList.append(diction)
    df2 = pd.DataFrame(dataList, columns=columns)
    return df2
        
def convertDate(dateTid):
    datum = int(dateTid[0])
    monad = int(datetime.datetime.strptime(dateTid[1], '%b').month)
    ar = int(dateTid[2][2:4])
    dateText = ('%i/%i/%i' %(monad, datum, ar))
    date = datetime.datetime.strptime(dateText, '%x').date()
    return date

#df2 = createPandaDF()
main()
print('properly done')
# for message in messages


# convert 19 Dec 2018, 10:07 to date time format