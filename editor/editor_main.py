# I learned that this module helps with type checking; otherwise I was getting errors when 
# I mentioned the DocumentState class as an argument or return value

from __future__ import annotations

from document import Document

def main(): 
    document = Document()

    document.insert("Hello")
    document.insert(" CSC7302")
    document.insert("!")
    print(document)          # Hello CSC7302!
    # print(document._history._states)

    document.delete_last(1)
    print(document)          # Hello CSC7302
    # print(document._history._states)

    document.change_font('Georgia')
    print(document)
    # print(document._history._states)

    document.change_font_size(20)
    print(document)
    # print(document._history._states)

    # This is where we are testing the undo for font
    document.undo()         # Should be Hello CS7302, Georgia, 12. And it works now! 
    # print(document._history._states)
    print(document)

    document.insert("!!!")
    print(document)          # Hello CSC7302!!!

    document.undo()
    print(document)          # Hello CSC7302

    document.change_font_size(30)
    print(document)
    # print(document._history._states)

    document.undo()
    print(document)
    # print(document._history._states)

    document.change_font('Calibri')
    print(document)

    document.undo()
    print(document)

    document.undo()
    print(document)

if __name__ == "__main__":
    main()