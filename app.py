import streamlit as st
import pandas as pd

# 페이지 설정: 와이드 모드로 설정
st.set_page_config(layout="wide")

# 웹페이지 제목
st.title("엑셀 파일에서 데이터 검색")

# 미리 업로드된 엑셀 파일 불러오기
excel_file_path = 'C:/임형태/33m2_data.xlsx'  # 엑셀 파일 경로 입력
df = pd.read_excel(excel_file_path, engine='openpyxl')

# 데이터 미리보기
st.write("전체 데이터 미리보기:")
st.dataframe(df)

# 입력 필드를 두 개의 열로 나누기
col1, col2, col3 = st.columns(3)

# 첫 번째 필터링 조건 (가로 배치, '지역'을 기본값으로 설정)
with col1:
    # '지역' 컬럼이 있으면 기본값으로 설정
    if '지역' in df.columns:
        column_name1 = st.selectbox('첫 번째 조건을 적용할 컬럼을 선택하세요', df.columns, key='col1', index=df.columns.get_loc('지역'))
    else:
        column_name1 = st.selectbox('첫 번째 조건을 적용할 컬럼을 선택하세요', df.columns, key='col1')

    condition_value1 = st.text_input(f"'{column_name1}' 컬럼에서 검색할 조건을 입력하세요", key='val1')

# 두 번째 필터링 조건 (두 번째 열, '시' 기본값)
with col2:
    if '시' in df.columns:
        column_name2 = st.selectbox('두 번째 조건을 적용할 컬럼을 선택하세요', df.columns, key='col2', index=df.columns.get_loc('시'))
    else:
        column_name2 = st.selectbox('두 번째 조건을 적용할 컬럼을 선택하세요', df.columns, key='col2')

    condition_value2 = st.text_input(f"'{column_name2}' 컬럼에서 검색할 조건을 입력하세요", key='val2')

# 세 번째 필터링 조건 (세 번째 열, '구' 기본값)
with col3:
    if '구' in df.columns:
        column_name3 = st.selectbox('세 번째 조건을 적용할 컬럼을 선택하세요', df.columns, key='col3', index=df.columns.get_loc('구'))
    else:
        column_name3 = st.selectbox('세 번째 조건을 적용할 컬럼을 선택하세요', df.columns, key='col3')

    condition_value3 = st.text_input(f"'{column_name3}' 컬럼에서 검색할 조건을 입력하세요", key='val3')


# 사용자가 필터링 버튼을 눌렀을 때
if st.button("데이터 검색"):
    if condition_value1 and condition_value2:
        # 두 개의 조건을 기반으로 데이터 필터링
        filtered_data = df[
            df[column_name1].astype(str).str.contains(condition_value1, case=False, na=False) &
            df[column_name2].astype(str).str.contains(condition_value2, case=False, na=False)
        ]
        
        # 검색 결과가 있을 경우 출력
        if not filtered_data.empty:
            st.write(f"조건에 맞는 데이터 (총 {len(filtered_data)}건):")
            st.dataframe(filtered_data)
        else:
            st.write("조건에 맞는 데이터가 없습니다.")
    else:
        st.write("검색할 두 조건을 모두 입력하세요.")
