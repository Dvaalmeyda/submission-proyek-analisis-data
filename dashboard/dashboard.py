import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style('dark')

# Load data
bike_rental_df = pd.read_csv('bike_rental.csv')
rfm_df = pd.read_csv('rfm_analysis.csv')

# Transform date columns
bike_rental_df['date'] = pd.to_datetime(bike_rental_df['date'])

# Sidebar
st.sidebar.title('Bike Rental Data Analysis')
st.sidebar.image('logo.png', width=250)
analysis_options = [
    'Total Rented Bikes by Season',
    'Total Rented Bikes by Holiday Status',
    'Total Rented Bikes by Weather Situation',
    'Total Customer (Casual and Registered)',
    'Monthly Total Rented Bikes Trend (2011-2012)',
    'RFM Analysis',
]

# Header
st.title('Bike Rental Data Analysis Dashboard - Dicoding')

analysis_choice = st.sidebar.selectbox('Select Analysis', analysis_options)

# Total Rented Bikes by Season
if analysis_choice == 'Total Rented Bikes by Season':
    st.header('Total Rented Bikes by Season')
    season_rented_bikes = bike_rental_df.groupby('season')['total_rented'].sum().reset_index()
    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=season_rented_bikes, x='season', y='total_rented', palette='coolwarm')

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)
        
    ax.set_title('Total Rented Bikes by Season')
    ax.set_ylabel('Total Rented Bikes')
    ax.set_xlabel('Season')
    st.pyplot(fig)

# Total Rented Bikes by Holiday Status
if analysis_choice == 'Total Rented Bikes by Holiday Status':
    st.header('Total Rented Bikes by Holiday Status')
    holiday_rented_bikes = bike_rental_df.groupby('is_holiday')['total_rented'].sum().reset_index()
    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=holiday_rented_bikes, x='is_holiday', y='total_rented', palette='coolwarm')

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)

    ax.set_title('Total Rented Bikes by Holiday Status')
    ax.set_ylabel('Total Rented Bikes')
    ax.set_xlabel('Holiday Status')
    ax.set_xticklabels(['No', 'Yes'])
    st.pyplot(fig)

# Total Rented Bikes by Weather Situation
if analysis_choice == 'Total Rented Bikes by Weather Situation':
    st.header('Total Rented Bikes by Weather Situation')
    weather_rented_bikes = bike_rental_df.groupby('weather_situation')['total_rented'].sum().reset_index()
    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=weather_rented_bikes, x='weather_situation', y='total_rented', palette='coolwarm')
    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)
    
    ax.set_title('Total Rented Bikes by Weather Situation')
    ax.set_ylabel('Total Rented Bikes')
    ax.set_xlabel('Weather Situation')
    st.pyplot(fig)

# Total Customer (Casual and Registered)
if analysis_choice == 'Total Customer (Casual and Registered)':
    # SUM of casual & registered
    casual_registered_total = bike_rental_df[['casual', 'registered']].sum().reset_index()
    casual_registered_total.rename(columns={'index': 'customer', 0: 'total_rented'}, inplace=True)

    st.header('Total Customer (Casual and Registered)')
    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=casual_registered_total, x='customer', y='total_rented', palette='Set1')

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)

    ax.set_title('Total Customer (Casual and Registered)')
    ax.set_ylabel('Total Rented Bikes')
    ax.set_xlabel('Customer Type')
    st.pyplot(fig)

# Monthly Total Rented Bikes Trend (2011-2012)
if analysis_choice == 'Monthly Total Rented Bikes Trend (2011-2012)':
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Juni', 'Juli', 'Agust', 'Sep', 'Okt', 'Nov', 'Des']

    year_month_total_rented = bike_rental_df.groupby(['year', 'month'])['total_rented'].sum().reset_index()
    year_month_total_rented['month'] = pd.Categorical(year_month_total_rented['month'], categories=month_order, ordered=True)

    st.header('Monthly Total Rented Bikes Trend (2011-2012)')
    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=year_month_total_rented, x='month', y='total_rented', hue='year', palette='muted', marker='o')
    ax.set_title('Monthly Total Rented Bikes Trend (2011-2012)')
    ax.set_ylabel('Total Rented Bikes')
    ax.set_xlabel('Month')
    st.pyplot(fig)

# RFM Analysis
if analysis_choice == 'RFM Analysis':
    st.header('RFM Analysis')
    st.dataframe(rfm_df)

    fig, ax = plt.subplots(1, 3, figsize=(18, 6))
    colors = ['#72BCD4']

    # Recency (5 lowest values)
    sns.barplot(y="recency", x="date", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel("Recency (Days)", fontsize=12)
    ax[0].set_xlabel("Month", fontsize=12)
    ax[0].set_title("Top 5 By Recency (Days)", loc="center", fontsize=16)
    ax[0].tick_params(axis='x', labelsize=12)

    # Frequency (5 highest values)
    sns.barplot(y="frequency", x="date", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel("Frequency", fontsize=12)
    ax[1].set_xlabel("Month", fontsize=12)
    ax[1].set_title("Top 5 By Frequency", loc="center", fontsize=16)
    ax[1].tick_params(axis='x', labelsize=12)
    
    # Monetary (5 highest values)
    sns.barplot(y="monetary", x="date", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
    ax[2].set_ylabel("Monetary Value", fontsize=12)
    ax[2].set_xlabel("Month", fontsize=12)
    ax[2].set_title("Top 5 By Monetary", loc="center", fontsize=16)
    ax[2].tick_params(axis='x', labelsize=12)

    plt.suptitle("Best Months Based on RFM Parameters", fontsize=20)
    st.pyplot(fig)

st.markdown(
    """
    <div style="text-align: center;">
        Copyright © 2024 | All rights reserved <a href="https://www.linkedin.com/in/divaalmeyda/" target="_blank">Diva Almeyda</a>
    </div>
    """,
    unsafe_allow_html=True
)