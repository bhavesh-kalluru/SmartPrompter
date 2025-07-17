import openai
from utils import load_api_key

openai.api_key = load_api_key()

def generate_best_prompt(user_input, tone="Neutral", category="General"):
    """
    Generate an ideal prompt using tone and category.
    """
    system_message = (
        "You are an expert prompt engineer. You take short or unclear user input and generate a detailed, "
        f"high-quality prompt in a {tone.lower()} tone and for the context of {category.lower()}."
    )

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"User input: '{user_input}'"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message["content"].strip()
