import requests, openai
from decouple import config

BOT_API_TOKEN = config('BOT_API_TOKEN', default='', cast=str)
OPENAI_API_TOKEN = config('OPENAI_API_TOKEN', default='', cast=str)


def generate_response_with_url(user_input):
    model_engine = "text-davinci-002"
    endpoint = f"https://api.openai.com/v1/engines/{model_engine}/jobs"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {OPENAI_API_TOKEN}"
    }
    data = {
        'prompt': user_input,
        'max_tokens': 100,
        'n': 1,
        'stop': None,
        'temperature': 0.5
    }
    
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        json_response = response.json()
        return json_response['choices'][0]['text']
    elif response.status_code == 401:
        # Send email to me here. It means that the API Key is not correct (Unauthorized)
        return "Requête non autorisée"
    else:
        return None

sample_1 = generate_response_with_url("Quelle est la date d'aujourd'hui?")
print(sample_1)




def generate_response_with_ai_bot(user_input):
    openai.api_key = OPENAI_API_TOKEN
    model_engine = "text-davinci-002"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    return completions.choices[0].text


sample_2 = generate_response_with_ai_bot("Quelle est la date d'aujourd'hui?")
print(sample_2)
