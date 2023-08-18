# 법령 크롤링 데이터 전처리

- [1.데이터 자체 삭제 케이스](#1데이터-자체-삭제-케이스)
    - [1-1.NaN 케이스](#1-1nan-케이스)
    - [1-2.길이(글자수)로 자르기](#1-2-길이글자수로-자르기)
- [2.특수문자 케이스](#2특수문자-케이스)
    - [2-1.대괄호 처리하기](#2-1대괄호-처리하기)
    - [2-2.꺾쇠괄호 처리하기](#2-2꺾쇠괄호-처리하기)
- [3.의미 불일치 케이스](#3의미-불일치-케이스)


## 1.데이터 자체 삭제 케이스
### 1-1.`NaN` 케이스

- 한글이 `NaN`인 경우는 영어에 쌍으로 수집되는 데이터가 누락된 경우이기에 삭제 처리 함

### 1-2. 길이(글자수)로 자르기

- `html`의 `tag` 중 `ho`에 해당하는 내용은 한 어절의 단어이거나 길이가 짧은 경우가 많음
- 따라서 [1-1](#1-1nan-케이스)을 처리한 후의 data(585,946) 중 단순 글자수를 기준으로 데이터양을 줄임
- 데이터를 삭제한 기준은 다음과 같음

    1. $log_{10}(한글\;글자\;수) < 1.5$의 경우 삭제
    2. 위의 방식에 따라 삭제된 데이터에서 $log_{10}(영어\;글자\;수) < 1.5$의 경우 삭제

- 이는 각 단계 별 데이터 셋의 $Q_1$ 값 근처의 값으로 처리 (하기 표 참조)
    - NaN 처리 후 데이터 셋의 한글 글자 수 통계량/값
        |통계량|값|
        |------|--------------|
        |count  |  585946.000000|
        |mean   |      1.725883|
        |std    |      0.349676|
        |min    |      0.301030|
        |25%    |      <span style="color:magenta">1.462398</span>|
        |50%    |      1.755875|
        |75%    |      1.986772|
        |max    |      3.253096|

    - 한글 삭제 후(log값 1.5 이하) 데이터 셋의 영어 글자수 통계량/값
        |통계량|값|
        |------|--------------|
        |count  |  585946.000000|
        |mean   |       2.182582|
        |std    |       0.362451|
        |min    |       0.301030|
        |25%    |       <span style="color:magenta">1.929419</span>|
        |50%    |       2.214844|
        |75%    |       2.451786|
        |max    |       3.899766|
<br>

## 2.특수문자 케이스

### 2-1.대괄호 처리하기

- 대괄호

### 2-2.꺾쇠괄호 처리하기

## 3.의미 불일치 케이스

## 3.무결성 검증