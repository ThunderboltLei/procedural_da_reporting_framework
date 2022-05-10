"""
@author raymanlei
@since 2022-05-08 22:22:08
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

from PIL import Image

from components import t_c_body
from utils import mysql_util


def script_execute(sidebar):
    st.markdown('''
        - #### 现象&问题
            - DAU持续下降原因？
            - 猜测：
                - 1、大盘DAU不同活跃度用户变化不一样，导致渗透率下降
                - 2、内容是否有异常
    ''')
    st.title('>>> 样例1：这里支持使用"左侧按钮控制图表"')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.title(time.strftime("当前日期：%Y年%m月%d日", time.localtime()))
    start_date = "20200101"
    gap = 365
    date_list = pd.to_datetime(pd.date_range(start=start_date, periods=gap).strftime("%Y%m%d").tolist())
    chart_data = pd.DataFrame(np.random.randn(365, 2), columns=['真实值', '预测值'], index=date_list)  # 传入DataFrame
    plt.plot(date_list, chart_data['真实值'], label='真实值')
    plt.plot(date_list, chart_data['预测值'], label='预测值')
    plt.ylim(bottom=0)
    plt.xticks(rotation=45)
    # plt.title(st_sidebar.sidebar()[0] + '行业' + st_sidebar.sidebar()[1] + '股票在' + st_sidebar.sidebar()[2] + '时间窗口下的预测结果',
    plt.title(sidebar[0] + '行业' + sidebar[1] + '股票在' + sidebar[2] + '时间窗口下的预测结果',
              loc='center',
              fontproperties="SimHei",
              fontsize=20)
    plt.xlabel('日期', loc='right')
    plt.ylabel('价格', loc='top')
    plt.legend(loc='upper right')
    st.pyplot()

    st.title('>>> 样例2：这里支持使用"第三方"数据库.目前，支持 MySQL，后续扩展 Hive，Spark')
    desc_info = mysql_util.run_query("desc core_indicator;")
    df_desc = pd.DataFrame(desc_info)
    st.table(df_desc)
    rows = mysql_util.run_query("SELECT * from core_indicator;")
    df_rows = pd.DataFrame(rows, columns=df_desc.iloc[:, 0])
    st.table(df_rows)
    for row in rows:
        st.write(f"{row[0]} has a {row[1]}, {row[2]}, {row[3]}, {row[4]}")

    st.code('''样例 SQL（忽略实际意义~~~）
    select count(1)
    from (
             select uid,
                    dt
             from (
                      select t1.uid                as uid,
                             date_sub(t1.dt, t1.r) as dt
                      from (
                               select uid,
                                      dt,
                                      row_number() over (distribute by uid sort by dt) as r
                               from login
                               where login_status = 1
                           ) as t1
                  ) as t2
             group by uid, dt
             having count(1) > 7
         ) as t3
    ;
    ''')

    # ----- part_alpha ----- #
    t_c_body.part_alpha()

    # ----- 读取数据 ----- #
    excel_file = '/opt/developments/jetbrains-work/myprojects/thunderboltlei/X-Projects/python/z-python-proj/datas/xls/各部门对生产部的评分情况.xlsx'
    sheet_name = 'DATA'

    df = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='B:D',
                       header=3)
    print(df)

    # 此处为各部门参加问卷调查人数
    df_participants = pd.read_excel(excel_file,
                                    sheet_name=sheet_name,
                                    usecols='F:G',
                                    header=3)
    df_participants.dropna(inplace=True)

    # streamlit的多重选择(选项数据)
    department = df['部门'].unique().tolist()
    # streamlit的滑动条(年龄数据)
    ages = df['年龄'].unique().tolist()
    # print(type(ages))

    st.title('>>> 样例3：这里支持使用"滚动条"控制图表')
    # st.sidebar.selectbox('年龄', sorted(ages))
    st.sidebar.selectbox('年份', [x for x in range(1970, 2031)])
    # 滑动条, 最大值、最小值、区间值
    age_selection = st.slider('年龄:',
                              min_value=min(ages),
                              max_value=max(ages),
                              value=(min(ages), max(ages)))

    # 多重选择, 默认全选
    department_selection = st.multiselect('部门:',
                                          department,
                                          default=department)

    # 根据选择过滤数据
    mask = (df['年龄'].between(*age_selection)) & (df['部门'].isin(department_selection))
    number_of_result = df[mask].shape[0]

    st.title('>>> 样例4：这里支持使用 MarkDown')
    # 根据筛选条件, 得到有效数据
    st.markdown(f'*有效数据: {number_of_result}*')

    # 根据选择分组数据
    # print(df[mask].groupby(by=['评分']).count())
    df_grouped = df[mask].groupby(by=['评分']).count()[['年龄']]
    df_grouped = df_grouped.rename(columns={'年龄': '计数'})
    df_grouped = df_grouped.reset_index()

    # 绘制柱状图, 配置相关参数
    bar_chart = px.bar(df_grouped,
                       x='评分',
                       y='计数',
                       text='计数',
                       color_discrete_sequence=['#F63366'] * len(df_grouped),
                       template='plotly_white')
    st.plotly_chart(bar_chart)

    st.title('>>> 样例5：这里支持使用"图文"')
    # 添加图片和交互式表格
    col1, col2 = st.columns(2)
    image = Image.open(
        '/opt/developments/jetbrains-work/myprojects/thunderboltlei/X-Projects/python/z-python-proj/datas/imgs/jpg/survey.jpg')
    col1.image(image,
               caption='Designed by 小F / 法纳斯特',
               use_column_width=True)
    col2.dataframe(df[mask], width=300)

    st.title('>>> 样例6：这里支持使用"图文"')
    # 绘制饼图
    pie_chart = px.pie(df_participants,
                       title='总参加人数',
                       values='人数',
                       names='公司部门')
    st.plotly_chart(pie_chart)
    st.markdown('''基于质能守恒定律：
        $
        E=mc^2
        $
    ''')
    st.markdown('''
    - #### 简要结论
    - 1、 社区DAU持续下降主要受两方面影响，环比-97.6W（-13.4%）
        - a) 大盘DAU-473W（-5.44%），影响社区DAU-39.6W（贡献度约41%）
        - b) 渗透率-0.7PP（-8.42%）,影响社区DAU-61.0W(贡献度约59%)
            - i) 用户维度：大盘DAU分维度来看，渗透率都有不同程度下降，大盘用户结构的影响未影响渗透率变化
                - 1、 其中35岁以上用户渗透率下降较大，31天内活跃天数最多 和最少的用户渗透率下降相对较大，女性渗透率下降较大
            - ii) 内容维度：内容上看各个分类各个doc都有不同程度下降，推断用户对近期内容讨论的兴趣度有一定程度下降。
                - 1、 分内容类型：各个分类都有不同程度下降，其中二级分类中下降幅度最大的是通用IP-9w(-52.8%)，下降绝对值最大的是电视剧IP-35.5w(-15.1%)、电影IP-17.5w(-14.2%)
                - 2、 长底页面分CID的社区渗透率普遍下降，说明目前各个长底页面的用户对内容兴趣缺乏，讨论意愿下降
                    - a) 长底整体的社区渗透率7.88%（-0.53pp,-6.33%）
    - 2、实验排查
        - 实验1：4月18日上线实验如下。经排查无影响
        链接：[欧拉插件](https://iwiki.woa.com/pages/viewpage.action?pageId=1286232876)
        - 实验2：2022-04-20 14:57:07 下线实验，经排查无影响
        链接：[欧拉插件](https://iwiki.woa.com/pages/viewpage.action?pageId=1286232876)

    ''')
