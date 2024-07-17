import streamlit as st


st.title('로그아웃')

if st.button('로그아웃'):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_set_query_params(page="auth")
        st.experimental_rerun()