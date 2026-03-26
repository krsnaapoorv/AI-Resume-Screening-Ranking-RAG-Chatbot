import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🤖 AI Resume Screening System")

# -------------------------------
# 🔐 Login Section
# -------------------------------
st.header("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    res = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email, "password": password}
    )

    if res.status_code == 200:
        token = res.json()["access_token"]
        st.session_state["token"] = token
        st.success("Logged in successfully!")
    else:
        st.error("Login failed")

# -------------------------------
# 📤 Upload Resume
# -------------------------------
st.header("Upload Resume")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file and st.button("Upload"):
    headers = {
        "Authorization": f"Bearer {st.session_state.get('token')}"
    }

    files = {"file": uploaded_file}

    res = requests.post(
        f"{BASE_URL}/resume/upload",
        headers=headers,
        files=files
    )

    if res.status_code == 200:
        st.success("Resume uploaded!")
        st.json(res.json())
    else:
        st.error("Upload failed")

# -------------------------------
# 📊 Ranking
# -------------------------------
st.header("Rank Candidates")

jd = st.text_area("Enter Job Description")

if st.button("Rank"):
    res = requests.post(
        f"{BASE_URL}/ranking/",
        params={"job_description": jd}
    )

    if res.status_code == 200:
        results = res.json()["ranked_candidates"]

        for r in results:
            st.write(f"Resume ID: {r['resume_id']} → Score: {r['score']:.2f}")
    else:
        st.error("Ranking failed")

# -------------------------------
# 💬 Chat with Resume (RAG)
# -------------------------------
st.header("Chat with Resume")

query = st.text_input("Ask something about resume")

if st.button("Ask"):
    res = requests.post(
        f"{BASE_URL}/chat/",
        params={"query": query}
    )

    if res.status_code == 200:
        st.write(res.json()["answer"])
    else:
        st.error("Chat failed")