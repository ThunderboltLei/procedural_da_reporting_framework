"""
@author raymanlei
@since 2022-05-08 20:54:55
"""

# streamlit_app.py
import os

import MySQLdb
import streamlit as st

st.SECRETS_FILE_LOC = os.path.abspath(os.path.join(os.environ['HOME'], ".streamlit", "secrets.toml"))
# print(st.SECRETS_FILE_LOC)
st_secrets = st.Secrets(st.SECRETS_FILE_LOC)
print(st_secrets)


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return MySQLdb.connect(**st_secrets["mysql"])


conn = init_connection()


# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


if __name__ == '__main__':
    import pandas as pd

    desc_info = run_query('desc mytable;')
    df_desc = pd.DataFrame(desc_info)
    print(df_desc)
    print(df_desc.iloc[:, 0])

    # rows = run_query("SELECT * from mytable;")
    #
    # # Print results.
    # for row in rows:
    #     st.write(f"{row[0]} has a :{row[1]}:")
