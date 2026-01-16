#class
class llm:

    def __init__(self,name):
        self.name=name

    def openai(self):
        print(f"say my name {self.name}")

obj=llm("Heisenberg")
obj.openai()
