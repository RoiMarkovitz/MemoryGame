# MemoryGame

The game was created as my idea for a project in the course "Seminar in Python - GUI and Design Patterns" at the academy.

The implemented design patterns are Memento and Singleton.

The Singleton was chosen because it was decided that only one game could exist at a time in the system.
This concept has also been used to prevent the opening of selected windows more than once at a time.

The Memento was chosen in the purpose of saving previous game states to allow the player to undo bad moves and thus maintain good game stats.

[Click to view my PP presentation of the project](/Presentation.pptx)

### Memory Game Description
- The game object is to match pairs of cards in as few attempts as possible.
- The player chooses from 3 difficulty levels: Beginner, Intermediate and Expert.
- The game board appears when all the cards are hidden.
- A game round takes place when a player selects two cards.
- If both cards match, the player earns point(s), and the cards remain visible.
- Otherwise, the cards become hidden.
- The game ends when there are no more cards to compare.

### Memory Game Features 
- Undo button allows the player to go back to the last game move.
- 3 difficulty levels to choose from: Beginner, Intermediate and Expert.
- 15 different types of cards.
- Game stats: Score, Moves, Undos left, streak and max streak.
- Scoring based on a sequence of matching successes. 
- Table of game history of all players.
- Option to search the table by player’s nickname.

### Conclusions
- Using singleton helped preventing the same screen to exist at once. But I could simply maintain only one screen open at a time or disable buttons that open screens, once these screens are already open.
However, doing so is a bad practice. the use of the singleton illustrates the desired use of the system: only one game instance should exist. The business logic should decide on the implementation and limitation of the game. That is not the view’s job.
- Using memento enriched the game experience and added a strategic aspect. It’s a great and interesting addition to the game.

### Example of some of the GUI screens

Main Menu         
:-------------------------:
<img src="https://github.com/roi-c/MemoryGame/blob/master/gui_images/MainMenu.jpg" alt="drawing" width="800"/>  

Game Options      
:-------------------------:
<img src="https://github.com/roi-c/MemoryGame/blob/master/gui_images/GameOptions.jpg" alt="drawing" width="800"/>  

Beginner Game    
:-------------------------:
<img src="https://github.com/roi-c/MemoryGame/blob/master/gui_images/BeginnerGame.jpg" alt="drawing" width="800"/> 

Intermediate Game   
:-------------------------:
<img src="https://github.com/roi-c/MemoryGame/blob/master/gui_images/IntermediateGame.jpg" alt="drawing" width="800"/> 

Expert Game    
:-------------------------:
<img src="https://github.com/roi-c/MemoryGame/blob/master/gui_images/ExpertGame.jpg" alt="drawing" width="800"/>  

Reports Table    
:-------------------------:
<img src="https://github.com/roi-c/MemoryGame/blob/master/gui_images/ReportsTable.jpg" alt="drawing" width="800"/>  



