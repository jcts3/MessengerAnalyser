from bs4 import BeautifulSoup 

import pandas as pd
import datetime

print('starting soup')
with open("messages/jamesstratford_koy9e4bcga.1/message.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')
print('soup made')

columns = ['Date', 'Time', 'Person', 'Message']

def createPandaDF():
    print('creating pandas')
    messages = soup.body.find_all("div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")
    print(len(messages))
    # print(messages[1:100])
    df = pd.DataFrame(columns=columns)
    for message in messages:
        # print(message)
        dateTid = message.find("div", class_="_3-94 _2lem").get_text().split(' ')
        date = convertDate(dateTid)
        msg = message.find("div", class_="_3-96 _2let")
        person = message.find("div", class_="_3-96 _2pio _2lek _2lel").get_text()
        try :
            text = msg.get_text()
        except:
            print('no text')
            text = '***NO TEXT***'
        obj = {date, dateTid[3], person, text}
        # df.append(obj)
        print('done')
        
def convertDate(dateTid):
    datum = dateTid[0]
    monad = datetime.datetime.strptime(dateTid[1], '%b').month
    ar = dateTid[2][2:4]
    dateText = ('%s/%s/%s' %(monad, datum, ar))
    date = datetime.datetime.strptime(dateText, '%x').date()
    return date

createPandaDF()

# for message in messages


# convert 19 Dec 2018, 10:07 to date time format