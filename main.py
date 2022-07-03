import requests
from bs4 import BeautifulSoup
from  dbConn import connect_db
from  functions import insertCases,sendMail
import time
while(1):
    # 執行1~3頁
    for page in range(1, 2): 
        # print("----------Page" + str(page)+"----------")
        # 將網頁資料GET下來
        r = requests.get("https://www.chickpt.com.tw/cases?page="+ str(page))
        # 將網頁資料以html.parser
        soup = BeautifulSoup(r.text, "html.parser")
        # 選取網頁中特定區塊
        result = soup.find_all('a',attrs={'class':'layout-width job-list-item is-flex flex-start flex-row flex-align-center is-tra'})
        # 迴圈輸出每個任務內容
        for r in result:
            id = r['href'].replace("https://www.chickpt.com.tw/job-","") # 輸出代號(網址尾端)
            content =  r.select_one("h2").text.replace(" ","").replace("\n","") # 輸出標題
            price =  r.select_one(".salary").text # 輸出價錢
            place = r.select_one(".place").text # 輸出價錢
            boss =  r.find("p", class_="mobile-job-company ellipsis-mobile-job-company ellipsis display-control show-mobile").text.replace(" ","").replace("\n","") # 輸出業主
            post_time =  r.find("span", class_="date-time is-flex flex-align-center").text.replace(" ","").replace("\n","")
            href = r['href'] # 輸出連結
            
            #print("\n工作代號:"+id+"\n工作內容:"+content+"\n工作價錢:"+price+"\n任務地點:"+place+"\n刊登案主:"+boss+"\n發布時間:"+post_time+"\n工作連結:"+href)
            # 呼叫匯入資料庫funct
            subject = content
            mail_href = "https://chickpt.com.tw/dl?tp=4&um=1&ti="+id+"&e=share_job&sm=210386" #要用這種連結才能直接跳轉至APP
            mail_content = "\n工作內容: "+content+"\n工作價錢: "+price+"\n任務地點: "+place+"\n刊登案主: "+boss+"\n發布時間: "+post_time+"\n工作連結: "+mail_href
            try:
                insertCases(id, content, price, place, boss, href)
                sendMail(subject, mail_content)
            except:
                pass
    time.sleep(180)



