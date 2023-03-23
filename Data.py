import streamlit as st
from directory_tree import display_tree

st.set_page_config(
    page_title="Data",
    page_icon="👋",
)

st.write("# Data Status")

customPath = r'C:\Users\jieunpark\Desktop\추론 AI 과제\data_processing\all_data_result\eng'
stringRepresentation = display_tree(customPath, string_rep=True, show_hidden=True)
# st.write(stringRepresentation)


st.markdown(
    '''Data Structure\n\n
    eng/ 
    ├── GSM8k_test_ver.1.json 
    ├── GSM8k_train_ver.1.json 
    ├── MATHQA_data_ver.1.json 
    ├── mwp_kr_data_result_ver.1.json 
    └── SVAMP_result_ver.1.json 
    kor/ 
    ├── GSM8k_trans_test_ver.2.json
    ├── GSM8k_trans_train_ver.2.json
    ├── HANDCRAFT_ver.1.json
    ├── KMWP_ver.1.json
    ├── KoEPT_result_test_ver.1.json
    ├── KoEPT_result_train_ver.1.json
    ├── Korean-MWP-dataset_test_result_ver.1.json
    ├── Korean-MWP-dataset_train_result_ver.1.json
    ├── Korean-MWP_test_ver.1.json
    ├── Korean-MWP_train_ver.1.json
    ├── Korean-MWP_valid_ver.1.json
    └── Korean_MWPS_result_ver.1.json
'''
)




























# import pandas as pd
# import streamlit as st
# from st_aggrid import AgGrid, GridOptionsBuilder
# from st_aggrid.shared import GridUpdateMode

# def aggrid_interactive_table(df: pd.DataFrame):
#     """Creates an st-aggrid interactive table based on a dataframe.
#     Args:
#         df (pd.DataFrame]): Source dataframe
#     Returns:
#         dict: The selected row
#     """
#     options = GridOptionsBuilder.from_dataframe(
#         df, enableRowGroup=True, enableValue=True, enablePivot=True
#     )

#     options.configure_side_bar()

#     options.configure_selection("single")
#     selection = AgGrid(
#         df,
#         enable_enterprise_modules=True,
#         gridOptions=options.build(),
#         theme="streamlit",
#         update_mode=GridUpdateMode.MODEL_CHANGED,
#         allow_unsafe_jscode=True,
#     )

#     return selection

# iris = pd.read_csv(
#     "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# )

# selection = aggrid_interactive_table(df=iris[:10])

# if selection:
#     st.write("You selected:")
#     st.json(selection["selected_rows"])

# st.write("## Code")
