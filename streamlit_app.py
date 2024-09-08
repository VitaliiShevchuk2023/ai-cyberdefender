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
st.title("🎈 Home/Office Wi-Fi AI Cyberdefender")

# App description
st.write(
    "This app analyzes cyber data from Wi-Fi traffic"
)

# Path to the CSV file
csv_file_path = 'dataset/ssid_distribution.csv'
csv1_file_path = 'dataset/mac_address_traffic.csv'

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


# Check if the file exists
if os.path.exists(csv_file_path):
    # Read data from the CSV file
    df = pd.read_csv(csv1_file_path)

   
    # Check if the file contains the required columns
    if 'Source MAC' in df.columns and 'Destination MAC' in df.columns and 'Packet Count' in df.columns:
        
        # Create lists of nodes (MAC addresses) and edges
        nodes = {}
        edges = []

        for index, row in df.iterrows():
            source_mac = row['Source MAC']
            dest_mac = row['Destination MAC']
            packet_count = row['Packet Count']
            
            # Add nodes (source and destination MAC addresses)
            if source_mac not in nodes:
                nodes[source_mac] = Node(id=source_mac, label=source_mac, size=10)
            if dest_mac not in nodes:
                nodes[dest_mac] = Node(id=dest_mac, label=dest_mac, size=10)
                
            # Add edges between nodes
            edges.append(Edge(source=source_mac, target=dest_mac, label=str(packet_count)))

        # Graph configuration
        config = Config(width=800, height=600, directed=True, nodeHighlightBehavior=True, 
                        highlightColor="#F7A7A6", collapsible=True, node_size=20)
        
        # Visualize the graph
        st.write("Graph of MAC Address Relationships:")
        agraph(list(nodes.values()), edges, config)
    
    else:
        st.error("The file does not contain the required columns: 'Source MAC', 'Destination MAC', and 'Packet Count'.")
else:
    st.error("File mac_address_traffic.csv not found in the dataset folder.")