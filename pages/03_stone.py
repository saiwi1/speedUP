from csv import list_dialects
import streamlit as st
import datetime
import sqlite3
import csv

st.title('石材計算')
st.caption('ない場合は0を入力してね。半角の数字のみで入力してください。エラーがでます。')

with st.form(key='stone_t'):
    Gov_id = st.text_input('総督ID','n/a')
    stone_0_75= st.number_input('石材 750',0,999999999,0)
    stone_07_5= st.number_input('石材 7500',0,999999999,0)
    stone_112_5= st.number_input('石材 37500',0,999999999,0)
    stone_0375= st.number_input('石材 112500',0,999999999,0)
    stone_0500= st.number_input('石材 375000',0,999999999,0)
    stone_1125= st.number_input('石材 1125000',0,999999999,0)
    stone_3750= st.number_input('石材 3750000',0,999999999,0)
    stone_have= st.number_input('手持ちの石材の量',0,9999999999999,0)



    submit_btn = st.form_submit_button('計算する')
    if submit_btn:
        w_1=(stone_0_75)*0.75*1000
        w_2=(stone_07_5)*7.5*1000
        w_3=(stone_112_5)*37.5*1000
        w_4=(stone_0375)*112.5*1000
        w_5=(stone_0500)*375*1000
        w_6=(stone_1125)*1125*1000
        w_7=(stone_3750)*3750*1000
        w_8=stone_have
       
        stone_total00=w_1+w_2+w_3+w_4+w_5+w_6+w_7+w_8
        stone_total01= stone_total00 // 10000//10000
        if stone_total00 >= 0:
            st.text(f'{Gov_id}様  石材は、{stone_total01}億分あります。({stone_total00:,}です)')
        dt_now = datetime.datetime.now()
        dt_str = dt_now.strftime('%Y%m%d%H%M%S')
        db_name = 'stonetotal.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # テーブルの作成
        c.execute('''CREATE TABLE IF NOT EXISTS stonetotal(timestamp str, year int, Month int,Day int,Hour int,Minutes int,Second int,Gov_id str,stone_total00 stone_total01 int,stone_0_75 int,stone_07_5 int,stone_112_5 int,stone_0375 int,stone_0500 int,stone_1125 int,stone_3750 int,speed_H_15h int,stone_have int)''')

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
        (dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,stone_total00,stone_total01,stone_0_75,stone_07_5,stone_112_5,stone_0375,stone_0500,stone_1125,stone_3750,stone_have),]
        c.executemany('INSERT INTO stonetotal VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        conn.commit()        
        
        data2 =[dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,stone_total00,stone_total01,stone_0_75,stone_07_5,stone_112_5,stone_0375,stone_0500,stone_1125,stone_3750,stone_have,]

        with open('stonetotal.csv', 'a') as f:
                writer = csv.writer(f)
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(data2)
            


    else:
        st.text(f'入力値を確認してください。ない場合は0を文字は半角で入力してください')
