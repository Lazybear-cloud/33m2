import streamlit as st
import pandas as pd

# 페이지 설정: 와이드 모드로 설정
st.set_page_config(layout="wide")

# 웹페이지 제목
st.title("Lazy._.bear 33m2 물건 검색기")

# GitHub에 있는 엑셀 파일의 raw 경로
url = '33m2_1101.xlsx'

# 엑셀 파일을 pandas DataFrame으로 읽기
df = pd.read_excel(url, engine='openpyxl')

# 데이터 미리보기
st.write("일부 데이터 미리보기:")
st.dataframe(df.head(300))

# 필터링된 데이터의 행 수 출력
st.write(f"총 물건 개수: {df.shape[0]}개")

# 입력 필드를 두 개의 열로 나누기
col1, col2, col3 = st.columns(3)

# 첫 번째 필터링 조건 (가로 배치, '지역'을 기본값으로 설정)
with col1:
    # '지역' 컬럼을 고정으로 설정하고 선택할 수 있는 리스트 제공
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
    column_name2 = '시'  # '시'을 고정된 값으로 사용
    column_filtered_df1 = df[df['지역'] == condition_value1]
    column_option2 = sorted(column_filtered_df1['시'].dropna().unique())

    # '지역' 컬럼에 대해 조건 값을 입력받음
    condition_value2 = st.selectbox(f"'{column_name2}' 컬럼에서 검색할 조건을 선택하세요", column_option2)

# 세 번째 필터링 조건 (세 번째 열, '구' 기본값)
with col3:
    # '시' 컬럼을 고정으로 설정
    column_name3 = '구'  # '시'을 고정된 값으로 사용
    column_filtered_df2 = df[df['시'] == condition_value2]
    column_option3 = ["전체"] + sorted(column_filtered_df1['구'].dropna().unique())
    
    # '지역' 컬럼에 대해 조건 값을 입력받음
    condition_value3 = st.selectbox(f"'{column_name3}' 컬럼에서 검색할 조건을 선택하세요", column_option3)


# 데이터 검색 버튼
if st.button("데이터 검색"):
    # 조건을 동적으로 구성하여 입력된 값에 맞게 필터링
    filtered_data = df[
        (df["지역"].astype(str).str.contains(condition_value1, case=False, na=False)) &
        (df["시"].astype(str).str.contains(condition_value2, case=False, na=False)) &
        (df["구"].astype(str).str.contains(condition_value3, case=False, na=False)) &
        ((df["구"].astype(str).str.contains(condition_value3, case=False, na=False)) if condition_value3 != "전체" else True)  # 지역2가 "전체"일 경우 모든 값 허용
    ]

    # 필터링된 데이터 표시
    st.dataframe(filtered_data)

    # 필터링된 데이터의 행 수 출력
    st.write(f"검색된 물건 개수: {filtered_data.shape[0]}개")

else:
    st.write("검색 조건을 설정하고 '데이터 검색' 버튼을 눌러주세요.")
