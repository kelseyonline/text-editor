# Memento 
class DocumentState(): 
    def __init__(self, content: str, fontName: str, fontSize: int): 
        self.content = content
        self.fontName = fontName 
        self.fontSize = fontSize

    # This is also part of my debugging for my undo method 
    # If I don't add this, it will show useless memory location of DocumentState objects in the 
    # History() class

    def __repr__(self): 
        # Adding angle brackets to help parse the states in the History() list 
        return f"<{self.content}, {self.fontName}, {self.fontSize}>\n"