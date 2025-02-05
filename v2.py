import streamlit as st
from streamlit_molstar import st_molstar
import os

# 페이지 제목 설정
st.set_page_config(page_title="The Viewer")
st.title("The Viewer")

# 파일 업로드 위젯 (PDB 파일만 허용)
uploaded_file = st.file_uploader("PDB 파일을 업로드하세요.", type=["pdb"])
print(">>> ",uploaded_file)
if uploaded_file is not None:
    try:
        # 업로드된 파일을 저장할 디렉토리 생성 (존재하지 않으면 생성)
        upload_dir = "uploaded_files"
        os.makedirs(upload_dir, exist_ok=True)
        
        # 업로드한 파일의 이름을 사용하여 저장할 경로 생성
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        # 업로드한 파일을 바이너리 형태로 저장
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    except Exception as e:
        st.error(f"파일 저장 중 오류 발생: {e}")
    else:
        # 저장된 파일의 경로를 st_molstar에 전달하여 Mol* 뷰어를 표시
        st_molstar(file_path, height='400px')
else:
    st.info("PDB 파일을 업로드하면 구조가 시각화됩니다.")
