from abc import ABC, abstractmethod

# === Abstract Commands === 
class Command(ABC): 
    @abstractmethod 
    def execute(self): 
        pass

class UndoableCommand(Command): 
    @abstractmethod
    def unexecute(self): 
        pass

# === Receiver === 

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
    
class History(): 
    def __init__(self):
        # This is where we keep a running list of all (undoable) commands we've run
        self._commands: list[UndoableCommand] = []

    # Now build it out like a regular stack 
    def push(self, command):
        self._commands.append(command)

    def pop(self):
        return self._commands.pop()
    
    # This is important to prevent crashing when undoing 
    def __len__(self): 
        return len(self._commands)

# === Concrete Commands === 
class SetTextCommand(UndoableCommand):
    def __init__(self, editor, history, text): 
        self._editor = editor 
        self._history = history 
        self._text = text
        self._prev_text = "" 

    def execute(self): 
        self._prev_text = self._editor._text
        self._history.push(self)
        self._editor.set_text(self._text)

    def unexecute(self): 
        self._editor._text = self._editor._prev_text

class SetContrastCommand(UndoableCommand): 
    def __init__(self, editor, history, contrast): 
        self._editor = editor 
        self._history = history 
        self._contrast = contrast
        self._prev_contrast = 0

    def execute(self): 
        self._prev_contrast = self._editor._contrast
        self._history.push(self)
        self._editor.set_contrast(self._contrast)

    def unexecute(self): 
        self._editor._contrast = self._prev_contrast

class RemoveTextCommand(UndoableCommand): 
    def __init__(self, editor, history): 
        self._editor = editor 
        self._history = history 
        self._prev_text = "" 

    def execute(self): 
        self._prev_text = self._editor._text
        self._history.push(self)
        self._editor.remove_text()

    def unexecute(self): 
        self._editor._text = self._prev_text

class UndoCommand(Command): 
    def __init__(self, history): # This class does not know VideoEditor
        self._history = history
		
    def execute(self):
        if len(self._history) > 0: # Prevents crash on empty list
            self._history.pop().unexecute()
    
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

main()