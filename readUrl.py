# We will read a stream and convert it into a stream
# then we will print it
# and do some stats

#import
import os
import urllib.request
import argparse



#var declarations
strVersion = "0.0.2"


#main
def echoHTML(strUrl):
    os.system('clear')
    print("Start System version: " + strVersion)
    print("init ReadStream")

    #fp = urllib.request.urlopen("http://www.python.org")
    fp = urllib.request.urlopen(strUrl)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    #print(mystr)
    return mystr


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    #parser.add_argument("-?", help="get the HTML content of the url provided: readUrl -url (url)")
    parser.add_argument("-url"			, "--url"				, help="Reads the content of the url provided. Use as e.g. 'readUrl -url http://www.yahoo.com'")
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

    print("Done")


main()
