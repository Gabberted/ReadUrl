# We will read a stream and convert it into a stream
# then we will print it
# and do some stats

#import
import os
import urllib3
import certifi
import argparse



#var declarations
strVersion = "0.0.2"


#main
def echoHTML(strUrl):
    os.system('clear')
    print("Start System version: " + strVersion)
    print("init ReadStream")

    #fp = urllib.request.urlopen("http://www.python.org")
    #fp = urllib.request.urlopen(strUrl)
    #mybytes = fp.read()
    http = urllib3.PoolManager(ca_certs=certifi.where())
    payload = {'name': 'Peter', 'age': 23}
    url = strUrl
    req = http.request('GET', url, fields=payload)
    print(req.data.decode('utf-8'))
    mystr = req.data.decode("utf8")
    #fp.close()
    #print(mystr)
    return mystr


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    #parser.add_argument("-?", help="get the HTML content of the url provided: readUrl -url (url)")
    parser.add_argument("-url"			, "--url"				      , help="Reads the content of the url provided. Use as e.g. 'readUrl -url http://www.yahoo.com'")
    parser.add_argument("-b"			, "--beautyfy"			      , help="Uses beautifull-soup to clear up the HTML")
    parser.add_argument("-words"		, "--get_all_seperate_words"  , help="Gets all the words of the page without HTML tags")
    parser.add_argument("-wordUnique"	, "--get_all_Unique_words"	  , help="Gets all the unique words of the page without HTML tags")
    args = parser.parse_args()
    if args.verbosity:
        print("verbosity turned on")
    if args.url:
        url=""
        if("HTTP" in str(args.url)):
            url=args.url
        else:
            url="HTTPS://" + str(args.url)

        return echoHTML(str(url))
    if args.beautyfy:
        print("Not implemented yet")
    if args.get_all_seperate_words:
        print("Not implemented yet")

    if args.get_all_Unique_words:
        print("Not implemented yet")

    print("Done")


main()
