#%%
import streamlit as st
import pandas as pd
import datetime
from pattern import *
from code_road import *
# 패턴 찾기를 수행하는 함수
def search_pattern(start_date, end_date, stock_code):
    # 여기서 패턴 찾기 수행
    result = {}  # 결과를 저장할 공간, 실제 패턴 찾기 로직으로 대체해야 함
    return result

# UI
st.title('주식 패턴 예측')

# 입력 섹션
st.header('종목 코드')
stock_name = st.text_input('종목명을 선택해 주세요', value='삼성전자')
stock_code = find_stock_code(stock_name)[0]

st.header('날짜 선택')
start_date = st.date_input('시작일')
end_date = st.date_input('종료일')



# 예측 실행 버튼
if st.button('예측하기'):
    with st.spinner('예측 중...'):
        # 예측을 수행하는 함수 호출
        result = search_pattern(start_date, end_date, stock_code)
        # 결과 표시
        if result:
            st.write(result)
            # 패턴을 그리는 부분, 해당 기능이 있다고 가정
            for idx in result.keys():
                find_pattern(stock_code=stock_code, 
                            start_date=start_date, 
                            end_date=end_date)
        else:
            st.write('결과를 찾을 수 없습니다.')
#%%
