import requests

S = requests.Session()

URL = "https://pt.wikipedia.org/w/api.php"

PARAMS = {
    'action': "query",
    'list': "categorymembers",
    'cmtitle': "Categoria:Grupos_de_rap_do_Brasil",
    'cmlimit': 500,
    'format': "json"
}

R = S.get(url=URL, params=PARAMS)
# DATA = R.json()

print(R.text)