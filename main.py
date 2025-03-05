import streamlit as st
import random
import string

st.set_page_config(page_title="Password Tool", layout="centered")

# Function to check password strength
def check_strength(password):
    if not password:
        return "Please enter a password", 0
    length = len(password)
    if length < 6:
        return "Very Weak", 20
    elif length < 8:
        return "Weak", 40
    elif length < 12:
        return "Medium", 60
    elif length < 16:
        return "Strong", 80
    else:
        return "Very Strong", 100

# Function to generate a password
def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

st.title("🔑 Password Tool")
st.write("Check password strength & generate a secure password.")

st.subheader("🔍 Check Password Strength")
password = st.text_input("Enter a password:", type="password")
message, strength = check_strength(password)
st.progress(strength / 100)
st.write(f"**Strength:** {message}")

st.subheader("⚡ Generate Password")
length = st.slider("Choose password length:", 6, 20, 12)
if st.button("Generate Password"):
    new_password = generate_password(length)
    st.text_input("Generated Password:", new_password)

st.subheader("🔒 Tips for a Strong Password")
st.write("- Use at least **12 characters**")
st.write("- Mix **uppercase, lowercase, numbers, and symbols**")
st.write("- **Avoid common words** and personal info")
st.write("✅ **Simple & Easy to Understand!**")
