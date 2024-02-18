import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.FileWriter;
import java.io.IOException;

@RestController
@SpringBootApplication
public class AskQuestionApplication {

    public static void main(String[] args) {
        SpringApplication.run(AskQuestionApplication.class, args);
    }

    @PostMapping("/ask")
    public String askQuestion(@RequestBody RequestData data) {
        String problem = data.getProblem();
        String instructions = "When presented with a math problem, please remember that due to limitations in your algorithms, mathematical operations may result in faulty answers. To ensure accuracy, please provide the logic for setting up the equation, and then enclose the final equation in triple angle brackets like so: <<<equation>>>. The final equation should be unsimplified your goal is to do the least amount of calculations. If the equation is already in a solvable form simply return the equation as is and modify it to a friendly format understandable by wolframalpha.  YOUR GOAL IS TO DO THE LEAST AMOUNT OF WORK WHILST HAVING AN ACCURATE EQUATION THAT WILL TAKE YOU TO THE ANSWER.";
        String prompt = instructions + "\nProblem: " + problem;
        OpenAiCompletion completion = OpenAiService.getChatCompletion(prompt);
        
        try (FileWriter fileWriter = new FileWriter("ai_response.txt")) {
            fileWriter.write(completion.choices[0].message.content);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
            return "Error";
        }

        OpenAiOutputReader reader = new OpenAiOutputReader("ai_response.txt");
        String output = reader.runWolframAlpha();

        return "{\"response\": \"" + output + "\"}";
    }

}

class RequestData {
    private String problem;

    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }
}

class OpenAiService {
    // Assume you have a method to get the OpenAiCompletion
    public static OpenAiCompletion getChatCompletion(String prompt) {
        // Implementation to get OpenAiCompletion
        return null;
    }
}

class OpenAiCompletion {
    public Choice[] choices;

    static class Choice {
        public Message message;

        static class Message {
            public String content;
        }
    }
}

class OpenAiOutputReader {
    private static final String PASS_KEY_START = "<<<";
    private static final String PASS_KEY_END = ">>>";
    private String filename;

    public OpenAiOutputReader(String filename) {
        this.filename = filename;
    }

    public String runWolframAlpha() {
        try {
            // Implementation for reading from file and querying Wolfram Alpha
            return null;
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            return null;
        }
    }
}
