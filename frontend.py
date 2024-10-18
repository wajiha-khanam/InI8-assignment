import streamlit as st
import requests
import json


API_URL = 'http://127.0.0.1:5000'

# Streamlit App

st.title("Registration System")

# Section 1: Creating a New Registration
st.header("Create a New Registration")
name = st.text_input("Name")
email = st.text_input("Email")
dob = st.date_input("Date of Birth")
phone = st.text_input("Phone Number (optional)")
address = st.text_input("Address (optional)")

if st.button("Create Registration"):

    data = {
        "Name": name,
        "Email": email,
        "DateOfBirth": str(dob),
        "PhoneNumber": phone,
        "Address": address
    }

    # Making POST request to create registration
    response = requests.post(f'{API_URL}/register', json=data)

    if response.status_code == 201:
        st.success("Registration created successfully!")
    else:
        st.error(f"Failed to create registration: {response.text}")

# Section 2: View All Registrations
st.header("View All Registrations")

if st.button("Load Registrations"):
    response = requests.get(f'{API_URL}/registrations')

    if response.status_code == 200:
        registrations = response.json()

        for reg in registrations:
            st.write(f"**ID**: {reg['ID']}")
            st.write(f"**Name**: {reg['Name']}")
            st.write(f"**Email**: {reg['Email']}")
            st.write(f"**Date of Birth**: {reg['DateOfBirth']}")
            st.write(f"**Phone**: {reg.get('PhoneNumber', 'N/A')}")
            st.write(f"**Address**: {reg.get('Address', 'N/A')}")
            st.write("---")
    else:
        st.error(f"Failed to load registrations: {response.text}")

# Section 3: Update a Registration by ID
st.header("Update a Registration")

update_id = st.number_input("Enter the ID to Update", min_value=0, step=1)
new_name = st.text_input("New Name")
new_email = st.text_input("New Email")
new_dob = st.date_input("New Date of Birth")
new_phone = st.text_input("New Phone Number (optional)")
new_address = st.text_input("New Address (optional)")

if st.button("Update Registration"):

    update_data = {
        "Name": new_name,
        "Email": new_email,
        "DateOfBirth": str(new_dob),
        "PhoneNumber": new_phone,
        "Address": new_address
    }

    response = requests.put(f'{API_URL}/registrations/{update_id}', json=update_data)

    if response.status_code == 200:
        st.success("Registration updated successfully!")
    else:
        st.error(f"Failed to update registration: {response.text}")

# Section 4: Delete a Registration by ID
st.header("Delete a Registration")

delete_id = st.number_input("Enter the ID to Delete", min_value=0, step=1)

if st.button("Delete Registration"):
    response = requests.delete(f'{API_URL}/registrations/{delete_id}')

    if response.status_code == 200:
        st.success("Registration deleted successfully!")
    else:
        st.error(f"Failed to delete registration: {response.text}")
