import requests

r=requests.get("http://example.com/")
r2 = r.text

print(r2[r2.find("<title>") + 7: r2.find("</title>")])
