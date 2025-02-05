import streamlit as st
from streamlit_molstar import st_molstar
from streamlit_molstar.docking import st_molstar_docking
import os

# 페이지 제목 설정
st.set_page_config(page_title="The Viewer")
st.title("The Viewer")

# 3개의 탭 생성
tabs = st.tabs(["Default view", "View Docking", "View Trajectory"])

for i, tab in enumerate(tabs):
    with tab:
        i += 1
        if i == 1:
            st.header("Default view")
            
            # 파일 업로드 위젯 (PDB 파일만 허용, 각 탭에 고유 key 지정)
            uploaded_file = st.file_uploader("PDB 파일을 업로드하세요.", type=["pdb"], key=f"file_uploader_{i}")
            st.write("1cbs.pdb 업로드")
            
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
                    st_molstar(file_path, height="400px")
            else:
                st.info("PDB 파일을 업로드하면 구조가 시각화됩니다.")
        elif i == 2:
            st.header("View Docking")
            
            # 파일 업로드 위젯 (PDB 파일만 허용, 각 탭에 고유 key 지정)
            pdb_uploaded_file = st.file_uploader("PDB 파일을 업로드하세요.", type=["pdb"], key=f"pdb_file_uploader_{i}")
            st.write("2zy1_protein.pdb 업로드")
            sdf_uploaded_file = st.file_uploader("SDF 파일을 업로드하세요.", type=["sdf"], key=f"sdf_file_uploader_{i}")
            st.write("docking.2zy1.0.sdf 업로드")

            if pdb_uploaded_file and sdf_uploaded_file is not None:
                try:
                    # 업로드된 파일을 저장할 디렉토리 생성 (존재하지 않으면 생성)
                    upload_dir = "uploaded_files"
                    os.makedirs(upload_dir, exist_ok=True)
                    
                    # 업로드한 파일의 이름을 사용하여 저장할 경로 생성
                    pdb_file_path = os.path.join(upload_dir, pdb_uploaded_file.name)
                    sdf_file_path = os.path.join(upload_dir, sdf_uploaded_file.name)
                    
                    # 업로드한 파일을 바이너리 형태로 저장
                    with open(pdb_file_path, "wb") as f:
                        f.write(pdb_uploaded_file.getbuffer())
                    with open(sdf_file_path, "wb") as f:
                        f.write(sdf_uploaded_file.getbuffer())

                except Exception as e:
                    st.error(f"파일 저장 중 오류 발생: {e}")
                else:
                    # 저장된 파일의 경로를 st_molstar에 전달하여 Mol* 뷰어를 표시
                    st_molstar_docking(pdb_file_path,
                                       sdf_file_path,
                                       key="5", height="400px")
            else:
                st.info("PDB 파일과 SDF 파일일을 업로드하면 구조가 시각화됩니다.")
        elif i == 3:
            st.header("View Trajectory")
            
            # 파일 업로드 위젯 (PDB 파일만 허용, 각 탭에 고유 key 지정)
            pdb_uploaded_file = st.file_uploader("PDB 파일을 업로드하세요.", type=["pdb"], key=f"pdb_file_uploader_{i}")
            st.write("complex.pdb 업로드")
            xtc_uploaded_file = st.file_uploader("XTC 파일을 업로드하세요.", type=["xtc"], key=f"xtc_file_uploader_{i}")
            st.write("complex.xtc 업로드")

            if pdb_uploaded_file and xtc_uploaded_file is not None:
                try:
                    # 업로드된 파일을 저장할 디렉토리 생성 (존재하지 않으면 생성)
                    upload_dir = "uploaded_files"
                    os.makedirs(upload_dir, exist_ok=True)
                    
                    # 업로드한 파일의 이름을 사용하여 저장할 경로 생성
                    pdb_file_path = os.path.join(upload_dir, pdb_uploaded_file.name)
                    xtc_file_path = os.path.join(upload_dir, xtc_uploaded_file.name)
                    
                    # 업로드한 파일을 바이너리 형태로 저장
                    with open(pdb_file_path, "wb") as f:
                        f.write(pdb_uploaded_file.getbuffer())
                    with open(xtc_file_path, "wb") as f:
                        f.write(xtc_uploaded_file.getbuffer())
                except Exception as e:
                    st.error(f"파일 저장 중 오류 발생: {e}")
                else:
                    # 저장된 파일의 경로를 st_molstar에 전달하여 Mol* 뷰어를 표시
                    st_molstar(pdb_file_path, xtc_file_path, height="400px", key="4")
            else:
                st.info("PDB 파일과 XTC 파일을 업로드하면 구조가 시각화됩니다.")
