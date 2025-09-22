import streamlit as st
import json

# Load the decision tree from JSON
with open("decision_tree.json", "r") as f:
    DECISION_TREE = json.load(f)

# Initialize session state
if "node" not in st.session_state:
    st.session_state.node = "start"
if "history" not in st.session_state:
    st.session_state.history = []
if "node_stack" not in st.session_state:
    st.session_state.node_stack = []

def go_to_node(option):
    # Handle Back button
    if option == "Back" and st.session_state.node_stack:
        st.session_state.node = st.session_state.node_stack.pop()
    else:
        st.session_state.node_stack.append(st.session_state.node)
        st.session_state.node = option
    
    # Save chat history
    st.session_state.history.append(f"**You:** {option}")
    st.session_state.history.append(f"**Bot:** {DECISION_TREE[st.session_state.node]['message']}")

# Display chat history
st.title("Rules-Based Chatbot")
for msg in st.session_state.history:
    st.write(msg)

# Display current node message if not empty
current_node = DECISION_TREE[st.session_state.node]
if not st.session_state.history or st.session_state.history[-1] != f"**Bot:** {current_node['message']}":
    st.write(f"**Bot:** {current_node['message']}")

# Display options as buttons
for option in current_node["options"]:
    if st.button(option):
        go_to_node(option)
        st.experimental_rerun()
