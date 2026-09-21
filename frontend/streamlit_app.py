from __future__ import annotations

import requests
import streamlit as st

API_URL = "http://localhost:8001"

st.set_page_config(page_title="Insure Agent", page_icon="🛡️")
st.title("Insure Agent")
st.subheader("Preliminary underwriting assessment")

with st.form("customer_form"):
    customer_name = st.text_input("Customer name")
    age = st.number_input("Age", min_value=18, max_value=90, value=35)
    annual_income = st.number_input("Annual income", min_value=0.0, step=5000.0, value=85000.0)
    requested_coverage = st.number_input("Requested coverage", min_value=10000.0, step=25000.0, value=500000.0)
    smoking_status = st.selectbox("Smoking status", ["non-smoker", "smoker"])
    medical_disclosure = st.text_area("Medical disclosure", value="No major issues noted.")
    policy_type = st.selectbox("Policy type", ["auto", "home", "life"])
    submitted = st.form_submit_button("Run underwriting check")

if submitted:
    payload = {
        "customer": {
            "customer_name": customer_name,
            "age": int(age),
            "annual_income": float(annual_income),
            "requested_coverage": float(requested_coverage),
            "smoking_status": smoking_status,
            "medical_disclosure": medical_disclosure,
            "policy_type": policy_type,
        }
    }

    try:
        response = requests.post(f"{API_URL}/api/underwrite", json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        st.success("Assessment complete")
        st.metric("Risk Score", data["risk_score"])
        st.metric("Recommendation", data["recommendation"])
        st.write("### Key factors")
        for factor in data["key_factors"]:
            st.write(f"- {factor}")
        st.write("### Policy evidence")
        for item in data["policy_evidence"]:
            st.write(f"- {item}")
    except Exception as exc:
        st.error(f"Unable to reach the backend: {exc}")
        st.info("Start the API with: uvicorn app.main:app --reload")
