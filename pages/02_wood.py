from csv import list_dialects
import streamlit as st
import datetime
import sqlite3
import csv

st.title('木材計算')
st.caption('ない場合は0を入力してね。半角の数字のみで入力してください。エラーがでます。')

with st.form(key='wood_t'):
    Gov_id = st.text_input('総督ID','n/a')
    wood_0001= st.number_input('木材 1000',0,999999999,0)
    wood_0010= st.number_input('木材 10000',0,999999999,0)
    wood_0050= st.number_input('木材 50000',0,999999999,0)
    wood_0150= st.number_input('木材 150000',0,999999999,0)
    wood_0500= st.number_input('木材 500000',0,999999999,0)
    wood_1500= st.number_input('木材 1500000',0,999999999,0)
    wood_5000= st.number_input('木材 5000000',0,999999999,0)
    wood_have= st.number_input('手持ちの木材の量',0,9999999999999,0)



    submit_btn = st.form_submit_button('計算する')
    if submit_btn:
        w_1=(wood_0001)*1*1000
        w_2=(wood_0010)*10*1000
        w_3=(wood_0050)*50*1000
        w_4=(wood_0150)*150*1000
        w_5=(wood_0500)*500*1000
        w_6=(wood_1500)*1500*1000
        w_7=(wood_5000)*5000*1000
        w_8=wood_have
       
        wood_total00=w_1+w_2+w_3+w_4+w_5+w_6+w_7+w_8
        wood_total01= wood_total00 // 10000//10000
        if wood_total00 >= 0:
            st.text(f'{Gov_id}様  木材は、{wood_total01}億分あります。({wood_total00}です)')
        dt_now = datetime.datetime.now()
        dt_str = dt_now.strftime('%Y%m%d%H%M%S')
        db_name = 'woodtotal.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # テーブルの作成
        c.execute('''CREATE TABLE IF NOT EXISTS woodtotal(timestamp str, year int, Month int,Day int,Hour int,Minutes int,Second int,Gov_id str,wood_total00 wood_total01 int,wood_0001 int,wood_0010 int,wood_0050 int,wood_0150 int,wood_0500 int,wood_1500 int,wood_5000 int,speed_H_15h int,wood_have int)''')

            #入力値を取得する

        # データベースに接続する
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        dt_now = datetime.datetime.now()
        dt_str = dt_now.strftime('%Y%m%d%H%M%S')
        dt_stY = int(dt_now.strftime('%Y'))
        dt_stm = int(dt_now.strftime('%m'))
        dt_std = int(dt_now.strftime('%d'))
        dt_stH = int(dt_now.strftime('%H'))
        dt_stM = int(dt_now.strftime('%M'))
        dt_stS = int(dt_now.strftime('%S'))
        # データの挿入
        data = [
        (dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,wood_total00,wood_total01,wood_0001,wood_0010,wood_0050,wood_0150,wood_0500,wood_1500,wood_5000,wood_have),]
        c.executemany('INSERT INTO woodtotal VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        conn.commit()        
        
        data2 =[dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,wood_total00,wood_total01,wood_0001,wood_0010,wood_0050,wood_0150,wood_0500,wood_1500,wood_5000,wood_have,]

        with open('woodtotal.csv', 'a') as f:
                writer = csv.writer(f)
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(data2)
            


    else:
        st.text(f'入力値を確認してください。ない場合は0を文字は半角で入力してください')
