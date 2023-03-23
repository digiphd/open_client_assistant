import openai

class GPT:
    def __init__(self, gpt_api_key):
        self.gpt_api_key = gpt_api_key

    def chat(self, context, message):
        openai.api_key = self.gpt_api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=context + [{"role": "user", "content": message}]
        )

        return response.choices[0].text.strip()