def format_response_content(response_content):
    formatted_content = response_content.strip().replace("\n\n", "\n")
    return formatted_content

def validate_user_input(user_question):
    if len(user_question) > 0:
        return True
    else:
        return False