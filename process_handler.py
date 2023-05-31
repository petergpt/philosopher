def process_user_input(selected_option, philosophers, funlosophers):
    philosopher = None
    funlosopher = None

    if "Philosopher" in selected_option:
        philosopher = selected_option.split('Philosopher: ')[1]
        thought_process = philosophers[philosopher]
    elif "Funlosopher" in selected_option:
        funlosopher = selected_option.split('Funlosopher: ')[1]
        thought_process = funlosophers[funlosopher]
    else:
        thought_process = ["Think deeply.", "Consider alternative viewpoints.", "Conclude."]

    return philosopher, funlosopher, philosopher or funlosopher, thought_process