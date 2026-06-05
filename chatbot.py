
from groq import Groq

client = Groq(api_key="   ") #add your own groq api key

# List of models to try (fallback system)
MODELS = [
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

def chatbot_answer(question):
    last_error = None

    for model in MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Friday, a personal AI assistant. "
                            "You speak clearly and simply. "
                            "The user's name is Shiv."
                        )
                    },
                    {"role": "user", "content": question}
                ],
                temperature=0.6,
                max_tokens=300
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            last_error = e
            continue

    # If all models fail
    return "Sorry Shiv, my AI brain is temporarily unavailable."



