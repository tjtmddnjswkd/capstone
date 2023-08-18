# 법령 크롤링 아이디어

- [1.크롤링 사용 라이브러리](#1크롤링-사용-라이브러리)
    - [1-1.라이브러리 import](#1-1라이브러리-import)
    - [1-2.`selenium` 환경 설정](#1-2selenium-환경-설정)
- [2.크롤링 과정](#2크롤링-과정)
    - [2-1.크롤링 개요](#2-1크롤링-개요)

## 1.크롤링 사용 라이브러리

### 1-1.라이브러리 import

```python
import pandas as pd     # 수집된 데이터를 pd.DataFrame 형태로 저장

from selenium.webdriver.common.by import By     # Element 탐색
from selenium.webdriver.support.ui import WebDriverWait     # 명시적 대기(1)
from selenium.webdriver.support import expected_conditions as EC # 명시적 대기(2)
from selenium.webdriver.common.keys import Keys     # WebElement.click()이 저장되지 않을 때 Keys.Enter 전달
from selenium import webdriver      # webdriver
```

- 이전의 `selenium.webdriver`는 로컬 환경에서 사용되는 브라우저의 버전에 맞게 설치가 필요했지만, 최신 빌드는 설치 없이 사용 가능
- 대표적으로 파싱 시 사용되는 `request`, `bs4`의 라이브러리는 페이지 소스를 읽어 올 수 있으나, 동적으로 동작하는 페이지 파싱에 있어서 온전히 가져오지 못하는 문제가 있음
- 본 과제의 크롤링에서는 `Chrome` 드라이버를 활용

### 1-2.`selenium` 환경 설정

```python
options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_argument('headless') # headless 모드 설정
options.add_argument("window-size=1920x1080") # 화면크기(전체화면, FHD)
options.add_argument("disable-gpu") # 하드웨어 가속 끄기
options.add_argument("disable-infobars") # infobars 비활성화
options.add_argument("--disable-extensions") # 크롬 확장 비활성화

# 속도 향상을 위한 옵션 해제
prefs = {
    'profile.default_content_setting_values': {
        'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2,
        'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2,
        'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2,
        'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2,
        'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2,
        'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2,
        'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2,
        'durable_storage' : 2
        }
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
```

- `selenium`은 브라우저에게 탐색을 부여하는 방식이기에 좀 더 빠른 동작을 위해 옵션을 세팅해줌

## 2.크롤링 과정

### 2-1.크롤링 개요

``` python
while category:     # 법령 종류 루프 -> 법령 종류 파싱
    '''
    get_category_name
    '''
    while pages:    # 법령 종류에 속하는 법령의 pages 루프
        while laws: # 법령 종류에 따른 page에 속한 법령들 -> 법령명 파싱
            '''
            get_law_names
            '''
            for tag in ["none", "hang", "ho"]:   # 수집할 태그
```