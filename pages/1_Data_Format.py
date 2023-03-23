import streamlit as st
import pandas as pd
import time
import json


def clear_text():
    st.session_state["1"] = ""
    st.session_state["2"] = ""
    st.session_state["3"] = ""
    st.session_state["4"] = ""
    st.session_state["5"] = ""

problem_ex = '예: 어떤 수에 3를 곱해야 할 것을 잘못하여 2로 나누었더니 3이 되었습니다. 바르게 계산했을 때 답은 무엇인가요?'
solution_ex = '예: 2로 나누어서 3이 되는 어떤 수를 구하는 식은 2x3=6입니다. 어떤 수는 6입니다. 바르게 계산하면 6x3=18입니다. 답은 18입니다.'
answer_ex = '예: 18'
equation_ex = '예: 2x3=6  \n 6x3=18'
python_code_ex = '예: x/2=3  \n answer=x*3  \n print(answer)'


if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'

# Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)

# Show title and description of the app.
st.sidebar.markdown('Login')

username = st.sidebar.text_input("User Name", key="user")
password = st.sidebar.text_input("Password",type='password',key="pwd")

timestr = time.strftime("%Y%m%d")
file_path = "./data_"+username+"_"+timestr+".json"

st.title('TL Data Format')
col1, _, _, _, col2 = st.columns(5)

login_button =  st.sidebar.button('로그인')
if login_button:
    if password != "1234":
        st.sidebar.error('  비밀번호가 틀렸습니다. 다시 입력해주세요.', icon="🚨")
    elif username =="":
        st.sidebar.error('  아이디를 입력해주세요.', icon="🚨")
    else:
        st.sidebar.success("접속이 완료되었습니다.")
        time.sleep(0.8)
        st.session_state.sidebar_state = 'collapsed'
        st.experimental_rerun()

if login_button:
    st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
    # Force an app rerun after switching the sidebar state.
    st.experimental_rerun()

with col1:
    link_clear = st.button('Clear (초기화)', on_click=clear_text)


st.subheader('Problem (문제)')
p1= st.empty()
st.subheader('Solution (풀이 과정)')
p2 = st.empty()
st.subheader('Answer (답)')
p3= st.empty()
st.subheader('Equation (수식)')
st.write(equation_ex)
p4 = st.empty()
st.subheader('Python Code (파이썬 코드)')
st.write(python_code_ex)
p5= st.empty()
st.subheader('Grade (학년)')
p6 = st.empty()
st.subheader('Type (문제 유형)')   # 수찾기1: 조건수 찾기, 수찾기2: 미지수 찾기, 수찾기3: 연산 오류 찾기
p7= st.empty()

problem = p1.text_area(problem_ex, key=1)
solution = p2.text_area(solution_ex, key=2)
answer = p3.text_input(answer_ex, key=3)
equation = p4.text_area("(enter로 줄바꿈 하시면 됩니다.)", key=4)
code = p5.text_area("(마지막에 print(answer)를 꼭 첨부해주세요.)", key=5)
grade = p6.selectbox(
        '문제 수준',
        pd.Series(['초등학교 1학년', '초등학교 2학년', '초등학교 3학년', 
                    '초등학교 4학년', '초등학교 5학년', '초등학교 6학년', '중학교 이상']), key=6)
type = p7.selectbox(
        '8가지 유형',
        pd.Series(['산술연산', '순서정하기', '조합하기', '조건수 찾기', 
                    '미지수 찾기', '연산 오류 찾기', '크기비교', '도형','기타']), key=7)


def json_save(file_path, problem, grade, type, solution, equation, code, answer):
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = []
    data.append({"problem":problem, "grade":grade,"type":type, "solution":solution, "equation":equation, "code":code, "answer":answer})
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def hi():
    st.write("hihi")


if st.button('Upload (업로드)'):
    if username!=""  and password=="1234":
        if problem=="" or answer=="" or solution=="" or equation=="" or code=="" :
            st.error(' 미작성 된 항목이 있습니다. 확인해주세요.', icon="🚨")
        else:
            json_save(file_path, problem, grade, type, solution, equation, code, answer)
            st.success("저장되었습니다.")
    else:
        st.error(' 로그인을 먼저 해주세요.', icon="🚨") 
                

