import streamlit as st
    
st.set_page_config(
    page_title="Gemini",
    page_icon="👋",
)


st.sidebar.success("Select a demo above.")
st.write("# Welcome to Gemini Streamlit! 👋")



st.markdown(
'''    
    Gemini demo
'''
)

if "key" not in st.session_state:
    st.session_state.key = None
    
key = st.sidebar.text_input("Your key", type="password")
if not key:
    st.info("Please add your key to continue.")
    st.stop()
else:
    st.session_state.key=key