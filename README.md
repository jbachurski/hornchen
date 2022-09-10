# Hornchen

## Description

*This is a project originally developed in 2017-2018, when I was in middle school.*

Unfortunately, the game was never finished. I am however proud of how much different mechanisms were implemented on the basis of rogue object oriented programming.

Main menu. Start of game.

<img src="https://user-images.githubusercontent.com/25066148/189498445-ecb6456e-8824-4ba9-bcd7-f19771f59b9f.png" width="500"/> <img src="https://user-images.githubusercontent.com/25066148/189498476-a73f5e52-7fac-4549-969b-ed4a78c196f4.png" width="500"/>

Inventory. Spell tree.

<img src="https://user-images.githubusercontent.com/25066148/189498597-76926b03-e30a-4dc9-a2cd-f2de40f9692b.png" width="500"/> <img src="https://user-images.githubusercontent.com/25066148/189498637-f05e7037-68c1-4f4a-aacd-1b7bcf45de3f.png" width="500"/>

Screen scrolling. Minimap.

<img src="https://user-images.githubusercontent.com/25066148/189498660-e0a8ead7-0c9f-4bba-9d10-16d9fe16ec43.png" width="500"/> <img src="https://user-images.githubusercontent.com/25066148/189498760-b80ce2e4-7771-4f51-a739-ba26d45c1406.png" width="500"/>

Combat (particles!!). Console (with a Python REPL).

<img src="https://user-images.githubusercontent.com/25066148/189498848-f7c995bb-99b3-48c8-9a01-7c1156a5caf1.png" width="500"/> <img src="https://user-images.githubusercontent.com/25066148/189498948-511ddb1c-823e-433d-b588-5d3f8e46001b.png" width="500"/>

The assets are based on a free alpha of an old game called Desktop Dungeons.

## Full description - Polish

### Wstęp

Hornchen to gra w zamyśle roguelike. Jest jeszcze niedokończona (w szczególności faktyczna rozgrywka),
ale jej główne elementy są sprawne - generowanie losowej mapy pomieszczeń, wrogowie, ekwipunek, umiejętności gracza.
Napisana jest całkowicie obiektowo w Pythonie z wykorzystaniem biblioteki pygame.

Silnik gry oparty jest na stanach (states), np. menu główne, ekwipunek gracza, widok poziomu (pomieszczenia).

Notatka: do uruchomienia gry potrzebna jest biblioteka pygame. Do jej zainstalowania można wykorzystać
         wbudowaną część Pythona - pip - za pomocą komendy cmd.exe "pip install pygame". Bibliotekę można
         też ewentualnie pobrać z https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame 

Grę włączamy za pomocą app.py (z widokiem konsoli Pythona - log) lub $launcher.pyw (bez konsoli Pythona)

### Menu główne

- "Continue" spróbuje wczytać zapis gry. Jeżeli nie może go znaleźć, nic się nie dzieje.
- "Start" wygeneruje nową mapę i zacznie nową grę.
- "Settings" to prosty prototyp ustawień 
  - w trybie z włączoną myszką "Use Mouse" efekty przedmiotów są kierowane w kierunku kursora

### Widok gry

Pojawia się po użyciu "Continue" lub "Start".

W górnej cześci ekranu znajduje się "Topbar", na którym widać obecny stan gracza (życie/mana),
używany przedmiot (pod przyciskiem "Z") i czar (pod "X"). W prawym górnym rogu jest minimapa.

Na początku gry gracz zawsze znajdzie się w pomieszczeniu startowym, w którym znajduje się
jedna pusta skrzynia, przeciwnik poruszający się w losowych kierunkach oraz przeciwnik
podążający za graczem.

### Klawisze

#### Gra

- lewo, prawo, góra, dół - W/S/A/D, strzałki
- użyj przedmiotu - Z, LPM (lewy przycisk myszy)
- użyj czaru (tzn. umiejętności) - X, PPM
- szybsze poruszanie (sprint) - V
- aktywacja części mapy (drzwi, skrzynia) - Spacja

#### W menu

