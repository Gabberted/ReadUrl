# We will read a stream and convert it into a stream
# then we will print it
# and do some stats

#import
import os
import urllib3
import certifi
import argparse



#var declarations
strVersion = "0.0.8"


#main
def echoHTML(strUrl):
    url = strUrl
    mystr=""
    try:    
        os.system('clear')
        print("Start System version: " + strVersion)
        print("init ReadStream")

        http = urllib3.PoolManager(ca_certs=certifi.where())
        print(f"HTTP pool created: {http}")
        payload = {'scheme':'https', 'auth':'None','name': 'Peter', 'age': 23}
        #payload = {}
        print(f"Payload created {payload}")    
        print(f"Requering {url}")
        try:
            #req = http.request('GET', url, fields=payload)
            req = http.request('GET', url)
            print(f"Get request {req}")
            print(req.data.decode('utf-8'))
            mystr = req.data.decode("utf8")
        except Exception as ex:
            print(f"Error QUERING URL: {ex}")
            pass       
    except Exception as ex:
        print(f"Error {ex}")
        pass
    return mystr

def webOpen(url):
    http = urllib3.PoolManager()
    url = 'http://webcode.me'
    resp = http.request('GET', url)
    print(resp.status)

def main():
    boVerbose=False
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    #parser.add_argument("-?", help="get the HTML content of the url provided: readUrl -url (url)")
    parser.add_argument("-url"			, "--url"				      , help="Reads the content of the url provided. Use as e.g. 'readUrl -url http://www.yahoo.com'")
    parser.add_argument("-b"			, "--beautyfy"			      , help="Uses beautifull-soup to clear up the HTML")
    parser.add_argument("-words"		, "--get_all_seperate_words"  , help="Gets all the words of the page without HTML tags")
    parser.add_argument("-wordUnique"	, "--get_all_Unique_words"	  , help="Gets all the unique words of the page without HTML tags")
    parser.add_argument("-test      "	, "--test"	  , help="Run test")
    args = parser.parse_args()
    url="HTTPS://" + str(args.url)
    if("HTTP" in str(args.url)):
        url=args.url
    else:
        url="HTTPS://" + str(args.url)
    if args.test:
        webOpen("www.nu.nl")        
    if args.verbosity:
        print("verbosity turned on")
        boVerbose=True
    if args.url:
        url=""
       
        return echoHTML(str(url))
    if args.beautyfy:
        print("Not implemented yet")
    if args.get_all_seperate_words:
        print("Not implemented yet")

    if args.get_all_Unique_words:
        print("Not fully implemented yet")
        strHTML= echoHTML(str(url))
        strHTMLSPL=strHTML.split(' ')
        for strItem in strHTMLSPL:
            print(strItem)

    print("Done")


main()
