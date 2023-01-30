import pandas as pd
import numpy as np 
import streamlit as st 
import pickle 

def Prediction(arr):
    model=pickle.load(open("model.sav", 'rb'))
    pred=model.predict([arr])
    return pred
def main():
    st.title("Human Stress Prediction")
    Heart_rate=st.text_input("Heart rate (60-160) (in BPM) :")
    
    Temperature=st.text_input("Temperature (25-50) (in celcius) :")
    output=""
    if st.button("Predict Stress Level"):
        try:
            Heart_rate=int(Heart_rate)
            Temperature=int(Temperature)
            output=Prediction([Heart_rate,Temperature])
            st.success(output[0])
        except:
            st.write("Enter correct values")
       


if __name__=="__main__":
    main()
    
