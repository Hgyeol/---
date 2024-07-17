import streamlit as st
from auth import auth

from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/')

db = client['database_test']
collection = db['mycollection']

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 세션 상태 초기화
if 'users' not in st.session_state:
    st.session_state.users = {}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# 로그인 상태에 따라 페이지 이동
query_params = st.query_params
page = query_params.get("page", ["auth"])[0]

if page == "smalltalk" and st.session_state.logged_in:
    st.switch_page("pages/smalltalk.py")
    # 여기서 SmallTalk 페이지 내용을 호출하거나 직접 작성할 수 있습니다.
    import pages.smalltalk as smalltalk
    smalltalk.main()
elif page == "auth":
    auth()
else:
    st.warning("로그인이 필요합니다. 로그인 해주세요.")
    auth()