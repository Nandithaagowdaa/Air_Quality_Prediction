import streamlit as st 
import pickle 
import os 
import pandas as pd 

#Introduction

st.title("Know what is the Air Quality in your city before ou go out ")

st.write("Get ahead of air pollution with our prediction for your city's Air Quality Index")

st.image("C:/Users/pc/Desktop/air-pollution-in-urban-area.tmb-1200v.jpg",caption ="Predict AQI",use_column_width=True)

def make_prediction(model,feature_set):
    y_predict=model.predict(feature_set)
    y_predict = round(float(y_predict),2)
    return y_predict
    
path = 'C:/Users/pc/Desktop/AQI Project' 

mreg= pickle.load(open(os.path.join(path,"C:/Users/pc/Desktop/AQI Project/Models/Multiple Regression.pkl"),'rb'))
preg= pickle.load(open(os.path.join(path,"C:/Users/pc/Desktop/AQI Project/Models/pregression.pkl"),'rb'))
dec_tree= pickle.load(open(os.path.join(path,"C:/Users/pc/Desktop/AQI Project/Models/Decision Tree.pkl"),'rb'))
rt_reg= pickle.load(open(os.path.join(path,"C:/Users/pc/Desktop/AQI Project/Models/Random Forest.pkl"),'rb'))
svr_reg= pickle.load(open(os.path.join(path,"C:/Users/pc/Desktop/AQI Project/Models/svrression.pkl"),'rb'))
poly_reg= pickle.load(open(os.path.join(path,"C:/Users/pc/Desktop/AQI Project/Models/poly_reg.pkl"),'rb'))

cities = ["Ahmedabad","Mumbai","Delhi","Chennai","Banglore"]
selected_city=st.selectbox("Select City:",cities)

pm2_5 =st.slider("PM2.5(Fine Particulate Matter)",min_value=0.0,max_value=50.0,value=3.0)
pm10 =st.slider("PM10(Coarse Particulate Matter)",min_value=0.0,max_value=50.0,value=3.0)

model_names = ['Multiple Regression','Polynomial Regression','Decision Tree','Random Forest','SVR','Polynomial Regression']
selected_model = st.selectbox('Select Model',model_names)

predict_button = st.button("Predict Air Quality")

if predict_button:
    user_data = {"PM2.5":pm2_5,"PM10":pm10,"NO":17.574730,"NO2":28.568659,"NOx":32.309123,
                 "NH3":23.483476,"CO":2.248598,"SO2":14.531977,"O3":34.491430,"Benzene":3.280840,
                 "Toluene":8.700972,"Xylene":166.463581}
    
    #Create a DataFrame for the User Data 
    user_df = pd.DataFrame([user_data])

    #Load the OneHotEncoder
    ohe= pickle.load(open(r"C:/Users/pc/Desktop/AQI Project/Models/OneHotEncoder_Featureset.pkl","rb"))
    
    #Transform the user data(assuming the first column is "State")
    try:
        x_new1=pd.DataFrame(ohe.transform([[selected_city]]).toarray())
    except Exception as e:
        print("Error during OneHotEncoder transformation:",e)
    feature_set = pd.concat([x_new1,user_df],axis = 1)
    feature_set = feature_set.iloc[:1,:].values
    
    #Make prediction based on Selected Model 
    if selected_model == "Multiple Regression":
        y_predict = make_prediction(mreg,feature_set)
    elif selected_model == " Polynomial Regression":
        y_predict = preg.predict(poly_reg.fit_transform(feature_set))
        y_predict=round(float(y_predict),2)
    elif selected_model == "Decision Tree":
        y_predict = make_prediction(dec_tree,feature_set)
    elif selected_model == "Random Forest":
        y_predict = make_prediction(rt_reg,feature_set)
    elif selected_model == "SVR":
        y_predict = make_prediction(svr_reg,feature_set)
    
    st.write(f"*The Predicted AQI  for{selected_city} is **{y_predict}**,*")