

import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import bcrypt
# Setup Google Sheets API
scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('cred.json', scopes=scopes)
gc = gspread.authorize(credentials)
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Open the Google Sheet
sh = gc.open_by_key("17KIBySu21Oh0ajtyo4A9jUTjnwOIl69KlqNlTfszrXQ")
worksheet = sh.sheet1

# Streamlit App
st.title('Data Entry Form')

# Create a form
with st.form(key='data_entry_form'):
    name = st.text_input('Name')
    password = st.text_input('Password')

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Store form data in Google Sheets
if submit_button:
    if name and password:
        # Prepare the row to be inserted
        password = hash_password(password).decode('utf-8')
        row_data = [name, password]
        
        # Append the data to the Google Sheet
        worksheet.append_row(row_data)
        
        st.success('Data has been submitted successfully!')
    else:
        st.error('Please fill in all the fields.')
