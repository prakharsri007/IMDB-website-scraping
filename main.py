import requests
from bs4 import BeautifulSoup
import openpyxl #for creating an excel file to save all that data

exl=openpyxl.Workbook()
sheet=exl.active
sheet.title='Top rated IMDB movies'

sheet.append(['Rank','Title','Year of release','IMDB Rating'])




url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
try:
    source = requests.get(url)
    source.raise_for_status() #to capture an error if the url is wrong

    soup = BeautifulSoup(source.text,'html.parser')
    
    
    movies=soup.find('tbody', class_="lister-list").find_all('tr') 
    #always use underscore while accessing class
    for movie in movies:

        rank=movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0] 
        #removes all spaces and newlines(get_text(strip=True) ) (.split('.')[0])= this is used for removing the dot from all ranks

        name=movie.find('td', class_="titleColumn").a.text
        #just get the text of the sub tag 'a'

        year=movie.find('td', class_="titleColumn").span.text.strip('()')
        #the strip is used to remove the any thing like in this case the brackets from the year

        rating=movie.find('td', class_="ratingColumn imdbRating").strong.text



        
        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating]) #adds all the data in the excel sheet
       
        

except Exception as e:
    print(e)

exl.save('Top 250 IMDB movies.xlsx')   
