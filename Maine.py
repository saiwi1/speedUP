import streamlit as st
import datetime
import csv

st.title('治療加速&フリー加速計算')
st.caption('ない場合は0を入力してね。半角の数字のみで入力してください。エラーがでます。')

with st.form(key='sepeed_F'):
    Gov_id = st.text_input('総督ID','n/a')
    speed_H_05m= st.number_input('治療加速05分',0,999999999,0)
    speed_H_10m= st.number_input('治療加速10分',0,999999999,0)
    speed_H_15m= st.number_input('治療加速15分',0,999999999,0)
    speed_H_30m= st.number_input('治療加速30分',0,999999999,0)
    speed_H_60m= st.number_input('治療加速60分',0,999999999,0)
    speed_H_03h= st.number_input('治療加速03時間',0,999999999,0)
    speed_H_08h= st.number_input('治療加速08時間',0,999999999,0)
    speed_H_15h= st.number_input('治療加速15時間',0,999999999,)
    speed_F_01m= st.number_input('加速01分',0,999999999,0)
    speed_F_05m= st.number_input('加速05分',0,999999999,0)
    speed_F_10m= st.number_input('加速10分',0,999999999,0)
    speed_F_15m= st.number_input('加速15分',0,999999999,0)
    speed_F_30m= st.number_input('加速30分',0,999999999,0)
    speed_F_60m= st.number_input('加速60分',0,999999999,0)
    speed_F_03h= st.number_input('加速03時間',0,999999999,0)
    speed_F_08h= st.number_input('加速08時間',0,999999999,0)
    speed_F_15h= st.number_input('加速15時間',0,999999999,0)
    speed_F_24h= st.number_input('加速24時間',0,999999999,0)
    speed_F_03d= st.number_input('加速03日間',0,999999999,0)



    submit_btn = st.form_submit_button('計算する')
    if submit_btn:
        H_05m=(speed_H_05m)*5
        H_10m=(speed_H_15m)*10
        H_15m=(speed_H_15m)*15
        H_30m=(speed_H_30m)*30
        H_60m=(speed_H_60m)*60
        H_03h=(speed_H_03h)*180
        H_08h=(speed_H_08h)*480
        H_15h=(speed_H_15h)*900
        F_01m=(speed_F_01m)*1
        F_05m=(speed_F_05m)*5
        F_10m=(speed_F_15m)*10
        F_15m=(speed_F_15m)*15
        F_30m=(speed_F_30m)*30
        F_60m=(speed_F_60m)*60
        F_03h=(speed_F_03h)*180
        F_08h=(speed_F_08h)*480
        F_15h=(speed_F_15h)*900
        F_24h=(speed_F_24h)*1440
        F_03d=(speed_F_03d)*4320
       
        speed_F_total=F_01m+F_05m+F_10m+F_15m+F_30m+F_60m+F_03h+F_08h+F_15h+F_24h+F_03d+H_05m+H_10m+H_15m+H_30m+H_60m+H_03h+H_08h+H_15h
        speed_F_total_d= speed_F_total // 1440
        if speed_F_total >= 0:
            st.text(f'{Gov_id}様  治療加速と加速合わせて、{speed_F_total_d}日分（端数切捨て)(分単位だと{speed_F_total}分です)')
            today = datetime.date.today()
            input_today =format(today, '%Y-%m-%d')
            list_01=[input_today,Gov_id,speed_H_05m,speed_H_10m,speed_H_15m,speed_H_30m,speed_H_60m,speed_H_03h,speed_H_08h,speed_H_15h,speed_F_01m,speed_F_05m,speed_F_15m,speed_F_30m,speed_F_60m,speed_F_03h,speed_F_08h,speed_F_15h,speed_F_24h,speed_F_03h,speed_F_total,speed_F_total_d]
            with open('フリー加速計算.csv', 'a') as f:
                writer = csv.writer(f)
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(list_01)
            
            
            
            
        else:
            st.text(f'入力値を確認してください。ない場合は0を文字は半角で入力してください')
