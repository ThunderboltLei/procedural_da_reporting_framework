"""
@author raymanlei
@since 2022-05-09 10:36:18
"""

import matplotlib.pyplot as plt
import streamlit as st

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def headers():
    print('--->>> header')
    # h_col1, h_col2 = st.columns([2, 1])
    # with h_col1:
    st.header('欢迎来到 DA 世界')
    # st.subheader(' ' * 8 + 'By Thunderbolt.Lei')
    # with h_col2:
    # st.latex(r'E=mc^2')
    st.markdown('''质能守恒定律公式：
                $
                E=mc^2
                $
            ''')
