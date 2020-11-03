#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver


# In[7]:


#######################
#######################
####여기부터는 연습########
#######################
#######################

driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://jcr.clarivate.com/JCRJournalHomeAction.action?pg=JRNLHOME&year=2011&edition=SCIE&categories=IJ&newApplicationFlag=Y')


# In[72]:


click = driver.find_element_by_css_selector('#ext-gen1018 > div.loginWrap > div.main-container > div:nth-child(33) > div.reports-category > a:nth-child(2) > button')
click.click()


# In[73]:


click = driver.find_element_by_css_selector('#skip-to-content > div > div.l-wrapper-content > div.l-column-sidebar > div > div:nth-child(4) > a')
click.click()


# In[74]:


click = driver.find_element_by_css_selector('#IJ')
click.click()


# In[75]:


click = driver.find_element_by_css_selector('#skip-to-content > div > div.l-wrapper-content > div.l-column-sidebar > div > div.filters.filters-last > div:nth-child(3) > a:nth-child(2)')
click.click()


# In[76]:


click = driver.find_element_by_css_selector('#gridview-1022-record-ext-record-492 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1014.x-unselectable > div > a')
click.click()


# In[83]:


ELEMENT = driver.find_elements_by_css_selector('#gridview-1027-record-ext-record-336 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a')[-1]
driver.execute_script("arguments[0].scrollIntoView(true);", ELEMENT);


# In[85]:


name = driver.find_elements_by_css_selector('#gridview-1027-record-ext-record-347 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a')
print(name[0].text)


# In[88]:


next = driver.find_element_by_css_selector('#ext-gen1097')
next.click()
click = driver.find_element_by_css_selector('#boundlist-1169-listEl > ul > li:nth-child(2)')
click.click()

#boundlist-1169-listEl > ul > li:nth-child(2)
#boundlist-1169-listEl > ul > li:nth-child(1)


# In[107]:


click = driver.find_element_by_css_selector('#skip-to-content > div > div.l-wrapper-content > div.l-column-sidebar > div.filters.filters-last > div:nth-child(3) > a:nth-child(2)')
click.click()
            


# In[25]:


titles=[]
for i in range(1,11):
    title = driver.find_elements_by_css_selector('#pageSearchResults > div > div > mat-sidenav-container > mat-sidenav-content > app-journal-search-results > div:nth-child(3) > div:nth-child(%d) > mat-card > mat-card-title'%i)
    titles.append(title[0].text)
titles
#pageSearchResults > div > div > mat-sidenav-container > mat-sidenav-content > app-journal-search-results > div:nth-child(3) > div:nth-child(1) > mat-card > mat-card-title
#pageSearchResults > div > div > mat-sidenav-container > mat-sidenav-content > app-journal-search-results > div:nth-child(3) > div:nth-child(2) > mat-card > mat-card-title


# In[27]:


next = driver.find_element_by_css_selector('#pageSearchResults > div > div > mat-sidenav-container > mat-sidenav-content > app-journal-search-results > div:nth-child(3) > div:nth-child(11) > mat-paginator > div > div > div.mat-paginator-range-actions > button.mat-paginator-navigation-next.mat-icon-button.mat-button-base > span')
next.click()

#######################
#######################
####여기까지 연습########
#######################
#######################


# In[116]:


##여기부터 실제 저널 타이틀 크롤링 ##
import time
driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.get('https://jcr.clarivate.com/JCRJournalHomeAction.action?pg=JRNLHOME&year=2011&edition=SCIE&categories=IJ&newApplicationFlag=Y')

##크롤링할 웹페이지까지 들어가는 과정
time.sleep(4)

#카테고리별 검색
click = driver.find_element_by_css_selector('#ext-gen1018 > div.loginWrap > div.main-container > div:nth-child(33) > div.reports-category > a:nth-child(2) > button')
click.click()
time.sleep(1)
#카테고리 클릭
click = driver.find_element_by_css_selector('#skip-to-content > div > div.l-wrapper-content > div.l-column-sidebar > div > div:nth-child(4) > a')
click.click()
time.sleep(0.2)
#engineering, industrial 선택
click = driver.find_element_by_css_selector('#IJ')
click.click()
time.sleep(0.2)
#검색 클릭
click = driver.find_element_by_css_selector('#skip-to-content > div > div.l-wrapper-content > div.l-column-sidebar > div > div.filters.filters-last > div:nth-child(3) > a:nth-child(2)')
click.click()
time.sleep(1)
#journal 클릭
click = driver.find_element_by_css_selector('#gridview-1022-record-ext-record-492 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1014.x-unselectable > div > a')
click.click()
time.sleep(1)
#본격 저널 이름 크롤링
#gridview-1027-record-ext-record-300 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-778 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-1001 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-1225 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-1446 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-1666 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-1885 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-2104 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-2324 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a
#gridview-1027-record-ext-record-2541 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a

