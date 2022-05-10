"""
@author raymanlei
@since 2022-05-09 10:42:02
"""
import streamlit as st

import scripts.demo.my_script_01 as my_script_01


def body(sidebar):
    print('--->>> body')
    with st.container():
        my_script_01.script_execute(sidebar)
        return
