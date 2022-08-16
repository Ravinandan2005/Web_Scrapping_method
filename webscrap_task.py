'''WEBSCRAPPING TASK FROM BEGINNING OF THE SITE - https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=QQ6SN8TKTCPBNF2VEH1K&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2
Needed Details RANK MOVIENAME YEAR RATINGS GROSS AMOUNT DIRECTOR NAMES SHORTNOTE of all 50Movies'''
#Step 1 Importing all necessary modules
from bs4 import BeautifulSoup
import requests, openpyxl
import re
#Step 13 using openpyxl module creating a workbook
excel = openpyxl.Workbook()
sheet = excel.active #Step 14 making a sheet as a active sheet
sheet.title = 'TM Movies' #Step 15 Assigning a Title
#Step 16 Appending Title to the excel sheet
sheet.append(['Rank','Movie Name','Released Year','IMDB Ratings','Story','Director','Gross Amount'])

try:
    #Step 2 using requests module we can able to connect to the webpage after connecting we are getting all info about the page and assigning to a variable
    get_url = requests.get("https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=S3BEWA5KCB5E2NCF5CXX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2") #Used to get data
    #Step 3 we are now getting all the html of the page using Bs4 BeaultifulSoup by the usage of html.parser
    html_parser = BeautifulSoup(get_url.text,'html.parser')
    #Step 4 Finding the main class then finding all the div class under the subclass name
    movies = html_parser.find("div",class_ = "lister-list").find_all("div",class_='lister-item')
    for movie in movies:
#Step 5 Finding Index - It is located in the h3 tag in that under span tag in the class name of lister-item-index 
#Then we nee to get text with the strip as true and we don't need the '.' so we can remove by split and finding index as 0
        index = movie.find('h3').find("span",class_="lister-item-index").get_text(strip=True).split('.')[0]
#Step 6 we are finding the movie name in h3 tag under that it is located in the anchor tage so we can directly use .a.text
        movie_name = movie.find('h3').a.text
#Step 7 now we are finding year as same as we have done before
        year = movie.find('h3').find("span",class_="lister-item-year").text
#Step 8 usage of regularexpressrion to replace a word in the format of ("what to keep","what to replace","from where")
        year = re.sub("\D","",year)
        rate = movie.find("div",class_="ratings-imdb-rating").strong.text #step 9 finding the ratings
#step 10 finding the story which is present in the para tag inside a paratage so we use .findNext("p") to find the next para tag
        story = movie.find("p").findNext("p").get_text(strip=True)
#Step 11 Finding the director name present in the anchor tag in the second sub para tag in para tag        
        director = movie.find("p").findNext("p").findNext("p").a.text
#Step 12 finding the gross presen in the para tag under the class sor-num_votes-visible1 in the last span tag
#So we use find_all span tag under the para tag so that we can use -1 to fetch the last para tag
        movie_gross_price = movie.find("p",class_="sort-num_votes-visible").find_all("span")[-1].get_text()
        # print(index,movie_name,year,rate,story,director,movie_gross_price)
        sheet.append([index,movie_name,year,rate,story,director,movie_gross_price])
except Exception as err:
    print('Technno Mindz Says Your Code as Error \n>>>',err)

excel.save('Action.xlsx')
