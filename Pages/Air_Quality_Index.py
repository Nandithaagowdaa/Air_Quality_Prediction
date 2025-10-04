import streamlit as st 
st.set_page_config(page_title="Air Qualtiy Index:")
st.header('AirWatch India')

st.image("download.png")

st.markdown("""
This app shows you the air pollution levels in Indian Cities.  
It tracks NO2, CO, AQI, PM2.5, PM10, and more.  
You'll see pollution trends and get health recommendations.
""")

# Impact on Health and Wellbeing
st.header('Impact on Health and Wellbeing')

st.markdown("""
**Respiratory health:** Poor air quality worsens asthma, bronchitis, and other lung diseases, and lowers lung function.  

**Heart and circulation:** Pollutants like PM2.5 increase the risk of heart attacks, strokes, and high blood pressure.  

**Brain and mental health:** Air pollution is linked to memory problems, dementia, stress, anxiety, and depression.  
""")
 
#Impact on Life Expectancy 
st.header('Impact on Life Expectancy')
 
st.markdown(
             """
             Poor air quality significantly reduces human life expectancy. Long-term exposure to pollutants such as fine particulate matter (PM2.5), nitrogen dioxide (NO₂), ozone (O₃), and sulfur dioxide (SO₂) damages the lungs, heart, and blood vessels, leading to chronic diseases. Studies show that living in polluted environments can shorten life by 2–5 years on average, depending on the severity of exposure.
             Air pollution increases the risk of heart attacks, strokes, lung cancer, and chronic respiratory diseases, which are leading causes of premature death. Children growing up in polluted areas often have reduced lung development, and older adults face worsened health conditions. The World Health Organization (WHO) estimates that millions of premature deaths occur each year due to air pollution, making it one of the greatest environmental threats to human longevity.
             On the other hand, improving air quality by reducing emissions, promoting clean energy, and controlling traffic pollution has been shown to increase average life expectancy, improve public health, and reduce healthcare costs.
             """)
 
#Conclusion
st.header("Conclusion")
 
st.markdown(
             """
             Our Health ratio is directly dependent on the Air Qualtiy 
             """

)
