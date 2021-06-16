import requests, webbrowser

response = requests.get('https://dog.ceo/api/breeds/image/random')
dict = response.json()

webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(dict['message'])
