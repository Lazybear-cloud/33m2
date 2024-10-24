import streamlit as st
import pandas as pd

# 페이지 설정: 와이드 모드로 설정
st.set_page_config(layout="wide")

# 웹페이지 제목
st.title("Lazy._.bear 33m2 물건 검색기")

# GitHub에 있는 엑셀 파일의 raw 경로
url = 'https://github.com/Lazybear-cloud/33m2/blob/main/33m2_data1.xlsx'

# 엑셀 파일을 pandas DataFrame으로 읽기
df = pd.read_excel(url, engine='openpyxl')

# 데이터 미리보기
st.write("일부 데이터 미리보기:")
st.dataframe(df.head(1000))

# 입력 필드를 두 개의 열로 나누기
col1, col2, col3 = st.columns(3)

# 첫 번째 필터링 조건 (가로 배치, '지역'을 기본값으로 설정)
with col1:
    # '지역' 컬럼을 고정으로 설정하고 선택할 수 있는 리스트 제공
    st.markdown("**지역을 선택해주세요.**")  # '지역'을 고정 값으로 표시
    column_name1 = '지역'  # '지역'을 고정된 값으로 사용

    # '지역' 선택을 위한 리스트 정의
    지역_리스트 = [
        '서울특별시', '경기도', '인천광역시', '대전광역시', '부산광역시',
        '경상남도', '충청남도', '대구광역시', '전라남도', '제주특별자치도',
        '경상북도', '전북특별자치도', '강원특별자치도', '광주광역시',
        '세종특별자치시', '충청북도', '울산광역시', '전라북도'
    ]

    # 사용자가 선택할 수 있게 selectbox로 변경
    condition_value1 = st.selectbox(f"'{column_name1}' 컬럼에서 검색할 조건을 선택하세요", 지역_리스트, key='val1')

# 두 번째 필터링 조건 (두 번째 열, '시' 기본값)
with col2:
    # '시' 컬럼을 고정으로 설정
    st.markdown("**구/시를 입력해주세요.**")  # '지역'을 고정 값으로 표시
    column_name2 = '시'  # '시'을 고정된 값으로 사용

    # '지역' 컬럼에 대해 조건 값을 입력받음
    condition_value2 = st.text_input(f"'{column_name2}' 컬럼에서 검색할 조건을 입력하세요", key='val2')

# 세 번째 필터링 조건 (세 번째 열, '구' 기본값)
with col3:
    # '시' 컬럼을 고정으로 설정
    st.markdown("**동/구를 입력해주세요.**")  # '지역'을 고정 값으로 표시
    column_name3 = '구'  # '시'을 고정된 값으로 사용

    # '지역' 컬럼에 대해 조건 값을 입력받음
    condition_value3 = st.text_input(f"'{column_name3}' 컬럼에서 검색할 조건을 입력하세요", key='val3')


# 사용자가 필터링 버튼을 눌렀을 때
if st.button("데이터 검색"):
    if condition_value1 and condition_value2:
        # 두 개의 조건을 기반으로 데이터 필터링
        filtered_data = df[
            df[column_name1].astype(str).str.contains(condition_value1, case=False, na=False) &
            df[column_name2].astype(str).str.contains(condition_value2, case=False, na=False) &
            df[column_name3].astype(str).str.contains(condition_value3, case=False, na=False)
        ]

        st.text("")
        st.text("")
        
        # 검색 결과가 있을 경우 출력
        if not filtered_data.empty:
            st.write(f"조건에 맞는 데이터 (총 {len(filtered_data)}건):")
            st.dataframe(filtered_data)
        else:
            st.write("조건에 맞는 데이터가 없습니다.")
    else:
        st.write("검색할 조건을 모두 입력하세요.")
