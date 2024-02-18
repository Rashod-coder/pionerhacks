
import wolframalpha

class OpenAiOutputReader:
    PassKeyStart = "<<<"
    PassKeyEnd = ">>>"
    
    def h():
        print("Hello World")
    
    def init(self, filename):
        print('RUNNING...')
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
                    Output = self.RunWolframAlpha(OpenOutput)
                    if (Output == None):
                      print("output was none exiting")
                      return None
                    print(Output)
                    return None
                else:
                    print("FATAL ERROR: PassKeyEnd not found")
                    return None
        print("FATAL ERROR: PassKeyStart not found")
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
