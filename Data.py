import streamlit as st
from directory_tree import display_tree

st.set_page_config(
    page_title="Data",
    page_icon="👋",
)

st.write("# Data Status")

st.markdown(
    '''Data Structure\n\n
    eng/ 
    ├── GSM8k_test_ver.1.json 
    ├── GSM8k_train_ver.1.json 
    ├── MATHQA_data_ver.1.json 
    ├── mwp_kr_data_result_ver.1.json 
    └── SVAMP_result_ver.1.json 
'''
)

