import urllib.request as req
import bs4

def main( x ):
    #網址
    url = "http://big5.quanben5.com/n/miaojianggushi/" + str( x ) + ".html"
    request = req.Request( url, headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        })
    with req.urlopen( request ) as response:
        data = response.read().decode( "utf-8" )
        #data為網頁原始碼
    
    #解析原始碼
    root = bs4.BeautifulSoup( data, "html.parser" )
    title = root.find( "h1", class_="title1" )
    
    contents = root.find_all( "p" )
    f = open( "小說.txt", "a", encoding = "utf-8" )
    f.write( title.text )
    
    for i in range( 2 ):
        f.write( "\n" )
        
    for content in contents[ 0: -4 ]:
        f.write( content.text )
        for i in range( 2 ):
            f.write( "\n" )
    f.close()
    
for i in range( 19887, 19888 ):
    main( i )
    
print( "完成" )