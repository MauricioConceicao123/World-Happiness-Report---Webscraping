import streamlit as st
import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
st.set_page_config(
    page_title="Project Web Scraping",
    page_icon=":tada:",
    layout="wide",
)
#st.title("Evolution of World Happiness")
#st.write("In this project we want to analyze the **World Happiness** in the last years and try to understand what contribute to the results")
st.sidebar.header("World Happiness Analysis")
#st.sidebar.slider('Select the Year', 2015, 2021)
#################
#dataset will come here:
df2019 = pd.read_csv("https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2019.csv")
df2018 = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2018.csv')
#################
choice = st.sidebar.radio("Select the Topic", ('Overall Happiness','Happiness by Region','Wealth Potential','Social Support','Correlations'))
if choice == 'Overall Happiness':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Happiness by Region':
    st.header("World Happiness Analysis 2019")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Wealth Potential':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Social Support':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            df2018.sort_values('Social support', ascending=False, inplace=True)
            socialsuport=df2018.head(10)
            fig, ax=plt.subplots(figsize=(8,5))
            viz1=sns.barplot(socialsuport, x='Country or region', y='Social support', palette="ch:s=.25,rot=-.25", ax=ax)
            ax.bar_label(ax.containers[0])
            ax.set_xticklabels(socialsuport['Country or region'], rotation=45)
            ax.set(title="Top 10 Country with the Best Social Support in 2018")
            ax.set_xlabel('')
            ax.set_ylabel('Rate Social Support')
            ax.set_ylim(bottom=1.4)
            st.pyplot(viz1.figure)
        with col2:
            st.write("here column 2")
            df2019.sort_values('Social support', ascending=False, inplace=True)
            ss2019=df2019.head(10)
            fig, ax=plt.subplots(figsize=(8,5))
            viz2=sns.barplot(ss2019, x='Country or region', y='Social support', palette="flare", ax=ax)
            ax.bar_label(ax.containers[0])
            ax.set_xticklabels(ss2019['Country or region'], rotation=45)
            ax.set(title="Top 10 Country with the Best Social Support in 2019")
            ax.set_xlabel('')
            ax.set_ylabel('Rate Social Support')
            ax.set_ylim(bottom=1.4)
            st.pyplot(viz2.figure)
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            df2018.sort_values('GDP per capita', ascending=False, inplace=True)
            gdp2018=df2018.head(10)
            fig, ax1=plt.subplots(figsize=(8,5))
            viz3=sns.barplot(gdp2018, x='Country or region', y='GDP per capita', palette="ch:s=.25,rot=-.25", ax=ax1)
            ax1.bar_label(ax1.containers[0])
            ax1.set_xticklabels(gdp2018['Country or region'], rotation=45)
            ax1.set(title="Top 10 Country with the Best Values of GDP per Capita in 2018")
            ax1.set_xlabel('')
            st.pyplot(viz3.figure)
        with col2:
            st.write("here column 2")
            df2019.sort_values('GDP per capita', ascending=False, inplace=True)
            gdp2019=df2019.head(10)
            fig, ax4=plt.subplots(figsize=(8,5))
            viz4=sns.barplot(gdp2019, x='Country or region', y='GDP per capita', palette="flare", ax=ax4)
            ax4.bar_label(ax4.containers[0])
            ax4.set_xticklabels(gdp2019['Country or region'], rotation=45)
            ax4.set(title="Top 10 Country with the Best Values of GDP per Capita in 2019")
            ax4.set_xlabel('')
            st.pyplot(viz4.figure)
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Correlations':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()

