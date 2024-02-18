import openai
import wolframalpha
openai.api_key = "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"

messages = []; 

# def CustomChatGPT(user_input):
#     messages.append({"role": "user", "content": user_input})
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = messages


instructions = "When presented with a math problem, please remember that due to limitations in your algorithms, mathematical operations may result in faulty answers. To ensure accuracy, please provide the logic for setting up the equation, and then enclose the final equation in triple angle brackets like so: <<<equation>>>. The final equation should be unsimplified your goal is to do the least amount of calculations. If the equation is already in a solvable form simply return the equation as is and modify it to a friendly format understandable by wolframalpha.  YOUR GOAL IS TO DO THE LEASDT AMOUNT OF WORK WHILST HAVING AN ACCURATE EQUATION THAT WILL TAKE YOU TO THE ANSWER."; #add chatgpt manual prompt here
problem = input("Enter math problem: ")
prompt = instructions + "/n" +  problem; 
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

file  = open("ai_response.txt", "a")
file.write(completion.choices[0].message.content)
file.close()

hint_instructions = "I need help solving this problem can you help me do the set up only. Do not solve for the final answer"
hint_prompt = hint_instructions + "/n" + problem 
hint_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": hint_prompt}])
print(hint_completion.choices[0].message.content)




class OpenAiOutputReader:
    PassKeyStart = "<<<"
    PassKeyEnd = ">>>"
    
    
    def __init__(self, filename):
        try:
            with open(filename, 'r') as file:
                self.readfile(file)
        except FileNotFoundError:
            print("File not found")

    def readfile(self, file):
        for line in file:
            index1 = line.find(self.PassKeyStart)
            if index1 != -1:
                index2 = line.find(self.PassKeyEnd, index1)
                if index2 != -1:
                    OpenOutput = line[index1 + len(self.PassKeyStart):index2]
                    # print("wolfram sees the next line")
                    # print(OpenOutput)
                    Output = self.RunWolframAlpha(OpenOutput)
                    if (Output == None):
                      print("output was none exiting")
                      return None
                    # print("THE FOLLOWING LINE IS THE ANSWER")
                    # print(Output)
                    return None
                else:
                    # print("FATAL ERROR: PassKeyEnd not found")
                    return None
        # print("mypasskeynofound")
        return None


    def RunWolframAlpha(self, OpenOutput):
      # Define your WolframAlpha API key
      ApiKey = 'EEXP69-GGL8V57YYJ'
      
      # Initialize the client
      client = wolframalpha.Client(ApiKey)
      
      # Query the API with your input
      print(OpenOutput)
      Response = client.query(OpenOutput)

      # Print the result
      bool = False
      for a  in Response.pods:
          if ( "Solution" == a.title ):
              bool = True
          for b in a.subpods:
              if (bool):
                return b.plaintext
              

      return None

# reader = OpenAiOutputReader("bob.txt")
reader = OpenAiOutputReader("ai_response.txt")