# We will read a stream and convert it into a stream
# then we will print it
# and do some stats

#import
import os
import urllib3
import certifi
import argparse
import json
import pymssql


#var declarations
strVersion = "1.0.0"
strHTMLTags=['\n','<br>','<p>','"','<a','</div>','<strong>','=','text/css','/>']
strHTMLTags+=['href','<span>','</span>','<div','classlimit','</div','<strong','</input>','</i>','<i>']

#db
def Connect():
    try:
        #dbg.setDebugLevel(0)
        print("Entering Connect")
        print("Trying to connect")
        #connection = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-SFABI2H\SQLEXPRESS1;Database=SLIMS;Trusted_Connection=yes;')
        #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:DESKTOP-SFABI2H\SQLEXPRESS1;Database=SLIMS;UID=SLIMS_APPUSR;PWD=xTzz488slims')
        #try:
        #    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:192.168.178.42\SQLEXPRESS1;Database=SLIMS;UID=SLIMS_APPUSR;PWD=xTzz488slims')
        #except Exception as e:
        #    dbg.debugprint(str(e))
        #  db = pymysql.connect("mysql8.mijnhostingpartner.nl","Autar3Joomla","asdf1234","Autar3newj" )

        #conn = pymssql.connect(host='84.246.4.143:9139', user='Autar3external', password='ijQ84mTO@85400', database='autar3filelog')
        #dbg.setDebugLevel(0)
        #conn = pymssql.connect(host='185.41.125.20', user='Autar3external', password='ijQ84mTO@85400', database='autar3filelog', port=9108)
        #conn = pymssql.connect(host='192.168.2.1/slims', user='SLIMS_APPUSR', password='xTzz488slims', database='slims', port=1433)
        #conn = mysql.connector.connect(host="127.0.0.1",user="root",password="ijQ84mTO@85400", port=3306)
        #conn = pymssql.connect(host='127.0.0.1', user='slims', password='ijQ84mTO@85400', database='slims', port=3306)
        #conn = mysql.connector.connect(host="database-2.chsg3bafu3rp.us-east-2.rds.amazonaws.com",user="admin",password="ijQ84mTO#85400", port=3306)
        #conn = mysql.connector.connect(host="sql211.unaux.com",user="unaux_27270618",password="#59ceFij4VkyaaE6hKO$", database="unaux_27270618_slims", port=3306)
        #conn = mysql.connector.connect(host="192.168.178.62",user="root",password="ijQ84mTO", database="unaux_27270618_slims", port=3306)

        #conn = mysql.connector.connect(host="gabberted.unaux.com",user="unaux_27270618",password="#59ceFij4VkyaaE6hKO$", database="unaux_27270618_slims", port=3306)
        #conn = mysql.connector.connect(host='185.41.126.25', user='50747_rakaut', password='t\H7mF|i:7', database='50747_BackSystem', port=9146)
        #conn = mysql.connector.connect(host='localhost', user='slims', password='ijQ84mTO@85400', database='slims', port=3306)
        #conn.autocommit(True)
        #conn = mysql.connector.connect(host='localhost',database='slims',user='slims',password='ijQ84mTO@85400')
        #conn = sqlite3.connect('data/mydb')
        #conn== sqlite3.connect(db)

        #conn = pymssql.connect(host='192.168.2.1\slims', user='SLIMS_APPUSR', password='xTzz488slims', database='deflopment', port=1433)
        #conn = pymssql.connect(host='192.168.2.1\slims', user='SLIMS_APPUSR', password='xTzz488slims', database='def', port=1433)
        #conn = pymssql.connect(host='192.168.2.1\slims', user='SLIMS_APPUSR', password='xTzz488slims', database='SLIMS', port=1433)
        #conn = pymssql.connect(host='185.41.126.25', user='50747_rakaut', password='t\H7mF|i:7', database='50747_BackSystem', port=9146)
        conn = pymssql.connect(host='192.168.10.102', user='Autar3External', password='ijQ84mTO@85400', database='Autar3main', port=9146)
        print("connection made: Connected")
        cursor=conn.cursor()
        print("db cursor: fetched " + str(cursor))
        #dbg.setDebugLevel(0)

    # except mysql.connector.Error as err:
    #     print("Something went wrong: {}".format(err))
    # except pymssql.InternalError as error:
    #     print("Error:" + str(error.args))
    #     code, message = error.args
    #     print(">>>>>>>>>>>>>", code, message)
    except Exception as e:
        print("Connection failed!")
        print(e)
        print("Leaving")
    #dbg.setDebugLevel(0)
    return cursor, conn

