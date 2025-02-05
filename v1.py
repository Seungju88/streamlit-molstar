import streamlit as st
import streamlit.components.v1 as components
import base64

# 페이지 설정
st.set_page_config(page_title="The Viewer")
st.title("The Viewer")

# 파일 업로드 (PDB 파일만 허용)
uploaded_file = st.file_uploader("PDB 파일을 업로드하세요.", type=["pdb"])

if uploaded_file is not None:
    try:
        # 업로드된 파일 읽기 (텍스트 형식)
        pdb_text = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"파일을 읽는 도중 오류가 발생했습니다: {e}")
    else:
        # PDB 파일 내용을 Base64로 인코딩 (HTML 내에 안전하게 포함)
        pdb_data_b64 = base64.b64encode(pdb_text.encode("utf-8")).decode("utf-8")
        
        # HTML 코드: initMolstar 함수를 먼저 정의한 후 Mol* 스크립트를 로드합니다.
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <title>The Viewer</title>
          <style>
            html, body, #app {{
              margin: 0;
              padding: 0;
              width: 100%;
              height: 100%;
              overflow: hidden;
            }}
          </style>
          <!-- Mol* 초기화 함수 정의 -->
          <script>
            function initMolstar() {{
              (async function() {{
                try {{
                  // Base64 문자열을 디코딩하여 PDB 텍스트로 변환
                  var pdbText = atob("{pdb_data_b64}");
                  // 텍스트를 Blob 객체로 생성 (MIME 타입: text/plain)
                  var blob = new Blob([pdbText], {{ type: 'text/plain' }});
                  // Blob URL 생성
                  var blobUrl = URL.createObjectURL(blob);
                  
                  // Mol*가 로드되었는지 확인
                  if (!window.Molstar) {{
                    console.error("Molstar가 정의되어 있지 않습니다.");
                    return;
                  }}
                  
                  // Mol* 뷰어 생성 (container: <div id="app">)
                  const viewer = await Molstar.Viewer.create(document.getElementById('app'), {{
                    layoutIsExpanded: true,
                  }});
                  console.log("Mol* viewer 생성 완료.");
    
                  // 로드 옵션: 단백질 구조의 경우 cartoon 모드
                  const loadOptions = {{
                    representationPreset: "cartoon"
                  }};
    
                  // Blob URL을 통해 PDB 파일의 구조 로드
                  // await viewer.loadStructureFromUrl(blobUrl, loadOptions);
                  await viewer.loadPdb(pdbText, loadOptions);
                  console.log("구조 로드 완료.");
                }} catch (error) {{
                  console.error("Mol* 초기화 중 에러 발생:", error);
                }}
              }})();
            }}
          </script>
          <!-- Mol* 라이브러리 로드: onload 이벤트에서 initMolstar() 호출 -->
          <script src="https://cdn.jsdelivr.net/npm/molstar@latest/build/viewer/molstar.js" onload="initMolstar()"></script>
        </head>
        <body>
          <div id="app"></div>
        </body>
        </html>
        """
        
        # HTML 컴포넌트 렌더링: allow_unsafe_scripts=False를 지정하여 외부 스크립트 실행을 허용
        components.html(html_code, height=600, scrolling=True, allow_unsafe_scripts=False)
else:
    st.info("PDB 파일을 업로드하면 구조가 시각화됩니다.")
