import requests
'''
# Do the following (include imports)
r = requests.get('https://www.google.com/search?q=when%20was%20trump%20born', headers=headers)
soup = BeautifulSoup(r.text, 'lxml')\nresult = soup.find('div', class_='_XWk')\nprint(result.text)
'''

from duckduckgo_search import DDGS
        
def quick_answer(query = "what is the sun"):
    with DDGS() as ddgs:
        res = ddgs.text(query)
        l = []
        for r in res:
            return r["body"]
            print(r)
            l.append(r)
        if len(l)>0 and "text" in l[0] and l[0]["text"] != "":
            return l[0]["text"]
        
def quick_answer_x(query = ""):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get("https://api.duckduckgo.com",
        params = {
            "q": query,
            "format": "json"
        })#,headers=headers)

    data = r.json()

    print(data)

    print(data["Abstract"])
    return data["Abstract"]
    
    
    
#print(quick_answer())

#for a in range(10):
#print(quick_answer("what is a dog?"))