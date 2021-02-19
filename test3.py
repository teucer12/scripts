import requests

r=requests.get("http://192.168.86.140/")
r2 = r.text

print(r2[r2.find("<title>") + 7: r2.find("</title>")])