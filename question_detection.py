from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# https://huggingface.co/shahrukhx01/bert-mini-finetune-question-detection?text=is+this+a+question%3F
# ACHTUNG dieser code returned true für True für alle recomenadtion fragen
class QuestionDetection:
    def __init__(self):
        tokenizer = AutoTokenizer.from_pretrained("shahrukhx01/question-vs-statement-classifier")
        model = AutoModelForSequenceClassification.from_pretrained("shahrukhx01/question-vs-statement-classifier")
        self.classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

    def predict(self, input):
        if "display" in input.lower() or "show" in input.lower() or "recommend" in input.lower():
            return True

        # if true == Question, if false == no Question
        isQuestion = self.classifier(input)
        if isQuestion[0]["label"] == "LABEL_1":
            return True
        elif isQuestion[0]["label"] == "LABEL_0":
            return False

'''
This code runs in an virtual environment with the following packages installed:
https://huggingface.co/docs/transformers/installation 
I am not yet sure if I have to install them directly on my machine or if I can use the virtual environment (regarding github)
print(QuestionDetection().predict("Who is the director of Good Will Hunting?"),"1")
print(QuestionDetection().predict("Who directed The Bridge on the River Kwai?"),"2")
print(QuestionDetection().predict("Who is the director of Star Wars: Episode VI - Return of the Jedi?"),"3")
print(QuestionDetection().predict("Who is the screenwriter of The Masked Gang: Cyprus?"),"4")
print(QuestionDetection().predict("What is the MPAA film rating of Weathering with You?	"),"5")
print(QuestionDetection().predict("What is the genre of Good Neighbors?	"),"6")
print(QuestionDetection().predict("Show me a picture of Halle Berry."),"7")
print(QuestionDetection().predict("What does Julia Roberts look like?"),"8")
print(QuestionDetection().predict("Let me know what Sandra Bullock looks like."),"9")
print(QuestionDetection().predict("Recommend movies similar to Hamlet and Othello."),"10")
print(QuestionDetection().predict("Given that I like The Lion King, Pocahontas, and The Beauty and the Beast, can you recommend some movies?"),"11")
print(QuestionDetection().predict("Recommend movies like Nightmare on Elm Street, Friday the 13th, and Halloween.	"),"12")
print(QuestionDetection().predict("What is the box office of The Princess and the Frog?	"),"13")
print(QuestionDetection().predict("Can you tell me the publication date of Tom Meets Zizou?	"),"14")
print(QuestionDetection().predict("Who is the executive producer of X-Men: First Class?	"),"15")
'''
