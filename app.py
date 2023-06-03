import os
import sys

import numpy as np
import pandas as pd
import streamlit as st

from api_handler import send_question_to_api
from philosophers import PHILOSOPHERS
from funlosophers import FUNLOSOPHERS
from scientists import SCIENTISTS
from methods import reasoning

def main():

    st.set_page_config(page_title="AI Philosopher")
    st.title("AI Philosopher - Ask Any Question")

    options = ['Philosopher', 'Funlosopher', 'Scientist']

    philosophers_list = list(PHILOSOPHERS.keys())
    funlosophers_list = list(FUNLOSOPHERS.keys())
    scientists_list = list(SCIENTISTS.keys())

    selection = st.selectbox("Explore", options)

    if selection == 'Philosopher':
        selected_option = st.selectbox("Select a Philosopher", [f"Philosopher: {philosopher}" for philosopher in philosophers_list])

        philosopher, funlosopher, scientist, thought_process = reasoning.process_user_input(selected_option, PHILOSOPHERS, FUNLOSOPHERS, SCIENTISTS)

    elif selection == 'Funlosopher':
        selected_option = st.selectbox("Select a Funlosopher", [f"Funlosopher: {funlosopher}" for funlosopher in funlosophers_list])

        philosopher, funlosopher, scientist, thought_process = reasoning.process_user_input(selected_option, PHILOSOPHERS, FUNLOSOPHERS, SCIENTISTS)

    elif selection == 'Scientist':
        selected_option = st.selectbox("Select a Scientist", [f"Scientist: {scientist}" for scientist in scientists_list])

        philosopher, funlosopher, scientist, thought_process = reasoning.process_user_input(selected_option, PHILOSOPHERS, FUNLOSOPHERS, SCIENTISTS)

    else:
        philosopher, funlosopher, scientist = None, None, None
        thought_process = []

    with st.form(key="ask_the_question_form"):
        user_question = st.text_input("Type your question here:")
        submit_button = st.form_submit_button("Ask the Question")

    if submit_button and (philosopher or funlosopher or scientist):
        with st.spinner("Progressing... Please wait"):
            api_response, final_answer = send_question_to_api(philosopher, funlosopher, scientist, thought_process, user_question)

        st.subheader("Final Answer")
        st.write(final_answer)

        st.subheader("Thought Process")
        st.write(api_response)


if __name__ == "__main__":
    main()