import streamlit as st
import os
st.config.session_state_persistence = True        
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
    

gkey=None
if "gemini-key" in os.environ:
    gkey=os.environ["gemini-key"]
    
key = st.sidebar.text_input("Your key", type="password",value=gkey)
 
if key:
    st.session_state.key =key
    
if not st.session_state.key: 
    st.info("Please add your key to continue.")
    st.stop()

    
