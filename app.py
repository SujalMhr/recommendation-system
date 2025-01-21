import streamlit as st
import pickle

fooditems=pickle.load(open("fooditem_list.pkl",'rb'))
fooditem_list=fooditems['fooditem'].values

st.header("Food recommendation system")
st.selectbox("Select fooditem from dropdown", fooditems)

if st.button("show Recommend"):
    pass

fooditem_list=fooditems['fooditem']