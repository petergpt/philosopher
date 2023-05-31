import streamlit as st
import numpy as np

from api_handler import send_question_to_api
from process_handler import process_user_input
from philosophers import PHILOSOPHERS
from funlosophers import FUNLOSOPHERS

def main():
    st.set_page_config(page_title="Philosophical Chatbot")
    st.title("Ask AI Philosopher")

    philosophers_list = list(PHILOSOPHERS.keys())
    funlosophers_list = list(FUNLOSOPHERS.keys())

    st.subheader("Choose a Philosopher or Funlosopher")
    option = st.radio("", ['Philosopher', 'Funlosopher'])

    if option == 'Philosopher':
        selected_philosopher = st.selectbox("Select a Philosopher", philosophers_list)
        thought_process = PHILOSOPHERS.get(selected_philosopher, [])
    elif option == 'Funlosopher':
        selected_philosopher = st.selectbox("Select a Funlosopher", funlosophers_list)
        thought_process = FUNLOSOPHERS.get(selected_philosopher, [])
    else:
        selected_philosopher = ""
        thought_process = []

    user_question = st.text_input("Type your question here:")

    if st.button("Ask the Philosopher") and selected_philosopher:
        api_response, final_answer = send_question_to_api(selected_philosopher, thought_process, user_question)

        st.subheader("Final Answer")
        st.write(final_answer)
        
        st.subheader(f"{selected_philosopher}'s Thought Process")
        st.write(api_response)

if __name__ == "__main__":
    main()