import streamlit as st

def family():
    st.title('가족 그룹 가입하기')

    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        st.warning('로그인이 필요합니다. 로그인 해주세요.')
        st.stop()

    family_name = st.text_input('가족 그룹 이름')
    family_members = st.text_area('가족 구성원 (쉼표로 구분)')

    if st.button('추가하기'):
        if family_name and family_members:
            family_members_list = [member.strip() for member in family_members.split(',')]
            if 'families' not in st.session_state:
                st.session_state.families = []
            st.session_state.families.append({'name': family_name, 'members': family_members_list})
            st.success(f'가족 그룹 "{family_name}"이(가) 추가되었습니다!')
        else:
            st.warning('가족 그룹 이름과 구성원을 입력해주세요.')

    # 추가된 가족 그룹 리스트를 보여주기
    if 'families' in st.session_state and st.session_state.families:
        st.subheader('추가된 가족 그룹들:')
        for family in st.session_state.families:
            st.write(f"그룹 이름: {family['name']}")
            st.write(f"구성원: {', '.join(family['members'])}")
            st.write('---')

if __name__ == "__main__":
    family()