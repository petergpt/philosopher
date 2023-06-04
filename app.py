import sys
import os

import streamlit as st
import numpy as np

from api_handler import send_question_to_api
from process_handler import process_user_input

from methods.philosophers import PHILOSOPHERS
from methods.funlosophers import FUNLOSOPHERS
from methods.scientists import SCIENTISTS
from methods.reasoning import REASONING

def main():
    st.set_page_config(page_title="Reason with AI")
    st.title("Reason with AI - Ask Any Question")

    philosophers_list = list(PHILOSOPHERS.keys())
    funlosophers_list = list(FUNLOSOPHERS.keys())
    scientists_list = list(SCIENTISTS.keys())
    reasoning_list = list(REASONING.keys())

    st.subheader("Choose a Philosopher, Funlosopher, Scientist, or Reasoning")
    
    option = st.radio("", ['Philosopher', 'Funlosopher', 'Scientist', 'Reasoning'])

    thought_process = None

    if option == 'Philosopher':
        selected_philosopher = st.selectbox("Select a Philosopher", philosophers_list)
        thought_process = PHILOSOPHERS.get(selected_philosopher, [])
    elif option == 'Funlosopher':
        selected_philosopher = st.selectbox("Select a Funlosopher", funlosophers_list)
        thought_process = FUNLOSOPHERS.get(selected_philosopher, [])
    elif option == 'Scientist':
        selected_philosopher = st.selectbox("Select a Scientist", scientists_list)
        thought_process = SCIENTISTS.get(selected_philosopher, [])
    elif option == 'Reasoning':
        selected_philosopher = st.selectbox("Select a Reasoning", reasoning_list)
        thought_process = REASONING.get(selected_philosopher, [])
    else:
        selected_philosopher = ""
        thought_process = []

    with st.form(key="ask_the_question_form"):
        user_question = st.text_input("Type your question here:")

        submit_button = st.form_submit_button("Ask the Question")

    if submit_button and selected_philosopher:
        with st.spinner("Progressing... Please wait"):
            api_response, final_answer = send_question_to_api(selected_philosopher, thought_process, user_question)

        st.subheader("Final Answer")
        st.write(final_answer)

        st.subheader(f"{selected_philosopher}'s Thought Process")
        st.write(api_response)

if __name__ == "__main__":
    main()