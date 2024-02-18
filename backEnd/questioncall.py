# key = sk-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
import openai
openai.api_key = "sk-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"

messages = []
#messages.append()
# messages = [{"role": "system", "content": "You are a math tutor"}]

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

prompt = "When presented with a math problem, please remember that due to limitations in your algorithms, mathematical operations may result in faulty answers. To ensure accuracy, please provide the logic for setting up the equation, and then enclose the final equation in triple angle brackets like so: <<<equation>>>. The final equation should be unsimplified your goal is to do the least amount of calculations. If the equation is already in a solvable form simply return the equation as is and modify it to a friendly format understandable by wolframalpha.  YOUR GOAL IS TO DO THE LEASDT AMOUNT OF WORK WHILST HAVING AN ACCURATE EQUATION THAT WILL TAKE YOU TO THE ANSWER."
system_msg = input("Enter your math problem: ")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= [{"role": "user", "content": prompt+system_msg }])
print(completion.choices[0].message.content)