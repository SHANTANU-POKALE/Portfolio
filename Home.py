import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Shantanu Pokale")
    content = """
    Hi, I am Shantanu! A diligent student pursuing a B.E. in Electronics & Telecommunication Engineering at PRMIT&R,
Amravati, with notable achievements in artificial intelligence and web development. Certified in Artificial
Intelligence from 1Stop in collaboration with IIT Roorkee, showcasing expertise in Python, VLSI, and
Verilog. Experienced in internships as a Frontend Web Developer and an Artificial Intelligence Intern,
excelling in projects like Capsule Network for MNIST Classification and GAN-based anime character
generation and Automated Interaction Script for App Using Appium. Proficient in a wide array of programming languages, 
soft skills, and cross-functional domains,
with a keen interest in next-generation technologies like AI,IOT and prompt engineering.
    """
    st.info(content)

content2 = """
Below  you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