- lewo, prawo, góra, dół - W/S/A/D, strzałki
- działanie w menu: Z/LPM, X/PPM, Spacja
- w widoku minimapy: powrót widoku do pozycji gracza - P
- wyjście - Escape, Enter

#### Włączanie menu

- pauza - Escape
- ekwipunek - I
- widok mapy - M
- widok wszystkich czarów (umiejętności) - T

#### Debugging

- konsola (interaktywny REPL Pythona) - F2
- widok debug - F3
- włącz/wyłącz użycie myszki - F6
- włącz/wyłącz nagrywanie - F9/F10, (uwaga: wymaga biblioteki 3rd-party: numpy)
- włącz/wyłącz tryb pełnoekranowy - F11
- screenshot - F12

#### W konsoli

Można używać prawie wszystkich znaków na zwykłej klawiaturze.
- wpisanie linii - Enter
- usuń jeden znak - Backspace
- usuń linię - Delete
- przewijaj widok w górę - Page Up
- przewijaj widok w dół - Page Down
- poprzedni z historii - strzałka w dół (historia to poprzednie wpisane komendy)
- następny z historii - strzałka w górę
- pozycja wskaźnika (gdzie są wpisywane litery) - strzałka w lewo/prawo


### Rozgrywka

#### Działanie
W widoku gry możemy używać przedmiotów, by pokonać wrogów. Należy się też poruszać by unikać ich ataków.
Inaczej tracimy życie. Aby pokonać wrogów możemy używać przedmiotów (tyle, ile chcemy) [Z/LPM] lub czarów [X/PPM],
które zużywają manę.

#### Pomieszczenia
W dowolnym momencie możemy przejść do innego pomieszczenia udając się przez jedne z drzwi
(obok niego należy nacisnąć spację lub wyjść poza mapę). Znajdziemy się wtedy w innym pomieszczeniu.
Wszystko, co zrobiliśmy w poprzednim pomieszczeniu jest zapisane i zapamiętane. Po tym, jak wrócimy
do pomieszczenia przeprowadzana jest "symulacja" tego, co się działo, gdy znajdowaliśmy się poza nim.
(np. przeciwnicy nadal się poruszają).

Wchodząc do innego pomieszczenia na minimapie odkrywamy wszystkie do niego sąsiednie. Znaki zapytania
oznaczają pomieszczenie nieodkryte.

#### Ekwipunek [I]
Przedmioty wybieramy kursorem myszki lub używając przycisków lewo/prawo/góra dół. Z/LPM wybieramy nowy
przedmiot do używania pod przyciskiem używania przedmiotu. Używając X/PPM możemy przenosić przedmioty
w ekwipunku pomiędzy dwoma miejscami, co pozwala na ich uporządkowanie. Najechanie na przedmiot
pokazuje jego opis, powiększoną ikonę i statystyki.

#### Czary [T]
Należy najechać na czar i używając przycisku X odblokować go. Następnie Z możemy go zaznaczyć do użycia.
Czary:

- płomyczki, promień spowalniający wrogów, kula ognia, pułapka

#### Minimapa [M]

Możemy ją przemieszczać używając kursora myszy (przytrzymując i przemieszczając go) lub przyciskami
lewo/prawo/góra/dół.

#### Pauza [Escape]
W oknie pauzy można użyć opcji "Save" by zapisać w pełni stan gry do pliku "save.json" w obecnej ścieżce. 

#### Konsola [F2]
Przydatne funkcje:
`get_player().reveal_all_map_tiles()` - odkrycie całej mapy (należy ją aktualizować przechodząc do innego pomieszczenia)
`spawn_enemy(type, col, row, count=1)` - np. spawn_enemy(enemies.GrayGoo, 5, 5) - przywołanie przeciwnika
`infmana()` - nieskończona mana do czarów

Jest to w pełni użyteczna konsola Pythona, więc wyrażenia tj.
```
> x = 5
> x + 3
8
```
Działają tak jak można się spodziewać.




Jakub Bachurski © 2017 kbachurski@gmail.com