# search.send_keys(iise)
start = [300, 778, 1001, 1225, 1446, 1666, 1885, 2104, 2324, 2541]
num = [48, 46, 47, 44, 44, 43, 43, 44, 43, 38]
titles_total = []

year = 1
for i in num:
    titles = []
    for count in range(i):
        title = driver.find_elements_by_css_selector('#gridview-1027-record-ext-record-%d > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a' % (start[year-1]+count))
        try:
            titles.append(title[0].text)
        except:
            while(not title):
                title = driver.find_elements_by_css_selector('#gridview-1027-record-ext-record-%d > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a' % (start[year-1]+count))
            titles.append(title[0].text)        
            time.sleep(0.5)
        ELEMENT = driver.find_elements_by_css_selector('#gridview-1027-record-ext-record-%d > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a' % (start[year-1]+count))[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", ELEMENT);
        if count==(i-1):
            titles_total.append(titles)
            next = driver.find_element_by_css_selector('#ext-gen1097')
            next.click()
            time.sleep(0.5)
            click = driver.find_element_by_css_selector('#boundlist-1169-listEl > ul > li:nth-child(%d)' % (year+1))
            time.sleep(0.5)
            click.click()
            year += 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            click = driver.find_element_by_css_selector('#skip-to-content > div > div.l-wrapper-content > div.l-column-sidebar > div.filters.filters-last > div:nth-child(3) > a:nth-child(2)')
            click.click()
            time.sleep(1)
    print(len(titles))


# In[118]:


print(len(titles_total))

#gridview-1027-record-ext-record-311 > td.x-grid-cell.x-grid-td.x-grid-cell-gridcolumn-1011.x-unselectable > div > div > a


# In[119]:


#### 타이틀 리스트 피클로 저장하기
# import pickle
# with open('D:/chromedriver/title.pickle','wb') as fw:
#     pickle.dump(titles_total, fw)


# In[89]:


#### 저장된 타이틀 리스트 가져오기
import pickle
with open('C:/Users/user/Documents/카카오톡 받은 파일/title/title.pickle','rb') as l:
    total = pickle.load(l)


# In[195]:


total[1]


# In[183]:


import time
#######################
#######################
####여기는 연습########
#######################
#######################
driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&search_mode=GeneralSearch&SID=C14AoANLXE6MhJRPoMD&preferencesSaved=')
time.sleep(6)


# In[138]:


# e = driver.find_element_by_id("currUrl")
# e.get_attribute("value")


# In[184]:


search = driver.find_elements_by_css_selector('#value\(input1\)')[0]
search.clear()
search.send_keys(total[0][0])
### 검색하기

click = driver.find_element_by_css_selector('#searchrow1 > td.search-criteria-cell2 > span > span.selection > span > span.select2-selection__arrow')
click.click()
time.sleep(0.5)
# click = driver.find_element_by_css_selector('#select2-select1-result-yrvt-SO')
# click.click()
time.sleep(0.5)
click = driver.find_element_by_css_selector('#searchCell1 > span.searchButton > button')
click.click()                    


# In[185]:


###오픈소스만 보기
click = driver.find_element_by_css_selector('#OpenAccessFilter_1')
click.click()
click = driver.find_element_by_css_selector('#PublicationYear_2')
click.click()
click = driver.find_element_by_css_selector('#refine_form > div.block-search-mini > button')
click.click()


# In[188]:


## 파일다운받기
# click = driver.find_element_by_css_selector('#SelectPageChkId')
# click.click()
# time.sleep(1)
click = driver.find_element_by_css_selector('#exportTypeName')
click.click()
click = driver.find_element_by_css_selector('#numberOfRecordsRange')
click.click()
time.sleep(1)
click = driver.find_element_by_css_selector('#page > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-quickoutput.qoExcel > div.ui-dialog-content.ui-widget-content > form > div.quickoutput-overlay-buttonset > span > button')
click.click()
time.sleep(4)


# In[189]:


driver.close()


# In[ ]:


###############################
###############################
#########여기까지 연습#########
###############################
###############################


# In[ ]:


############진짜 시작###########


# In[231]:


count = 0
year = 2
for i in total[8:]:
    for j in range(5):
        driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get('https://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&search_mode=GeneralSearch&SID=F2PoJp6cidrDdVpoKpn&preferencesSaved=')
        time.sleep(6)
        search = driver.find_elements_by_css_selector('#value\(input1\)')[0]
        search.clear()
        search.send_keys(i[j])
        ### 검색하기
        click = driver.find_element_by_css_selector('#searchrow1 > td.search-criteria-cell2 > span > span.selection > span > span.select2-selection__arrow')
        click.click()
        time.sleep(0.5)
        click = driver.find_element_by_css_selector('#searchCell1 > span.searchButton > button')
        click.click()              
        time.sleep(1)
        ###오픈소스만 보기
#         click = driver.find_element_by_css_selector('#OpenAccessFilter_1')
#         click.click()
        click = driver.find_element_by_css_selector('#PublicationYear_%d' % (year))
        click.click()
        click = driver.find_element_by_css_selector('#refine_form > div.block-search-mini > button')
        click.click()
        ##파일 다운받기
        time.sleep(4)
        click = driver.find_element_by_css_selector('#exportTypeName')
        click.click()
        click = driver.find_element_by_css_selector('#numberOfRecordsRange')
        click.click()
        time.sleep(1)
        click = driver.find_element_by_css_selector('#page > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-quickoutput.qoExcel > div.ui-dialog-content.ui-widget-content > form > div.quickoutput-overlay-buttonset > span > button')
        click.click()
        time.sleep(5)
        driver.close()
        count += 1
    year += 1
    print("finish download %d paper" % count)


# In[226]:


driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&search_mode=GeneralSearch&SID=C14AoANLXE6MhJRPoMD&preferencesSaved=')
total[2][4] 


# In[233]:


import pandas as pd


# In[299]:


df = pd.read_excel('C:/Users/user/Documents/paper/2019/savedrecs.xls')


# In[300]:


column_list = ['Article Title', 'Author Full Names', 'Source Title', 'Abstract', 'Publication Year']


# In[301]:


df = df[column_list]


# In[302]:


df.shape[0]


# In[314]:


df_sub = pd.read_excel('C:/Users/user/Documents/paper/2018/savedrecs (9).xls')
df_sub = df_sub[column_list]
df = df.append(df_sub)
df.shape[0]


# In[315]:


year = 2017
num = 10

while(True):
    df_sub = pd.read_excel('C:/Users/user/Documents/paper/%d/savedrecs (%d).xls' % (year, num))
    df_sub = df_sub[column_list]
    df = df.append(df_sub)
    num += 1
    if num%5==0:
        year -= 1
    if year==2009:
        break;
print('finish!')

# In[317]:

df.shape[0]


# In[319]:


# #### 논문들 데이터 프레임 피클로 저장하기
# import pickle
# with open('C:/Users/user/Downloads/df.pickle','wb') as fw:
#     pickle.dump(df, fw)


# In[320]:


#### 저장된 논문들 데이터 프레임 가져오기
import pickle
with open('C:/Users/user/Documents/카카오톡 받은 파일/df.pickle','rb') as l:
    df = pickle.load(l)


# In[321]:


df.shape[0]


"""
이 밑에는 쓸모없음.
"""


# In[16]:


## pdf text로 긁어모을때 필요한 lib
pip install pdfminer


# In[19]:


### pdf읽어서 text 긁기 함수 정의.
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def read_pdf_PDFMINER(pdf_file_path):
    """
    pdf_file_path: 'dir/aaa.pdf'로 구성된 path로부터 
    내부의 text 파일을 모두 읽어서 스트링을 리턴함.
    """
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())


