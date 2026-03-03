class VideoEditor: 
    def __init__(self) -> None: 
        self._contrast = 0.5
        self._text = ""

    def set_text(self, text: str) -> None: 
        self._text = text 

    def remove_text(self) -> None: 
        self._text = ""

    def get_contrast(self) -> float: 
        return self._contrast
    
    def set_contrast(self, contrast: float) -> None: 
        self._contrast = contrast 

    def __str__(self) -> str: 
        return f"VideoEditor(contrast={self._contrast}, text={self._text!r})"
    
def main(): 
    editor = VideoEditor()
    history = History() # Or whatever helper object this design needs

    # user actions 
    set_text = SetTextCommand(editor, history, "Intro")
    set_text.execute()

    set_contrast = SetContrastCommand(editor, history, 0.8)
    set_contrast.execute()

    remove_text = RemoveTextCommand(editor, history) 
    remove_text.execute()

    print(editor) # Should reflect the latest changes

    undo = UndoCommand(history)
    undo.execute()
    undo.execute()

    print(editor) # Should reflect 2 undos