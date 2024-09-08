import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_agraph import agraph, Node, Edge, Config
from streamlit_agraph import TripleStore
#from streamlit_agraph import Node, Edg
#from streamlit_agraph import agraph, Node, Edge, Config
#from streamlit_agraph import agraph, Node, Edge, Config


# App title
st.title("🎈 Home Wi-Fi AI Cyberdefender")

# App description
st.write(
    "This app analyzes cyber data from Wi-Fi traffic"
)

# Path to the CSV file
csv_file_path = 'dataset/ssid_distribution.csv'
#csv1_file_path = 'dataset/mac_address_traffic.csv'
csv1_file_path = 'dataset/processed_data.csv'

# Check if the file exists
if os.path.exists(csv_file_path):
    # Read the data from the CSV file
    df = pd.read_csv(csv_file_path)
 

    # Check if the file has the required columns
    if 'SSID' in df.columns and 'Count' in df.columns:
        # Plot SSID distribution chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['SSID'], df['Count'], color='skyblue')
        ax.set_xlabel('SSID')
        ax.set_ylabel('Count')
        ax.set_title('SSID Distribution in Wi-Fi Networks')
        plt.xticks(rotation=90)
        plt.tight_layout()

        # Display the chart
        st.pyplot(fig)
    else:
        st.error("The file does not contain the required columns 'SSID' and 'Count'.")
else:
    st.error("File ssid_distribution.csv not found in the dataset directory.")


# Check if the CSV file exists and load data
if pd.io.common.file_exists(csv1_file_path):
    # Load data from CSV file
    df = pd.read_csv(csv1_file_path)

    
    # Define the function to visualize anomalies
    def visualize_anomalies(df):
        if df.empty:
            st.write("No data to visualize.")
            return
        
        # Create the scatter plot
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Distribution of packet lengths
        normal = df[df['Anomaly'] == 'Normal']
        anomaly = df[df['Anomaly'] == 'Anomaly']
        
        ax.scatter(normal.index, normal['Length'], label='Normal', color='blue', alpha=0.5, s=10)
        ax.scatter(anomaly.index, anomaly['Length'], label='Anomaly', color='red', alpha=0.5, s=10)
        
        ax.set_xlabel('Packet Index')
        ax.set_ylabel('Packet Length')
        ax.set_title('Anomaly Detection in Packet Length Across All Files')
        ax.legend()
        
        # Show the plot
        st.pyplot(fig)
    
    # Visualize anomalies
    visualize_anomalies(df)
else:
    st.error("File processed_data.csv not found in the dataset folder.")