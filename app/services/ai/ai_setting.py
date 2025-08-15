def call_openai(client, messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
