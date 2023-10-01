import os
import streamlit as st
from ctransformers import AutoModelForCausalLM



@st.cache_resource()
def ChatModel(temperature, top_p):
    return AutoModelForCausalLM.from_pretrained(
        'llama-2-7b-chat.ggmlv3.q2_K.bin', 
        model_type='llama',
        temperature=temperature, 
        top_p = top_p
    )

def generate_llama2_response():
    string_dialogue = '''You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'.
    Utilize The Bhagavad Gita's teachings to address user queries. Quote most appropriate verses to provide insights and solutions. Limit response to 100 words.\n\n'''

    for dict_message in st.session_state.messages[-3:]:
        current_dialogue = ""
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"

    # Removing unnecessary content from output
    output = chat_model(f"prompt {string_dialogue} Assistant:")
    if "User:" in output:
        output_parts = output.split("User:", 1)
        stripped_output = output_parts[0].strip()
    else:
        stripped_output = output
    return stripped_output

def clear_chat_history():
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Welcome, seeker of wisdom. How may I assist you on your journey today? Ask your questions, and I shall guide you."
    }]



st.set_page_config(page_title="GitaSage", page_icon="🕉️", layout="centered")

with st.sidebar:
    st.title('🕉️ GitaSage')
    st.markdown('Discover Inner Peace and Enlightenment')

    temperature = 0.6
    top_p = 0.6 
    chat_model =ChatModel(temperature, top_p)

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Welcome, seeker of wisdom. How may I assist you on your journey today? Ask your questions, and I shall guide you."
    }]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Contemplating..."):
            response = generate_llama2_response()
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)

    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
