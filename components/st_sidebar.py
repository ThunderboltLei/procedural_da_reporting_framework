"""
@author raymanlei
@since 2022-05-08 22:27:25
"""

import streamlit as st
import pandas as pd
from datetime import datetime as dt


def update_parameters(select_parameters):
    st.header('模板：' + str(dt.now().__format__('%Y-%m-%d')) + ' 分析报告 by raymanlei')
    st.info(select_parameters)
    return


def sidebar():
    print('--->>> sidebar')

    # file uploader
    uploaded_files = st.sidebar.file_uploader("Upload your Python DA Script", type=["py"], accept_multiple_files=True)
    if uploaded_files is not None:
        for f in uploaded_files:
            input_df = pd.read_csv(f)
            print(input_df.head(5))

    # part 2
    df_parameters = pd.DataFrame(
        {'industry': ['-', 'Financial', 'Medical'], 'name': ['-', 'Alibaba', 'Tencent'],
         'time': ['-', '5 Days', '7 Days']})
    select_parameters = []
    option_industry = '-'
    option_name = '-'
    option_time = '-'

    option_industry = st.sidebar.selectbox('Industry', df_parameters['industry'])
    if option_industry != '-':
        select_parameters.append(option_industry)
        option_name = st.sidebar.selectbox('Stock', df_parameters['name'])
    else:
        pass

    if option_name != '-':
        select_parameters.append(option_name)
        option_time = st.sidebar.selectbox('Times', df_parameters['time'])
    else:
        pass

    if option_time != '-':
        select_parameters.append(option_time)
        version_option = st.sidebar.selectbox('Anonymous：', ('-', 'Anonymous 1', 'Anonymous 2', 'Anonymous 3'))
        st.sidebar.button('Button Alpha')
        st.sidebar.button('Button Beta', on_click=update_parameters(select_parameters))

    return select_parameters
