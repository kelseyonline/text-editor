# Originator
class Document(): 
    FONTS = ['Arial', 'Georgia', 'Calibri']

    def __init__(self, fontName='Arial', fontSize=12):
        self._content = ""
        self.fontName = fontName
        self.fontSize = fontSize
        self._history = History()

    def _create_state(self):
        return DocumentState(self._content)
    
    def _set_content_from_history(self, state): 
        self._content = state.content

    def _save_history_before_change(self): 
        self._history.push(self._create_state())

    # Now we can do the public methods 

    def insert(self, text): 
        self._save_history_before_change()
        self._content += text

    def delete_last(self, n):
        if n <= 0: 
            raise ValueError("n must be positive")
        self._save_history_before_change()
        self._content = self._content[:-n] if n <= len(self._content) else ""

    def undo(self): 
        prev = self._history.pop()

        if prev is None: 
            return None
        
        self._set_content_from_history(prev)

    def change_font(self, fontName): 
        self.fontName = fontName 

    def __str__(self): 
        return f"{self._content}, {self.fontName}, {self.fontSize}"

    

# Caretaker
class History(): 
    def __init__(self): 
        self._states = []

    # This method is public because another class (Document)
    # needs to know it
    def push(self, state): 
        self._states.append(state)

    def pop(self):
        if len(self._states) == 0:
            return None
        return self._states.pop()
    
    def __len__(self):
        return len(self._states) 

# Memento 
class DocumentState(): 
    def __init__(self, content, fontName='Arial', fontSize=12): 
        self.content = content
        self.fontName = fontName 
        self.fontSize = fontSize


def main(): 
    document = Document()

    document.insert("Hello")
    document.insert(" CSC7302")
    document.insert("!")
    print(document)          # Hello CSC7302!

    document.delete_last(1)
    print(document)          # Hello CSC7302

    document.change_font('Georgia')

    document.insert("!!!")
    print(document)          # Hello CSC7302!!!

    document.undo()
    print(document)          # Hello CSC7302


    document.undo()
    print(document)          # Hello CSC7302!

    document.undo()
    print(document)          # Hello CSC7302

    document.undo()
    print(document)          # Hello

main()