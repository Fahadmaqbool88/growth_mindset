import streamlit as st
    st.set_page_config(page_title= "growth mindset project", project_icon="★")
    st.title("growth mindset challange: web app with streamlit  ")
    st.header("welcome to your growth journey")
    st.write("embrace challange, learn from mistakes, and unlock your full potential. this AI-powerd app help")
    st.header("today' growth mindset quote ")
    st.write("success is not final failure is not fatal: it is the courage to continue that counts.- winston churchil")

    st.header("what's your challange today?")
    user_input = st.text_input("describe the challange you are facing")
if user_input:
    st.success(f"you are facing: {user_input}.keep pushing forward towards your goal!")
else:
    st.warning("tell us about your challange to get started:")
    st.header("reflect on your learning")
    reflection = st.text_area("write your reflections here:")
if reflection:
    st.success(f"Great insight | your reflection: {reflection}")
else:

    st.info("reflecting on past experience help you grow! share your acheivment")
    st.header("celebrate your wins !")
    acheivment  = st.text_input("share something you have recently accomplished:")
if acheivment:
    st.success(f"amazing you acheived:{acheivment}")
else:
    st.info("big or small, every acheivment counts! share one now")
    st.write("- - -")
    st.write("keep believing in yourself . growth is a gourney, note a distination")
    st.write("""creat by Maqbool Ahmed""") 