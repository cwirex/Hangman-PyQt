# Gra Wisielec
![Screenshot from the game](https://github.com/cwirex/Hangman/blob/master/hangman_game.png?raw=true)
<p align="center">Screenshot from the game</p>

### Game Info
1. **Player Database**
   - Registration of new players
     - Before starting the game, there should be an option to register new players (Avatar, unique Nickname, email, gender)
   - Existing players joining the game (login)
     - The database of results is checked based on the player's Nickname

2. **Results Database**
   - Results are saved to the database after the game ends
   - During a round, results are stored locally, and after it ends, the results list and database are updated

3. **Word Categories Database**
   - The program is provided with an encrypted file (json or xml) of phrases and categories
     - When the program starts, an attempt is made to update the database file
     - If updating fails, the provided file is used

4. **Game Features**
   - Drawing the starting order
   - Drawing a phrase and category (or selecting a category)
   - Time limit for responses
     - After exceeding the time limit, a line is automatically drawn on the screen
   - The player earns 1 point for each guessed letter, and after guessing the phrase, they get +1 for each undiscovered letter
   - For an incorrectly guessed phrase, points are subtracted from the points earned in the round (current points – number of undiscovered letters)
   - Game modes (at least 2)

5. **Documentation**
   - Complete (readable) project documentation is available
   - Generated using Sphinx
   - Format HTML or PDF