#main
def echoHTML(strUrl):
    url = strUrl
    mystr=""
    try:    
        os.system('clear')
        print("Start System version: " + strVersion)
        print("init ReadStream")

        #http = urllib3.PoolManager(ca_certs=certifi.where())
        http = urllib3.PoolManager()
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

def webOpen(url=""):
    http = urllib3.PoolManager()
    if url=="":
        url = 'http://webcode.me'
    resp = http.request('GET', url)
    print(resp.data.decode('utf-8'))
    return resp.data.decode('utf-8')

def removeHTMLTags(strHTML):
    for strTag in strHTMLTags:
        strHTML=strHTML.replace(strTag,"")
    return strHTML

def storeHTMLTags(strHTMLTags):
    cursor, conn = Connect()
    print(f"Storing Tag: {strHTMLTags}")
    for strHTMLTag in strHTMLTags.split(","):
        print(f"Tag: {strHTMLTag}")
        strQ="insert into HTML_Tags(Tag)values('" + strHTMLTag + "')"
        cursor.execute(strQ)
    
    cursor.close()
    conn.close()

        
def get_all_seperate_words(url):    
    strHTML= echoHTML(str(url))    
    strHTML=removeHTMLTags(strHTML)
    print(f"strHtml: {strHTML}")
    strHTMLsplit=strHTML.split()
    iLen=len(strHTMLsplit)

    print(f"The lenght of strHTMLsplit: {iLen}")
    for strItem in strHTMLsplit:
        print(f"item: {strItem}")
    
    return json.dumps(strHTMLsplit)

    #return str(strHTMLsplit)


def runserver():
    return "Not implemented yet!"

def collectHTMLTags(url):
    lstTags=[]
    strHTML= echoHTML(str(url))  
    for strItem in strHTML.split("<"):
        for strHTMLTag in strItem.split(">"):
            if(len(strHTMLTag.strip())>0):    
                strHTMLTag = "<" + strHTMLTag  + ">"                            
                if strHTMLTag not in lstTags:
                    lstTags.append(strHTMLTag)
                    #print(f"tag: {strHTMLTag}")

    return json.dumps(lstTags)

  
def main():
    boVerbose=False
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    #parser.add_argument("-?", help="get the HTML content of the url provided: readUrl -url (url)")
    parser.add_argument("-url"			, "--url"				      , help="Reads the content of the url provided. Use as e.g. 'readUrl -url http://www.yahoo.com'")
    parser.add_argument("-b"			, "--beautyfy"			      , help="Uses beautifull-soup to clear up the HTML")
    parser.add_argument("-words"		, "--get_all_seperate_words"  , help="Gets all the words of the page without HTML tags")
    parser.add_argument("-wordUnique"	, "--get_all_Unique_words"	  , help="Gets all the unique words of the page without HTML tags")
    parser.add_argument("--runserver"	, help="Run the server on host port 4452")
    parser.add_argument("-test      "	, "--test"	  , help="Run test")
    parser.add_argument("-collectHTMLTags "	, "--collectHTMLTags"	  , help="Collect all HTML tags in the url")
    args = parser.parse_args()
    url="HTTPS://" + str(args.url)
    if("HTTP" in str(args.url)):
        url=args.url
    else:
        url="HTTPS://" + str(args.url)
    if args.collectHTMLTags:
        collectHTMLTags()
    if args.runserver:
        runserver()        
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
        strHTML= get_all_seperate_words(url)
       

    if args.get_all_Unique_words:
        print("Not fully implemented yet")
        strHTML= echoHTML(str(url))
        strHTMLSPL=strHTML.split(' ')
        for strItem in strHTMLSPL:
            print(strItem)

    print("Done")


main()
