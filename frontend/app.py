import streamlit as st
import requests
import pandas as pd
import time
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Shield.OS - Fraud Detection", layout="wide", initial_sidebar_state="expanded")
st.title("🛡️ Shield.OS – Fraud Detection System")

API_URL = "http://127.0.0.1:8000"

# Sidebar for model selection
st.sidebar.header("Configuration")
default_model = st.sidebar.selectbox("Default Model", ["xgboost", "logistic"])

# Initialize session state for live stream
if 'transactions' not in st.session_state:
    st.session_state.transactions = []
if 'stream_active' not in st.session_state:
    st.session_state.stream_active = False

# Create tabs
tab1, tab2, tab3 = st.tabs(["Single Prediction", "Live Stream Simulator", "Batch CSV Audit"])

# ============ TAB 1: Single Prediction ============
with tab1:
    st.subheader("Single Transaction Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        amount = st.number_input("Transaction Amount ($)", value=50.0, min_value=0.0)
        distance = st.number_input("Distance From Home (km)", value=0.0, min_value=0.0)
        time_elapsed = st.number_input("Time Elapsed (seconds)", value=3600, min_value=0)
    
    with col2:
        model_choice = st.selectbox("Model", ["xgboost", "logistic"], key="single_model")
        
        if st.button("Load Sample Fraud Transaction"):
            st.session_state.sample_loaded = True
    
    # Load sample if button clicked
    if st.session_state.get('sample_loaded', False):
        amount = 2500.0
        distance = 500.0
        time_elapsed = 86400
        st.success("Sample fraud transaction loaded!")
        st.info("High-risk parameters: Large amount ($2500), Far distance (500km), Late night transaction")
    
    if st.button("Predict", key="predict_single"):
        try:
            payload = {
                "Amount": amount,
                "Time": time_elapsed,
                "Distance_From_Home": distance,
                "selected_model": model_choice,
            }
            
            response = requests.post(f"{API_URL}/predict/single", json=payload, timeout=5)
            
            if response.status_code == 200:
                result = response.json()
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Fraud Probability", f"{result['fraud_probability']:.2%}")
                with col2:
                    st.metric("Status", result['status'], delta_color="inverse")
                with col3:
                    st.metric("Classification", "🚨 FRAUD" if result['is_fraud'] else "✓ LEGITIMATE")
                
                if result['is_fraud']:
                    st.warning(f"⚠️ Transaction FLAGGED with {result['fraud_probability']:.2%} fraud probability")
                else:
                    st.success(f"✓ Transaction CLEARED with {result['fraud_probability']:.2%} fraud probability")
            else:
                st.error(f"API Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {str(e)}")

# ============ TAB 2: Live Stream Simulator ============
with tab2:
    st.subheader("Live Transaction Stream")
    
    col1, col2 = st.columns([1, 4])
    
    with col1:
        stream_duration = st.number_input("Duration (seconds)", value=30, min_value=5, max_value=300)
        start_stream = st.button("Start Stream")
    
    with col2:
        if start_stream:
            st.session_state.stream_active = True
            st.session_state.transactions = []
    
    # Placeholder for metrics and table
    metrics_placeholder = st.empty()
    table_placeholder = st.empty()
    
    if st.session_state.stream_active:
        start_time = time.time()
        elapsed = 0
        
        while elapsed < stream_duration:
            # Generate random transaction
            amount = np.random.exponential(100)
            distance = np.random.uniform(0, 1000)
            time_of_day = np.random.uniform(0, 86400)
            
            try:
                payload = {
                    "Amount": float(amount),
                    "Time": float(time_of_day),
                    "Distance_From_Home": float(distance),
                    "selected_model": default_model,
                }
                
                response = requests.post(f"{API_URL}/predict/single", json=payload, timeout=5)
                
                if response.status_code == 200:
                    result = response.json()
                    transaction = {
                        "Timestamp": datetime.now().strftime("%H:%M:%S"),
                        "Amount": f"${amount:.2f}",
                        "Distance (km)": f"{distance:.1f}",
                        "Probability": f"{result['fraud_probability']:.2%}",
                        "Status": result['status'],
                    }
                    st.session_state.transactions.append(transaction)
            
            except:
                pass
            
            # Display metrics
            if st.session_state.transactions:
                df_transactions = pd.DataFrame(st.session_state.transactions)
                flagged = len([t for t in st.session_state.transactions if t['Status'] == 'FLAGGED'])
                
                with metrics_placeholder.container():
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Total Transactions", len(st.session_state.transactions))
                    m2.metric("Flagged", flagged)
                    m3.metric("Flagged %", f"{flagged/len(st.session_state.transactions)*100:.1f}%")
                
                with table_placeholder.container():
                    st.dataframe(df_transactions, use_container_width=True)
            
            elapsed = time.time() - start_time
            time.sleep(1)
        
        st.session_state.stream_active = False
        st.success(f"Stream completed! Processed {len(st.session_state.transactions)} transactions")

# ============ TAB 3: Batch CSV Audit ============
with tab3:
    st.subheader("Batch CSV Fraud Audit")
    
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    if uploaded_file is not None:
        if st.button("Analyze Batch", key="analyze_batch"):
            try:
                # Read CSV
                df = pd.read_csv(uploaded_file)
                
                # Send to API
                files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
                response = requests.post(f"{API_URL}/predict/batch", files=files, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Total Transactions", result['total_transactions'])
                    col2.metric("Flagged Transactions", result['flagged_count'])
                    col3.metric("Flagged Amount", f"${result['flagged_amount']:.2f}")
                    
                    # Calculate and display flagged percentage
                    if result['total_transactions'] > 0:
                        flagged_pct = (result['flagged_count'] / result['total_transactions']) * 100
                        st.info(f"Fraud Detection Rate: {flagged_pct:.2f}%")
                    
                    # Show preview of data
                    st.subheader("Dataset Preview")
                    st.dataframe(df.head(10), use_container_width=True)
                    
                else:
                    st.error(f"API Error: {response.status_code}")
            
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")

# Footer
st.divider()
st.caption("Shield.OS v1.0 | Fraud Detection System | Powered by FastAPI & Streamlit")
