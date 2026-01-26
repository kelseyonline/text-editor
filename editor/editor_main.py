# Originator
class Document(): 
    def __init__(self):
        self._content = ""
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

    def __str__(self): 
        return self._content

    

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
    def __init__(self, content): 
        self.content = content


def main(): 
    document = Document()

    document.insert("Hello")
    document.insert(" CSC7302")
    document.insert("!")
    print(document)          # Hello CSC7302!

    document.delete_last(1)
    print(document)          # Hello CSC7302

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