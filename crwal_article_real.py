import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from dbconnect_article import insertBLOB

driver = webdriver.Chrome()  # Chrome으로 selenium 사용
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")  # 호출 URL
elem = driver.find_element(By.NAME, "q")  # 구글 검색창 name인 q를 지정.
elem.send_keys("카리나")  # 검색어
elem.send_keys(Keys.RETURN)  # enter 의미


# last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이
# while True: # 더이상 표시할 이미지가 없을때까지 스크롤 내림
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1) # 스크롤을 내리고 로딩되는 시간 설정 1초
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element(By.CSS_SELECTOR, ".mye4qd").click() # 구글 이미지의 결과 더보기 클릭
#         except:
#             break
#     last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")  # 리스트 사진의 class 를 선택하여 이미지를 선택
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)  # 이미지 클릭후 2초동안 딜레이
        # 이미지 가져오기 (중복된 class 명이 있어 풀패스경로로 설정)
        imgUrl = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")

        # 기사 제목 가져오기 (중복된 class 명이 있어 풀패스경로로 설정)
        # subTitle = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("alt")

        # 봇 접근으로 인식하여 차단될 경우 브라우저로 페이크 설정
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        #result = imgUrl.find('화보')

        save_name = "카리나{}.png".format(count)
        out_path = "D:/Pinterest/media/카리나/"
        dirname = os.path.dirname(out_path)
        if dirname:
            if not os.path.exists(dirname):
                try:
                    os.makedirs(dirname)
                except Exception as e:
                    print("# Cannot create directory '{}'".format(dirname))
                    print("# Error Details.. '{}'".format(str(e)))

        #if result != -1: # 제목에 화보가 들어갈 경우 이미지 다운로드
        urllib.request.urlretrieve(imgUrl, out_path+str(save_name))

        #mem = urllib.request.urlopen(imgUrl).read()

        #with open(savename, mode="wb") as f:
        #    f.write(mem)
        #    print("다운로드")
        count = count + 1
        file_path = "카리나/{}".format(save_name)
        file_name = "카리나{}".format(count)

        #insert_data = '"아스날/{}", "아스날1", "아스날 사진", "2023-01-05", 1, 1"'.format(savename)
        #insertBLOB(insert_data)
        insertBLOB(file_path, file_name, "카리나 사진", "2023-01-05", 1, 2)
        #insertBLOB("아스날/아스날3.png", "아스날3", "아스날 사진", "2023-01-05", 1, 1)
        #insertBLOB("아스날/아스날4.png", "아스날4", "아스날 사진", "2023-01-05", 1, 1)
        #insertBLOB("아스날/아스날5.png", "아스날5", "아스날 사진", "2023-01-05", 1, 1)




        # 화보가 들어간 기사 제목 사진만 3개까지 다운로드
        if count > 20:
            break
    except Exception as e:
        pass


driver.close() # 브라우져 종료