from csv import list_dialects
import streamlit as st
import datetime
import sqlite3
import csv

st.title('食料計算')
st.caption('ない場合は0を入力してね。半角の数字のみで入力してください。エラーがでます。')

with st.form(key='food_t'):
    Gov_id = st.text_input('総督ID','n/a')
    food_0001= st.number_input('食料 1000',0,999999999,0)
    food_0010= st.number_input('食料 10000',0,999999999,0)
    food_0050= st.number_input('食料 50000',0,999999999,0)
    food_0150= st.number_input('食料 150000',0,999999999,0)
    food_0500= st.number_input('食料 500000',0,999999999,0)
    food_1500= st.number_input('食料 1500000',0,999999999,0)
    food_5000= st.number_input('食料 5000000',0,999999999,0)
    food_have= st.number_input('手持ちの食料の量',0,9999999999999,0)



    submit_btn = st.form_submit_button('計算する')
    if submit_btn:
        F_1=(food_0001)*1*1000
        F_2=(food_0010)*10*1000
        F_3=(food_0050)*50*1000
        F_4=(food_0150)*150*1000
        F_5=(food_0500)*500*1000
        F_6=(food_1500)*1500*1000
        F_7=(food_5000)*5000*1000
        F_8=food_have
       
        food_total00=F_1+F_2+F_3+F_4+F_5+F_6+F_7+F_8
        food_total01= food_total00 // 10000//10000
        if food_total00 >= 0:
            st.text(f'{Gov_id}様  食料は、{food_total01}億分あります。({food_total00:,}です)')
        dt_now = datetime.datetime.now()
        dt_str = dt_now.strftime('%Y%m%d%H%M%S')
        db_name = 'foodtotal.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        # テーブルの作成
        c.execute('''CREATE TABLE IF NOT EXISTS Foodtotal(timestamp str, year int, Month int,Day int,Hour int,Minutes int,Second int,Gov_id str,food_total00 int,food_total01 int,food_0001 int,food_0010 int,food_0050 int,food_0150 int,food_0500 int,food_1500 int,food_5000 int,food_have int)''')

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
        (dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,food_total00,food_total01,food_0001,food_0010,food_0050,food_0150,food_0500,food_1500,food_5000,food_have),]
        c.executemany('INSERT INTO Foodtotal VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        conn.commit()        
        
        data2 =[dt_str,dt_stY,dt_stm,dt_std,dt_stH,dt_stM,dt_stS,Gov_id,food_total00,food_total01,food_0001,food_0010,food_0050,food_0150,food_0500,food_1500,food_5000,food_have,]

        with open('foodtotal.csv', 'a') as f:
                writer = csv.writer(f)
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(data2)
            


    else:
        st.text(f'入力値を確認してください。ない場合は0を文字は半角で入力してください')
