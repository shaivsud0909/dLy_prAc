#inheritance
from prac1 import llm

class chatbot(llm):

    def __init__(self, model,name):
        self.model = model
        super().__init__(name)

    def showme(self):
        print(f"I AM calling {self.model}") 
       


bot = chatbot("openai","heisenberg")
bot.showme()
bot.openai()   
