from __future__ import annotations

# Originator
class Document(): 
    # I'm not sure if it's good practice to include 
    # constants within a class 
    FONTS = ['Arial', 'Georgia', 'Calibri']

    # I will initialize it with default values 
    def __init__(self):
        self._content = ""
        self._fontName = 'Arial'
        self._fontSize = 12
        self._history = History()

    def _create_state(self):
        return DocumentState(self._content, self._fontName, self._fontSize)
    
    # Apparently the content of state needs to be public since we are using it in a different class 
    def _set_content_from_history(self, state: DocumentState):
        self._content: str = state.content
        self._fontName: str = state.fontName
        self._fontSize: int = state.fontSize

    def _save_history_before_change(self): 
        self._history.push(self._create_state())

    # Now we can do the public methods 

    def insert(self, text: str): 
        self._save_history_before_change()
        self._content += text

    def delete_last(self, n: int):
        if n <= 0: 
            raise ValueError("n must be positive")
        self._save_history_before_change()
        self._content = self._content[:-n] if n <= len(self._content) else ""

    # This method is our primary highlight for this task 

    def undo(self): 
        prev = self._history.pop()

        # Can comment out after debugging
        # print(f"Prev is {prev}")

        if prev is None: 
            return None
        
        self._set_content_from_history(prev)

    def change_font(self, _fontName: str): 
        self._save_history_before_change()
        self._fontName = _fontName 

    def change_font_size(self, _fontSize: int): 
        self._save_history_before_change()
        self._fontSize = _fontSize

    def __str__(self): 
        return f"{self._content}, {self._fontName}, {self._fontSize}"