from methods.philosophers import PHILOSOPHERS
from methods.funlosophers import FUNLOSOPHERS
from methods.scientists import SCIENTISTS
from methods.reasoning import REASONING

def process_user_input(selected_option, philosophers, funlosophers, scientists, reasoning):
    philosopher = None
    funlosopher = None
    scientist = None
    reasoner = None

    if "Philosopher" in selected_option:
        philosopher = selected_option.split('Philosopher: ')[1]
        thought_process = philosophers[philosopher]
    elif "Funlosopher" in selected_option:
        funlosopher = selected_option.split('Funlosopher: ')[1]
        thought_process = funlosophers[funlosopher]
    elif "Scientist" in selected_option:
        scientist = selected_option.split('Scientist: ')[1]
        thought_process = scientists[scientist]
    elif "Reasoning" in selected_option:
        reasoner = selected_option.split('Reasoning: ')[1]
        thought_process = reasoning[reasoner]
    else:
        thought_process = ["Think deeply.", "Consider alternative viewpoints.", "Conclude."]

    return philosopher, funlosopher, scientist, reasoner, philosopher or funlosopher or scientist or reasoner, thought_process