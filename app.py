import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NTPC CSR Admit Card", page_icon="📄")

st.title("NTPC CSR Entrance Examination 2026")
st.subheader("Download Your Admit Card")

# Load Excel
@st.cache_data
def load_data():
    return pd.read_excel("admission data spreadsheet.xlsx")

df = load_data()

phone = st.text_input("Enter Mobile Number")

if st.button("Get Admit Card"):

    if phone == "":
        st.warning("Please enter Mobile Number")

    else:
        try:
            phone = int(phone)

            student = df[
                (df["Candidate Mobile No"] == phone)
            ]

            if not student.empty:

                st.success("Student Verified ✅")

                # Roll number get from excel
                roll = student.iloc[0]["ROLL NO"]

                folder = "New folder"
                file_found = None

                # Search admit card by roll number
                for file in os.listdir(folder):
                    if file.startswith(str(roll)):
                        file_found = os.path.join(folder, file)
                        break

                if file_found:

                    with open(file_found, "rb") as f:
                        img_data = f.read()

                    # Show image preview
                    st.image(file_found, caption="Admit Card", use_container_width=True)

                    # Download button
                    st.download_button(
                        label="Download Admit Card",
                        data=img_data,
                        file_name=file,
                        mime="image/png"
                    )

                else:
                    st.error("Admit Card file not found")

            else:
                st.error("Mobile Number not found")

        except:
            st.error("Please enter valid Mobile Number")
