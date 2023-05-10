from csv import list_dialects
import streamlit as st
import datetime
import sqlite3
import csv

st.title('金貨計算')
st.caption('ない場合は0を入力してね。半角の数字のみで入力してください。エラーがでます。')

with st.form(key='gold_t'):
    Gov_id = st.text_input('総督ID','n/a')
    gold_0001= st.number_input('金貨 500',0,999999999,0)
    gold_0010= st.number_input('金貨 3000',0,999999999,0)
    gold_0050= st.number_input('金貨 15000',0,999999999,0)
    gold_0050= st.number_input('金貨 50000',0,999999999,0)
    gold_0200= st.number_input('金貨 200000',0,999999999,0)
    gold_0600= st.number_input('金貨 600000',0,999999999,0)
    gold_2000= st.number_input('金貨 2000000',0,999999999,0)
    gold_have= st.number_input('手持ちの金貨の量',0,9999999999999,0)



    submit_btn = st.form_submit_button('計算する')
    if submit_btn:
        g_1=(gold_0001)*0.5*1000
        g_2=(gold_0010)*3*1000
        g_3=(gold_0050)*15*1000
        g_4=(gold_0050)*50*1000
        g_5=(gold_0200)*200*1000
        g_6=(gold_0600)*600*1000
        g_7=(gold_2000)*2000*1000
        g_8=gold_have
       
        gold_total00=g_1+g_2+g_3+g_4+g_5+g_6+g_7+g_8
        gold_total01= gold_total00 // 10000//10000
        if gold_total00 >= 0:
            st.text(f'{Gov_id}様  金貨は、{gold_total01}億分あります。({gold_total00}です)')
        dt_now = datetime.datetime.now()
        dt_str = dt_now.strftime('%Y%m%d%H%M%S')
        db_name = 'goldtotal.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # テーブルの作成
        c.execute('''CREATE TABLE IF NOT EXISTS goldtotal(timestamp str, year int, Month int,Day int,Hour int,Minutes int,Second int,Gov_id str,gold_total00 gold_total01 int,gold_0001 int,gold_0010 int,gold_0050 int,gold_0050 int,gold_0200 int,gold_0600 int,gold_2000 int,speed_H_15h int,gold_have int)''')

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
        (dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,gold_total00,gold_total01,gold_0001,gold_0010,gold_0050,gold_0050,gold_0200,gold_0600,gold_2000,gold_have),]
        c.executemany('INSERT INTO goldtotal VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        conn.commit()        
        
        data2 =[dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,gold_total00,gold_total01,gold_0001,gold_0010,gold_0050,gold_0050,gold_0200,gold_0600,gold_2000,gold_have,]

        with open('goldtotal.csv', 'a') as f:
                writer = csv.writer(f)
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(data2)
            


    else:
        st.text(f'入力値を確認してください。ない場合は0を文字は半角で入力してください')
