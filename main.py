import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv


driver = webdriver.Chrome(executable_path='/Users/christoslianos/Downloads/WebScrapper/chromedriver')
driver.maximize_window()
driver.get("https://www.nba.com/stats/players/traditional/?SeasonType=Playoffs&sort=PTS&dir=-1")

time.sleep(5)
content = driver.page_source.encode('utf-8')
soup = BeautifulSoup(content, 'html.parser')
player = soup.find_all('td', class_="player")
average_points = soup.find_all('td', class_="sorted")
points = []
players = []
for name in player:
    text = name.get_text()
    players.append(text)

for point in average_points:
    number = point.get_text()
    points.append(number)

new_list = []
for i in range(0, len(points)):
    new_list.append(players[i])
    new_list.append(points[i])
    with open ('stats.csv', newline="", mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(new_list)

#print(new_list)

