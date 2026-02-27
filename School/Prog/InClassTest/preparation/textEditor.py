from stack import LinkedStack

class TextEditor:
    def __init__(self):
        self.stack = LinkedStack()

    def write(self, text):
        self.stack.push(text)

    def undo(self):
        self.stack.pop()

    def get_content(self):
        reversed_stack = LinkedStack()
        text = ""
        while not self.stack.is_empty():
            reversed_stack.push(self.stack.pop())
        while not reversed_stack.is_empty():
            element = reversed_stack.pop()
            self.stack.push(element)
            text += element
        return text

if __name__ == "__main__":
    textEditor = TextEditor()
    textEditor.write("Hello ")
    textEditor.write("haloo")
    textEditor.undo()
    textEditor.write("World")
    print(textEditor.get_content())