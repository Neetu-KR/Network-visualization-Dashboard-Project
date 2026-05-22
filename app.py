import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Network Visualization Dashboard",
    layout="wide"
)

# Title
st.title("🌐 Network Visualization Dashboard")
st.markdown("Interactive visualization of network connections")

# Load dataset
@st.cache_data

def load_data():
    df = pd.read_csv("data/sample_network.csv")
    return df


df = load_data()

# Show dataset
st.subheader("📄 Network Data")
st.dataframe(df)

# Create graph
G = nx.from_pandas_edgelist(df, source='source', target='target')

# Sidebar options
st.sidebar.title("Dashboard Controls")

layout_option = st.sidebar.selectbox(
    "Choose Layout",
    ["spring", "circular", "kamada_kawai"]
)

# Layout selection
if layout_option == "spring":
    pos = nx.spring_layout(G)
elif layout_option == "circular":
    pos = nx.circular_layout(G)
else:
    pos = nx.kamada_kawai_layout(G)

# Edge coordinates
edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]

    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)

    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

# Create edge trace
edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    line=dict(width=1, color='#888'),
)
st.markdown("Made using Python, Streamlit, NetworkX and Plotly")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)