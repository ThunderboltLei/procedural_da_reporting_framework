"""
@author raymanlei
@since 2022-05-09 09:52:06
"""

import datetime

import streamlit as st


def part_alpha():
    ini_date = datetime.date.today()
    end_date = datetime.date.today()
    st.write('训练数据：')
    ini_date = st.date_input('起始日期：', value=datetime.date(2001, 1, 1))
    end_date = st.date_input('截止日期：')
    st.button('确定')
    return ini_date, end_date
