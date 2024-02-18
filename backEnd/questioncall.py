# key = sk-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
import openai
openai.api_key = "sk-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"


messages = []
#messages.append()
messages = [{"role": "system", "content": "You are a math tutor"}]

def check():
    while input != "quit()":
        message = input()
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")
    

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# messages = []
# system_msg = input("What type of chatbot would you like to create?\n")
# messages.append({"role": "system", "content": system_msg})

# print("Your new assistant is ready!")
# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")

system_msg = input("Enter your math problem: ")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= [{"role": "user", "content": system_msg }])
# Open a file named "output.txt" in write mode ('w')
with open('output.txt', 'w') as f:
    # Write data to the file
    f.write(completion.choices[0].message.content+"\n")

# File automatically closed when exiting the 'with' block
init('output.txt')
print(completion.choices[0].message.content)




