from csv import list_dialects
import streamlit as st
import datetime
import sqlite3
import csv

st.title('AP計算')
st.caption('ない場合は0を入力してね。半角の数字のみで入力してください。エラーがでます。')

with st.form(key='AP_t'):
    Gov_id = st.text_input('総督ID','n/a')
    AP_0050= st.number_input('緊急行動力 50',0,999999999,0)
    AP_0100= st.number_input('初級行動力 100',0,999999999,0)
    AP_0500= st.number_input('中級行動力 500',0,999999999,0)
    AP_1000= st.number_input('高級行動力 1000',0,999999999,0)

    submit_btn = st.form_submit_button('計算する')
    if submit_btn:
        a_1=(AP_0050)*0.5*1000
        a_2=(AP_0100)*3*1000
        a_3=(AP_0500)*15*1000
        a_4=(AP_1000)*50*1000

       
        AP_total00=a_1+a_2+a_3+a_4
        if AP_total00 >= 0:
            st.text(f'{Gov_id}様  行動力回復(AP)は{AP_total00:,}分あります')
        dt_now = datetime.datetime.now()
        dt_str = dt_now.strftime('%Y%m%d%H%M%S')
        db_name = 'aptotal.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # テーブルの作成
        c.execute('''CREATE TABLE IF NOT EXISTS aptotal(timestamp str, year int, Month int,Day int,Hour int,Minutes int,Second int,Gov_id str,AP_total00 ,AP_0050 int,AP_0100 int,AP_0500 int,AP_1000 int)''')

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
        (dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,AP_total00,AP_0050,AP_0100,AP_0500,AP_1000),]
        c.executemany('INSERT INTO aptotal VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        conn.commit()        
        
        data2 =[dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,AP_total00,AP_0050,AP_0100,AP_0500,AP_1000,]

        with open('aptotal.csv', 'a') as f:
                writer = csv.writer(f)
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(data2)
            


    else:
        st.text(f'入力値を確認してください。ない場合は0を文字は半角で入力してください')
