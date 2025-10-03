import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

#Load the dataset 

data=pd.read_csv("AQI Project/Dataset for AQI/city_day.csv")

#Set page title 
st.set_page_config(page_title='Air Quality Dashboard')

#Introduction
st.title("Air Quality dashboard")
st.write("""Visualizing Air Pollution level in Indian Cities""")

#Data Cleaning and Preprocessing 
data['Date']=pd.to_datetime(data['Date'])
data.dropna(subset=['AQI'],inplace=True)

#sidebar option 
st.sidebar.title('Study the AQI Patterns')
display_aqi_by_city =st.sidebar.checkbox("AQI by City")
display_aqi_by_year =st.sidebar.checkbox("AQI by Year")
display_aqi_by_bucket =st.sidebar.checkbox("AQI by AQI_Buckets")
display_pollutants_over_time = st.sidebar.checkbox("Pollutants Over time",value = True)

#AQI by cities
if display_aqi_by_city:
    st.subheader('AQI by City')
    cities = data['City'].unique()
    selected_city= st.selectbox("Select a City",cities)
    city_data = data[data['City']==selected_city]
    
    fig_aqi_city,ax_aqi_city = plt.subplots()
    sns.barplot(x=city_data['Date'].dt.year,y=city_data['AQI'],ax=ax_aqi_city)
    ax_aqi_city.set_xlabel('Year')
    ax_aqi_city.set_ylabel('Average AQI')
    ax_aqi_city.set_title(f'AQI Trend for {selected_city}')
    sns.despine(fig=fig_aqi_city)
    st.pyplot(fig_aqi_city)
    
    st.write('Observations: ')
    st.write('The graph shows the average AQI trend for the selected city over the years')
    st.write('Higher AQI value indicates the worst Air Quality')
    st.write('Te trend can help identify if air quality has improved or deteriorated over time in the selected city')
      
#AQI by Year
if display_aqi_by_year:
    st.subheader('AQI by Year')
    years=data['Date'].dt.year.unique()
    selected_year = st.selectbox("Select a Year",years)
    year_data = data[data['Date'].dt.year == selected_year]
    
    fig_aqi_year,ax_aqi_year = plt.subplots()
    sns.barplot(x=year_data['City'],y=year_data['AQI'],ax=ax_aqi_year)
    ax_aqi_year.set_xlabel('City')
    ax_aqi_year.set_ylabel('Average AQI')
    ax_aqi_year.set_title(f'AQI by city for {selected_year}')
    sns.despine(fig=fig_aqi_year)
    st.pyplot(fig_aqi_year)
    
    st.write('Observation')
    st.write('The graph shows the average AQI for different cities in the selected year')
    st.write('It allows comparing the Air quality across cities for specific year')
    st.write('Cities with higher bars have worse Air Quality compared to thosed wit lower bars')
    
 #AQI for bucket
if display_aqi_by_bucket:
    st.subheader('AQI by AQI_Bucket')
    aqi_buckets = data['AQI_Bucket'].unique()
    
    fig_aqi_bucket,ax_aqi_bucket = plt.subplots()
    sns.countplot(x=data['AQI_Bucket'],ax=ax_aqi_bucket)
    ax_aqi_bucket.set_xlabel('AQI_Bucket')
    ax_aqi_bucket.set_ylabel('Count')
    plt.xticks(rotation=45)
    sns.despine(fig=fig_aqi_bucket)
    st.pyplot(fig_aqi_bucket)
    
    st.write('Observation')
    st.write('The graph shows the count of AQI values falling into each AQI_Buckets ')
    st.write('It provides the overview of the distribution of AQI values across diffrent buckets')
    st.write('Higher counts in the "Poor" or "Very Poor" buckets indicate a higher frequency or por air qualtiy.')
    
    
#Pollutants over time
if display_pollutants_over_time:
    st.subheader('Pollutants over time') 
    pollutants=['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']
    selected_pollutants = st.multiselect("Select Pollutants",pollutants,default=['PM2.5','PM10'])
    
    cities=data['City'].unique()
    selected_city=st.selectbox("Select a City",cities,key='pollutant_city') 
    city_data = data[data['City']==selected_city]
    
    fig_pollutants,ax_pollutants=plt.subplots(figsize=(10,6))
    for pollutant in selected_pollutants:
        sns.lineplot(x=city_data['Date'],y=city_data[pollutant],label=pollutant,ax=ax_pollutants)
    ax_pollutants.set_xlabel('Date')
    ax_pollutants.set_ylabel('Pollutant Level')
    ax_pollutants.set_title(f'Pollutant over time for  {selected_city}')
    ax_pollutants.legend()
    sns.despine(fig=fig_pollutants)
    st.pyplot(fig_pollutants)             
    
    
    st.write('Observation')
    st.write('The graph shows the level of selected Pollutantss over time for the selected city ')
    st.write('It allows monitoring the trends and patterns of Pollutants levels')
    st.write('Higher Pollutant level indicates the worst quality of Air.')

    st.write('The Graph help identify any seasonal or long term variations in pollutant level.')
