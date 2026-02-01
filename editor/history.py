from __future__ import annotations
from document_state import DocumentState

# Caretaker
class History(): 
    def __init__(self): 
        self._states: list[DocumentState] = []

    # This method is public because another class (Document)
    # needs to know it
    def push(self, state: DocumentState): 
        self._states.append(state)

    def pop(self) -> DocumentState | None: 
        if len(self._states) == 0:
            return None
        return self._states.pop()
    
    def __len__(self):
        return len(self._states) 