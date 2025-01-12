"""
Akhbar padh kr sunno, From the newapi.org We are getting the frest top news and then using the pywin32 are makint the python to speack it
"""

import json
import requests
from win32com.client import Dispatch
from dotenv import load_dotenv
from os import environ

load_dotenv()

apikey = environ["key"]
URL = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey={0}".format(apikey)


def speak(str):
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)


def news_api(url=URL):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['articles']


if __name__ == "__main__":
    top_ten = news_api()    

    for number, articles in enumarate(top_ten):
        speak("Moving towards "+ "a " if number== 0 else "another " + "fresh news")
        print(f"Title: {articles['title']}. \nDiscription: {articles['description']}. \
         Actually: {articles['content']}\nFor more info... Go to ==>>> {articles['url']}\n")
        speak(f"Title; {articles['title']}. \nDiscription; {articles['description']}. \
        Actually; {articles['content']}\n")
        
    speak("Thank you for listening")

