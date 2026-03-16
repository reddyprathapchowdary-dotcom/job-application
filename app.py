import streamlit as st

st.title("Job Application Form")

st.header("Applicant Details")

# Personal Details
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")

# Job Details
position = st.selectbox(
    "Position Applying For",
    ["Software Developer", "Data Analyst", "Web Developer", "UI/UX Designer"]
)

experience = st.slider("Years of Experience", 0, 10)

skills = st.multiselect(
    "Select Your Skills",
    ["Python", "Java", "SQL", "Machine Learning", "HTML", "CSS", "JavaScript"]
)

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

cover_letter = st.text_area("Cover Letter")

# Submit Button
if st.button("Submit Application"):
    st.success("Application Submitted Successfully!")

    st.subheader("Application Summary")
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Phone:", phone)
    st.write("Position:", position)
    st.write("Experience:", experience, "years")
    st.write("Skills:", skills)

    if resume:
        st.write("Resume Uploaded:", resume.name)