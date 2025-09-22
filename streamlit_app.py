import streamlit as st
import json

# Load decision tree from JSON
with open("decision_tree.json", "r") as f:
    DECISION_TREE = json.load(f)

# Initialize session state
if "node" not in st.session_state:
    st.session_state.node = "start"

# Initialize a simple chat history
if "history" not in st.session_state:
    st.session_state.history = []

current_node = DECISION_TREE[st.session_state.node]

st.write("### Chatbot")
# Display chat history
for msg in st.session_state.history:
    st.write(msg)

st.write(current_node["message"])

# Display options as buttons
for option in current_node["options"]:
    if st.button(option):
        # Save current message and user choice to history
        st.session_state.history.append(f"**You:** {option}")
        st.session_state.history.append(f"**Bot:** {DECISION_TREE[option]['message']}")
        # Move to the next node
        st.session_state.node = option
        # Rerun automatically via Streamlit's normal rerun
        st.experimental_rerun = lambda: None  # workaround in new versions
        st.session_state.node = option
        st.experimental_rerun()  # works in older versions
