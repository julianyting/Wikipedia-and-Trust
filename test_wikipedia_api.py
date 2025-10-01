import requests
import json
headers={"User-Agent" : "test/0.0"}
s = requests.Session()
s.headers.update({"User-Agent" : "test/0.0"})

#gets the revision history and sorces count
params = {"action" : "query", "format" : "json" , "formatversion" : 2, "meta" : "siteinfo", 
          "generator" : "random" , "grnnamespace" : 0, 
          "prop" : "revisions|extlinks","ellimit" : "max","rvlimit" : "max"}

outp = s.get("https://en.wikipedia.org/w/api.php",params=params).json()
print("article " + (outp["query"]["pages"][0]["title"]))
print("amount of sources " + len(outp["query"]["pages"][0]["extlinks"]))
print("amount of revisions " + len(outp["query"]["pages"][0]["revisions"]))

