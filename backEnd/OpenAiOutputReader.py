class OpenAiOutputReader:
    PassKeyStart = "<<<"
    PassKeyEnd = ">>>"

    def init(self, filename):
        try:
            with open(filename, 'r') as file:
                answer = self.readfile(file)
                print(answer)
                print("Program exited with exit code 69")
        except FileNotFoundError:
            print("File not found")

    def readfile(self, file):
        for line in file:
            index1 = line.find(self.PassKeyStart)
            if index1 != -1:
                index2 = line.find(self.PassKeyEnd, index1)
                if index2 != -1:
                    return line[index1 + len(self.PassKeyStart):index2]
                else:
                    print("FATAL ERROR: PassKeyEnd not found")
                    return None
        print("FATAL ERROR: PassKeyStart not found")
        return None


if __name == "__main":
    file_name = "my.txt"
    m = OpenAiOutputReader(file_name)