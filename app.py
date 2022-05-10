"""
@author raymanlei
@since 2022-05-07 23:23:40
"""
import matplotlib.pyplot as plt
import streamlit as st

from components import st_header, st_sidebar, st_body

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# # 设置网页名称
# st.set_page_config(page_title='Einstein\'s death formula',
#                    page_icon='🧊',
#                    layout="wide",
#                    menu_items={
#                        'Get Help': 'https://www.extremelycoolapp.com/help',
#                        'Report a bug': 'https://www.baidu.com',
#                        # 'Tencent': 'https://www.qq.com'
#                    })

sidebar = st_sidebar.sidebar()
if len(sidebar) != 3:
    st_header.headers()
else:
    st_body.body(sidebar)
