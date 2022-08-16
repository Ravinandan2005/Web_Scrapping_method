'''WEBSCRAPPING TASK FROM BEGINNING OF THE SITE - https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=QQ6SN8TKTCPBNF2VEH1K&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2
Needed Details RANK MOVIENAME YEAR RATINGS GROSS AMOUNT DIRECTOR NAMES SHORTNOTE of all 50Movies'''
from bs4 import BeautifulSoup
import requests,re
import pandas as pd

try:
    get_url = requests.get("https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=S3BEWA5KCB5E2NCF5CXX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2") #Used to get data
    html_parser = BeautifulSoup(get_url.text,'html.parser')
    movies = html_parser.find("div",class_ = "lister-list").find_all("div",class_='lister-item')
    movie_lst = {"Rank" : [],"Movie Name":[],"Year":[],"Ratings": []}
    for movie in movies:
        index = movie.find('h3').find("span",class_="lister-item-index").get_text(strip=True).split('.')[0]
        movie_name = movie.find('h3').a.text
        year = movie.find('h3').find("span",class_="lister-item-year").text
        year = re.sub("\D","",year)
        rate = movie.find("div",class_="ratings-imdb-rating").strong.text
        story = movie.find("p").findNext("p").get_text(strip=True)
        director = movie.find("p").findNext("p").findNext("p").a.text
        movie_gross_price = movie.find("p",class_="sort-num_votes-visible").find_all("span")[-1].get_text()
        movie_lst["Rank"].append(index)
        movie_lst["Movie Name"].append(movie_name)
        movie_lst["Year"].append(year)
        movie_lst["Ratings"].append(rate)


except Exception as err:
    print('Technno Mindz Says Your Code as Error \n>>>',err)

Data_Frame = pd.DataFrame(data = movie_lst)
print(Data_Frame.head())
