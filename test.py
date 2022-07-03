def isOdd(num):
    if(num%2 == 1):
        return True
    else:
        return False


if(isOdd(623)):
    print("is Odd")
else:
    print("is Even")

# import requests
# from bs4 import BeautifulSoup

# #將網頁資料GET下來
# r = requests.get("https://www.chickpt.com.tw/cases") 
# #將網頁資料以html.parser
# soup = BeautifulSoup(r.text,"html.parser")
#soup = soup.find_all('a',id='job-list')  #可以使用下標查詢
#print(soup.find_all('ul')[4].find_all('li'))
# print(soup.find('a',attrs={'class':'layout-width job-list-item is-flex flex-start flex-row flex-align-center is-tra'})) #更通用
# result = soup.find_all('a',attrs={'class':'layout-width job-list-item is-flex flex-start flex-row flex-align-center is-tra'}) #更通用
# for r in result:    
#     print("工作內容:" + r.select_one("h2").text.replace(" ","").replace("\n","")) # 輸出標題
#     print("工作價錢:" + r.select_one(".salary").text) # 輸出價錢
#     print("工作地點:" + r.select_one(".place").text) # 輸出價錢
#     print("工作連結:" + r['href']) # 輸出連結
#     print("\n")
    
# for r in result:   
#     content =  r.select_one("h2").text.replace(" ","").replace("\n","")# 輸出標題
#     price =  r.select_one(".salary").text# 輸出價錢
#     place = r.select_one(".place").text# 輸出價錢
#     boss =  r.find("p", class_="mobile-job-company ellipsis-mobile-job-company ellipsis display-control show-mobile").text.replace(" ","").replace("\n","")
#     post_time =  r.find("span", class_="date-time is-flex flex-align-center").text.replace(" ","").replace("\n","")
#     href = r['href']# 輸出連結
#     print("\n工作內容:"+content+"\n工作價錢:"+price+"\n任務地點:"+place+"\n刊登案主:"+boss+"\n發布時間:"+post_time+"\n工作連結:"+href)


# # # print(soup.find_all('ul'))
# # case = (soup.find_all('ul',id='job-list') )  #可以使用下標查詢
# # print(case)



# # 選取欲處理範圍(class="jobs-wrap"->a->h2) 
# sel = soup.select("div.jobs-wrap a h2") 
# article_title = []
# for s in sel:
#     item_href = s.text.replace(" ", "").replace("\n","")
#     article_title.append(item_href)
# print(article_title)

# # 選取欲處理範圍(class="jobs-wrap"->a)
# sel = soup.select("div.jobs-wrap a") 
# article_href = []
# for s in sel:
#     #print(s.text.replace(" ", ""))     
#     item_href = s["href"]
#     article_href.append(item_href)
# print(article_href)



#----- ver.1  輸出單頁------

# import requests
# from bs4 import BeautifulSoup
# #將網頁資料GET下來
# r = requests.get("https://www.chickpt.com.tw/cases") 
# #將網頁資料以html.parser
# soup = BeautifulSoup(r.text,"html.parser")
# # 選取網頁中特定區塊
# result = soup.find_all('a',attrs={'class':'layout-width job-list-item is-flex flex-start flex-row flex-align-center is-tra'})
# # 迴圈輸出每個任務內容
# for r in result:   
#     content =  r.select_one("h2").text.replace(" ","").replace("\n","") # 輸出標題
#     price =  r.select_one(".salary").text # 輸出價錢
#     place = r.select_one(".place").text # 輸出價錢
#     boss =  r.find("p", class_="mobile-job-company ellipsis-mobile-job-company ellipsis display-control show-mobile").text.replace(" ","").replace("\n","") # 輸出業主
#     post_time =  r.find("span", class_="date-time is-flex flex-align-center").text.replace(" ","").replace("\n","")
#     href = r['href'] # 輸出連結
#     print("\n工作內容:"+content+"\n工作價錢:"+price+"\n任務地點:"+place+"\n刊登案主:"+boss+"\n發布時間:"+post_time+"\n工作連結:"+href)

#----- ver.1  end------

#----- ver.2  輸出多頁------

# import requests
# from bs4 import BeautifulSoup
# # 執行1~3頁
# for page in range(1, 4): 
#     print("----------Page" + str(page)+"----------")
#     #將網頁資料GET下來
#     r = requests.get("https://www.chickpt.com.tw/cases?page="+ str(page))
#     #將網頁資料以html.parser
#     soup = BeautifulSoup(r.text, "html.parser")
#     # 選取網頁中特定區塊
#     result = soup.find_all('a',attrs={'class':'layout-width job-list-item is-flex flex-start flex-row flex-align-center is-tra'})
#     # 迴圈輸出每個任務內容
#     for r in result:   
#         content =  r.select_one("h2").text.replace(" ","").replace("\n","") # 輸出標題
#         price =  r.select_one(".salary").text # 輸出價錢
#         place = r.select_one(".place").text # 輸出價錢
#         boss =  r.find("p", class_="mobile-job-company ellipsis-mobile-job-company ellipsis display-control show-mobile").text.replace(" ","").replace("\n","") # 輸出業主
#         post_time =  r.find("span", class_="date-time is-flex flex-align-center").text.replace(" ","").replace("\n","")
#         href = r['href'] # 輸出連結
#         print("\n工作內容:"+content+"\n工作價錢:"+price+"\n任務地點:"+place+"\n刊登案主:"+boss+"\n發布時間:"+post_time+"\n工作連結:"+href)
    
#----- ver.2  end------



