import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NTPC CSR Admit Card", page_icon="📄")

st.title("NTPC CSR Entrance Examination 2026")
st.subheader("Download Your Admit Card")

# Load Excel
df = pd.read_excel("admission data spreadsheet.xlsx")

roll = st.text_input("Enter Roll Number")
phone = st.text_input("Enter Mobile Number")

if st.button("Get Admit Card"):

    if roll == "" or phone == "":
        st.warning("Please enter both Roll Number and Mobile Number")

    else:
        try:
            roll = int(roll)
            phone = int(phone)

            student = df[
                (df["ROLL NO"] == roll) &
                (df["Candidate Mobile No"] == phone)
            ]

            if not student.empty:

                st.success("Student Verified ✅")

                folder = "New folder"
                file_found = None

                for file in os.listdir(folder):
                    if file.startswith(str(roll)):
                        file_found = os.path.join(folder, file)
                        break

                if file_found:
                    with open(file_found, "rb") as f:
                        st.download_button(
                            label="Download Admit Card",
                            data=f,
                            file_name=file,
                            mime="application/pdf"
                        )
                else:
                    st.error("Admit Card file not found")

            else:
                st.error("Invalid Roll Number or Mobile Number")

        except:
            st.error("Please enter valid numbers")
