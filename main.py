import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

layoffs_df = pd.read_csv("layoffs.csv")




#############################





# Set Streamlit page configuration
st.set_page_config(page_title='Layoffs Dataset EDA', layout='wide')
st.sidebar.image("toxic-boss-shouting-on-employee-8269479-6605156.webp")

# Load the dataset
layoffs_file_path = 'layoffs.csv'  # Update this path if necessary
layoffs_df = pd.read_csv(layoffs_file_path)

# Handling missing values
layoffs_df['location'].fillna('Unknown', inplace=True)
layoffs_df['industry'].fillna('Unknown', inplace=True)
layoffs_df['total_laid_off'].fillna(0, inplace=True)
layoffs_df['percentage_laid_off'].fillna(0, inplace=True)
layoffs_df['stage'].fillna('Unknown', inplace=True)
layoffs_df['funds_raised'].fillna(0, inplace=True)

# Convert 'date' to datetime
layoffs_df['date'] = pd.to_datetime(layoffs_df['date'])

# Title
st.title('Layoffs Dataset EDA')

# Sidebar for user interaction
st.sidebar.title('Select Analysis')

# Button options
options = [
    "Basic Information", 
    "Summary Statistics", 
    "Missing Values", 
    "Distribution of Numerical Features", 
    "Correlation Matrix", 
    "Time Series Plots", 
    "Scatter Plot Matrix", 
    "Categorical Analysis", 
    "Boxplots by Country and Industry", 
    "Trend Analysis Over Time", 
    "Top Companies by Total Layoffs", 
    "Top Industries by Total Layoffs", 
    "Top Countries by Total Layoffs", 
    "Distribution by Stage", 
    "Layoffs Percentage by Industry", 
    "Layoffs Percentage by Country", 
    "Funds Raised by Industry", 
    "Funds Raised by Country", 
    "Time Series Analysis by Industry", 
    "Time Series Analysis by Country"
]

# User selection
selected_option = st.sidebar.selectbox("Choose Analysis Type", options)

# Display selected analysis
if selected_option == "Basic Information":
    st.header("Basic Information")
    buffer = st.text("")
    buffer.write(layoffs_df.info())

elif selected_option == "Summary Statistics":
    st.header("Summary Statistics")
    st.write(layoffs_df.describe(include='all'))

elif selected_option == "Missing Values":
    st.header("Missing Values")
    st.write(layoffs_df.isnull().sum())

elif selected_option == "Distribution of Numerical Features":
    st.header("Distribution of Numerical Features")
    numerical_features = ['total_laid_off', 'percentage_laid_off', 'funds_raised']
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    layoffs_df[numerical_features].hist(bins=15, ax=axes)
    plt.tight_layout()
    st.pyplot(fig)

elif selected_option == "Correlation Matrix":
    st.header("Correlation Matrix")
    correlation_matrix = layoffs_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    st.pyplot(fig)

elif selected_option == "Time Series Plots":
    st.header("Time Series Plots")
    layoffs_df.set_index('date', inplace=True)
    fig, axes = plt.subplots(3, 1, figsize=(12, 18), sharex=True)
    layoffs_df[['total_laid_off', 'percentage_laid_off', 'funds_raised']].plot(subplots=True, ax=axes)
    plt.tight_layout()
    st.pyplot(fig)
    layoffs_df.reset_index(inplace=True)

elif selected_option == "Scatter Plot Matrix":
    st.header("Scatter Plot Matrix")
    numerical_features = ['total_laid_off', 'percentage_laid_off', 'funds_raised']
    fig = sns.pairplot(layoffs_df[numerical_features].dropna())
    st.pyplot(fig)

elif selected_option == "Categorical Analysis":
    st.header("Categorical Analysis")
    categorical_features = ['company', 'location', 'industry', 'stage', 'country']
    for feature in categorical_features:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(y=feature, data=layoffs_df, order=layoffs_df[feature].value_counts().index, ax=ax)
        st.pyplot(fig)

elif selected_option == "Boxplots by Country and Industry":
    st.header("Boxplots by Country and Industry")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='country', y='total_laid_off', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='industry', y='total_laid_off', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected_option == "Trend Analysis Over Time":
    st.header("Trend Analysis Over Time")
    layoffs_df_monthly = layoffs_df.resample('M', on='date').sum()
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    layoffs_df_monthly[['total_laid_off', 'percentage_laid_off']].plot(subplots=True, ax=axes)
    plt.tight_layout()
    st.pyplot(fig)

elif selected_option == "Top Companies by Total Layoffs":
    st.header("Top Companies by Total Layoffs")
    top_companies = layoffs_df.groupby('company')['total_laid_off'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=top_companies.values, y=top_companies.index, ax=ax)
    st.pyplot(fig)

elif selected_option == "Top Industries by Total Layoffs":
    st.header("Top Industries by Total Layoffs")
    top_industries = layoffs_df.groupby('industry')['total_laid_off'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=top_industries.values, y=top_industries.index, ax=ax)
    st.pyplot(fig)

elif selected_option == "Top Countries by Total Layoffs":
    st.header("Top Countries by Total Layoffs")
    top_countries = layoffs_df.groupby('country')['total_laid_off'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax)
    st.pyplot(fig)

elif selected_option == "Distribution by Stage":
    st.header("Distribution by Stage")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='stage', y='total_laid_off', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected_option == "Layoffs Percentage by Industry":
    st.header("Layoffs Percentage by Industry")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='industry', y='percentage_laid_off', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected_option == "Layoffs Percentage by Country":
    st.header("Layoffs Percentage by Country")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='country', y='percentage_laid_off', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected_option == "Funds Raised by Industry":
    st.header("Funds Raised by Industry")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='industry', y='funds_raised', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected_option == "Funds Raised by Country":
    st.header("Funds Raised by Country")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='country', y='funds_raised', data=layoffs_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected_option == "Time Series Analysis by Industry":
    st.header("Time Series Analysis by Industry")
    fig, ax = plt.subplots(figsize=(12, 8))
    for industry in layoffs_df['industry'].unique():
        industry_data = layoffs_df[layoffs_df['industry'] == industry].resample('M', on='date').sum()
        ax.plot(industry_data.index, industry_data['total_laid_off'], label=industry)
    ax.legend()
    st.pyplot(fig)

elif selected_option == "Time Series Analysis by Country":
    st.header("Time Series Analysis by Country")
    fig, ax = plt.subplots(figsize=(12, 8))
    for country in layoffs_df['country'].unique():
        country_data = layoffs_df[layoffs_df['country'] == country].resample('M', on='date').sum()
        ax.plot(country_data.index, country_data['total_laid_off'], label=country)
    ax.legend()
    st.pyplot(fig)

# Show selected analysis
st.write(f"Selected analysis: {selected_option}")

