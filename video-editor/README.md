### Video Editor 

# Pattern decision 
My choice: Command (with some Memento elements because we use History/Caretaker)

1. What is the key idea of this pattern?
The command pattern encapsulates an action as an object. It helps to keep classes uncoupled. 

2. Why is it a better fit than the other?
I believe that memento may be a better choice if we were trying to save a larger snapshot of the entire video, but because our main goal is just to track the operations done on it, it makes more sense to go the Command route.

3. What is the main tradeoff of this choice (memory vs flexibility)?
Using Memento in this case would be very memory intensive, since we're having to save the entire state of the video rather than just saving the history of the various operations done on the video 