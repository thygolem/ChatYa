import os
import openai

API_KEY = open("API_KEY.txt", "r").read()
openai.api_key = API_KEY


chat_log = []

while True:
    user_message = input("ICCMU@User: ~ $")
    if user_message.lower() == "exit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log,
        )
        assistant_message = response['choices'][0]['message']['content']
        print("ICCMU@Assistant: ~ $", assistant_message.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_message.strip("\n").strip()})














# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": "Quiero información sobre cómo usar blockchain con python y hdfs"},
#     ]
# )

# print(response)

