import numpy as np
import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Pasien ini tidak menderita diabetes'
    else:
      return 'Pasien ini menderita diabetes'


    
def bar_chart(data, x_column, y_column):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.bar(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    st.pyplot()

def main():
    
    app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Main Data', 'Prediction'])  # two pages
    if app_mode == 'Home':    
      # giving title
      st.markdown("<h1 style='text-align: center; color: black;'>Diabetes Prediction Web App</h1>", unsafe_allow_html=True)
      st.image("diabetes.jpg", width=700)
      st.markdown('<div style="text-align:justify"><br><br>Diabetes adalah penyakit kronis yang ditandai dengan kadar gula darah tinggi. Diabetes dapat menyebabkan komplikasi serius, seperti penyakit jantung, stroke, penyakit ginjal, kebutaan, dan amputasi. Oleh karena itu, penting untuk mencegah diabetes.</div></br>', unsafe_allow_html=True)
      st.markdown('<div style="text-align:justify">Salah satu cara untuk mencegah diabetes adalah dengan menjaga berat badan yang sehat. Berat badan berlebih dan obesitas adalah faktor risiko utama diabetes tipe 2. Jika kelebihan berat badan atau obesitas, menurunkan berat badan bahkan sebesar 5-10 persen dapat membantu mengurangi risiko diabetes.</div></br>', unsafe_allow_html=True)
      st.markdown('<div style="text-align:justify">Cara lain untuk mencegah diabetes adalah dengan melakukan aktivitas fisik secara teratur. Aktivitas fisik dapat membantu menurunkan kadar gula darah dan meningkatkan sensitivitas insulin. Orang dewasa dianjurkan untuk melakukan setidaknya 150 menit aktivitas fisik intensitas sedang atau 75 menit aktivitas fisik intensitas tinggi setiap minggu.</div>', unsafe_allow_html=True)

    elif app_mode == 'Main Data':
      st.markdown("<h2 style='text-align: center; color: black;'>Dataset</h2>", unsafe_allow_html=True)   
      # Read CSV
      df = pd.read_csv('diabetes.csv')
      st.dataframe(df)
      st.markdown("<h4 style='text-align: center; color: black;'><br>Chart Bar<br></h4>", unsafe_allow_html=True)
      x_column = "Age"
      y_column = "DiabetesPedigreeFunction"
      bar_chart(df, x_column, y_column)


    elif app_mode == 'Prediction':  
      st.markdown("<h2 style='text-align: center; color: black;'>Prediction</h2>", unsafe_allow_html=True)  

      #getting the input data from the user
      Age = st.number_input("Age in Years", 1, 150, 25, 1)
      Pregnancies = st.number_input("Number of Pregnancies", 0, 20, 0, 1)
      Glucose = st.slider("Glucose Level", 0, 200, 25, 1)
      BloodPressure = st.slider('Blood Pressure', 0, 122, 69, 1)
      SkinThickness = st.slider("Skin Thickness", 0, 99, 20, 1)
      Insulin = st.slider("Insulin", 0, 846, 79, 1)
      BMI = st.slider("BMI", 0.0, 67.1, 31.4, 0.1)
      DiabetesPedigreeFunction = st.slider("Diabetics Pedigree Function", 0.000, 2.420, 0.471, 0.001)
      
      #code for prediction 
      diagnosis = ''
      
      #creating a button for prediction
      if st.button('Diabetes Test Result'):
          diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
      
      st.success(diagnosis)
      
if __name__=='__main__':
    main()
