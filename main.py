import pandas as pd
import streamlit as st
import data_scraper

with open('dates.txt', 'r') as file:
    dates = file.readlines()

dates = [date.strip() for date in dates]

with open('wind_speed_gust.txt', 'r') as file:
    data = file.readlines()

with open('angles.txt', 'r') as file:
    angles = file.readlines()

with open('temp.txt', 'r') as file:
    temp = file.readlines()

angles_values = []
temp_values = []
for i in angles:
    angles_values.append(i)
for i in temp:
    temp_values.append(i + "°")

speed_values=(data[0].split(" "))
gust_values=(data[1].split(" "))
if len(dates) > len(speed_values):
    dates = dates[:len(speed_values)]
elif len(dates) < len(speed_values):
    dates += [''] * (len(speed_values) - len(dates))
if len(angles_values) > len(speed_values):
    angles_values = angles_values[:len(speed_values)]
elif len(angles_values) < len(speed_values):
    angles_values += [''] * (len(speed_values) - len(angles_values))
if len(temp_values) > len(speed_values):
    temp_values = temp_values[:len(speed_values)]
elif len(temp_values) < len(speed_values):
    temp_values += [''] * (len(speed_values) - len(temp_values))
if len(gust_values) > len(speed_values):
    gust_values = gust_values[:len(speed_values)]
elif len(gust_values) < len(speed_values):
    gust_values += [''] * (len(speed_values) - len(gust_values))

def main():
    st.title("Thor Wind Website")
    with st.spinner("Loading data..."):
        import data_scraper

    df = pd.DataFrame({
        'Date': dates,
        'Speed': speed_values,
        'Gust': gust_values,
        'Angle': angles_values,
        'Temperature': temp_values
    })

    st.table(df)
if __name__ == "__main__":
    main()