# In[39]:


##pdf 다운로드 받기
import os
from urllib import request

dir = 'D:/capstone'
def get_download(url,fname,directory):
#     try:
    os.chdir(directory)
    print(url)
    request.urlretrieve(url,fname)
    print('다운로드 완료')
#     except:
#         print(1)
#         return None


# In[69]:


####본격 pdf 다운로드###

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')

id = 1
count = 1
for name in titles:
    driver.get('https://arxiv.org/search/?query=&searchtype=journal_ref&abstracts=show&order=-announced_date_first&size=200')
    time.sleep(5)

    search = driver.find_elements_by_css_selector('#query')[0]
    search.send_keys(name)
    time.sleep(1)
    
    click = driver.find_element_by_css_selector('#main-container > div.content > form > div.field.has-addons-tablet > div:nth-child(3) > button')
    click.click()    
    time.sleep(1)
    while(1):
        try:
            select = driver.find_elements_by_css_selector('#main-container > div.content > ol > li:nth-child(%d) > div > p > span > a' % count)[0]
            time.sleep(1)
        except:
            count = 1
            break
        url = select.get_attribute('href')
    
        get_download(url, '%d.pdf' % id, dir)
    
        count += 1

        id += 1
    


# In[70]:


file_path = 'D:/capstone/1.pdf'

s = read_pdf_PDFMINER(file_path)


# In[71]:


s


# In[ ]:




