def process_user_input(selected_option, philosophers, funlosophers, scientists):
    philosopher = None
    funlosopher = None
    scientist = None

    if "Philosopher" in selected_option:
        philosopher = selected_option.split('Philosopher: ')[1]
        thought_process = philosophers[philosopher]
    elif "Funlosopher" in selected_option:
        funlosopher = selected_option.split('Funlosopher: ')[1]
        thought_process = funlosophers[funlosopher]
    elif "Scientist" in selected_option:
        scientist = selected_option.split('Scientist: ')[1]
        thought_process = scientists[scientist]
    else:
        thought_process = ["Think deeply.", "Consider alternative viewpoints.", "Conclude."]

    return philosopher, funlosopher, scientist, philosopher or funlosopher or scientist, thought_process