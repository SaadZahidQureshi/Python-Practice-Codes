import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/saadzahidqureshi/"

req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_pic = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_pic)