import requests
import json
headers={"User-Agent" : "test/0.0"}
s = requests.Session()
s.headers.update({"User-Agent" : "test/0.0"})

#gets the revision history and sorces count
params = {"action" : "query", "format" : "json" , "formatversion" : 2, "meta" : "siteinfo", 
          "generator" : "random" , "grnnamespace" : 0, 
          "prop" : "revisions|extracts|contributors","ellimit" : "max","rvlimit" : 1, "explaintext" :1}

outp = s.get("https://en.wikipedia.org/w/api.php",params=params).json()
print("article " + outp["query"]["pages"][0]["title"])
print("date of last revision " + (str)((outp["query"]["pages"][0]["revisions"][0]["timestamp"])))
print("number of contributors " + (str)(len(outp["query"]["pages"][0]["contributors"])))
print("number of charactors in the text " + (str)(len(outp["query"]["pages"][0]["extract"])))