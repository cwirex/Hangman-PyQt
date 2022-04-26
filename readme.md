# Gra Wisielec
![Screenshot from the game](https://github.com/cwirex/Hangman/blob/master/hangman_game.png?raw=true)
<p align="center">Screenshot from the game</p>

### Funkcje gry
1. Baza danych graczy
   - Rejestracja nowych graczy 
   - Przed rozpoczęciem rozgrywki powinna istnieć możliwość rejestracji nowych graczy (Avatar, Nick(unikalny), email, płeć)
   - Dołączenie do gry istniejących graczy (logowanie)
     - Sprawdzana jest baza wyników na podstawie pseudonimu (Nick) gracza 

2. Baza danych wyników
   - Wyniki zapisywane są do bazy po zakończeniu rozgrywki
   - Na czas rundy wyniki przechowywane są lokalne, a po jej zakończeniu aktualizowana jest lista wyników oraz baza danych wyników
   
3. Baza kategoriii słów do odgadnięcia
   - Program dostarczany jest z zaszyfrowanym plikiem (json lub xml) haseł i kategorii.
     - W momencie  uruchomienia  programu następuje próba zaktualizowania pliku  z  bazą danych.
     - W przypadku niepowodzenia korzysta się z dostarczonego pliku.
     
4. Funkcje gry
   - Losowanie kolejności rozpoczęcia gry
   - Losowanie hasła i kategorii (lub wybór kategorii)
   - Limit czasu na odpowiedź
     - Po przekroczeniu czasu automatycznie na ekranie rysowana jest linia
   - Gracz zdobywa 1 pkt za odgadniętą literkę, a po odgadnięciu hasła dostaje +1 za każdą nieodkrytą literę
   - Za błędnie odgadnięte hasło od ilości zdobytych pkt w rundzie  odejmowane są pkt (aktualne pkt – ilość nieodkrytych liter)
   - tryby rozgrywki (co najmniej 2)

5. Dokumentacja
    - Dostępna jest pełna (czytelna) dokumentacja projektu
    - Wygenerowana przy użyciu Sphinx
    - Format HTML lub PDF
