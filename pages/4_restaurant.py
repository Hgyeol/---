import streamlit as st

def restaurants():
    st.title('우리 동네 근처 맛집 추천')

    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        st.warning('로그인이 필요합니다. 로그인 해주세요.')
        st.stop()

    location = st.text_input('위치')

    if st.button('추천받기'):
        if location:
            st.success(f'{location} 근처의 맛집을 추천합니다!')
        else:
            st.warning('위치를 입력해주세요.')

if __name__ == "__main__":
    restaurants()