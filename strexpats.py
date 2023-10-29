# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

#Display title and description

st.title("Stuttgart Expats Etkinlik Kayıt Formu")
st.markdown("Lütfen kayıt için gerekli bilgileri giriniz.")

#Establishing a googlesheets connection.

conn = st.connection("gsheets", type=GSheetsConnection)

#Fetch existing vendors data

#existing_data = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/11FS5OoNggyZZKwlekgu4PsxkXm0gjaCpNv9lFr4jv9k/edit?usp=sharing", worksheet="Etkinlik", usecols=list(range(3)), ttl=5)
existing_data =  conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1fzG1L2idj8p-_5b2ieFK3gdDZPXKXGiZRWbaRCW9uVw/edit?usp=sharing",worksheet="Etkinlik",usecols=list(range(3)),ttl=5)
existing_data = existing_data.dropna(how="all")

#List of Etkinlik

Etkinlik = ["Cumhuriyet Kahvaltısı","80'ler-90'lar Partisi"]

with st.form(key="Etkinlik_form"):
        
    EtkinlikAdı = st.selectbox(label="Etkinlik Adı*",options=Etkinlik,index=None)
    Days = st.multiselect("Seçenekler",options=["Pazartesi","Salı","Çarşamba"])
    iletisim = st.text_input(label="Mail Adresi")
    #Mark Mandotary fields
    
    st.markdown("**Doldurulması zorunlu alan*")
    
    submit_button = st.form_submit_button("Kaydet")
    
    
    