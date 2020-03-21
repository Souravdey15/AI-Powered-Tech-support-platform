from twilio.rest import Client
import requests
from bs4 import BeautifulSoup, Tag

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'ACb23ca05abc9d2c3ad77b976ebcdeb037'
auth_token = 'd49fd44cbdca5332607775e5f61eead9'
#client = Client(account_sid, auth_token)

#Everything can be found if you properly read the documentation

response =requests.get("https://api.twilio.com/2010-04-01/Accounts/AC4af74c20f6e5f5aee9b1e7563ae727c9/Recordings",auth=(account_sid, auth_token))       #v1/Recordings        #client.video.v1.Recordings
xmls = BeautifulSoup(response.content,features="lxml")

rid_list = []


for tags in xmls.find_all("sid"):
    rid_list.append(tags.string)

for rids in rid_list:
    response = requests.get("https://api.twilio.com/2010-04-01/Accounts/{0}/Recordings/{1}".format(account_sid,rids))
    fileName= rids+".wav"
    try:
        with open(fileName, mode='bx') as f:
            f.write(response.content)
    except:
        print(rids+".wav already created")
        pass


