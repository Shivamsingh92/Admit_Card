import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NTPC CSR Admit Card Download")

st.title("NTPC CSR Entrance Examination 2026")
st.subheader("Download Admit Card")

# Load Excel
df = pd.read_excel("students.xlsx")

roll = st.text_input("Enter Roll Number")
phone = st.text_input("Enter Mobile Number")

if st.button("Download Admit Card"):

    if roll == "" or phone == "":
        st.warning("Please enter Roll Number and Mobile Number")

    else:
        student = df[(df["ROLL NO"] == int(roll)) & (df["Candidate Mobile No"] == int(phone))]

        if not student.empty:

            name = student.iloc[0]["Candidate Name"]
            filename = f"id_cards/{roll}_{name.replace(' ', '_')}_AdmitCard.pdf"

            if os.path.exists(filename):

                with open(filename, "rb") as file:
                    st.success("Admit Card Found")
                    st.download_button(
                        label="Download Admit Card",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="application/pdf"
                    )

            else:
                st.error("Admit Card file not found")

        else:
            st.error("Invalid Roll Number or Mobile Number")