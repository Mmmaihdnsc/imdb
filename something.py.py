import requests
from bs4 import BeautifulSoup
url='https://www.imdb.com/chart/top/?ref_=chttvtp_nv_menu'
con=requests.get(url,headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
                 
)

soup=BeautifulSoup(con.text,'html.parser')
movie=soup.find('main',class_='ipc-page-wrapper ipc-page-wrapper--baseAlt')
movies1=movie.find_all('h3')
for i in movies1:
    print(i.text,'\n','\t')
input('\t\t enter to exit')
