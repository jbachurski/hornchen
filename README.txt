Hornchen - Readme

Wst�p
Hornchen to gra w zamy�le roguelike. Jest jeszcze niedoko�czona (w szczeg�lno�ci faktyczna rozgrywka),
ale jej g��wne elementy s� sprawne - generowanie losowej mapy pomieszcze�, wrogowie, ekwipunek, umiej�tno�ci gracza.
Napisana jest ca�kowicie obiektowo w Pythonie z wykorzystaniem biblioteki pygame.
Silnik gry oparty jest na stanach (states), np. menu g��wne, ekwipunek gracza, widok poziomu (pomieszczenia).
Notatka: do uruchomienia gry potrzebna jest biblioteka pygame. Do jej zainstalowania mo�na wykorzysta�
         wbudowan� cz�� Pythona - pip - za pomoc� komendy cmd.exe "pip install pygame". Bibliotek� mo�na
         te� ewentualnie pobra� z https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame 

Gr� w��czamy za pomoc� app.py (z widokiem konsoli Pythona - log) lub $launcher.pyw (bez konsoli Pythona)

Menu g��wne
"Continue" spr�buje wczyta� zapis gry. Je�eli nie mo�e go znale��, nic si� nie dzieje.
"Start" wygeneruje now� map� i zacznie now� gr�.
"Settings" to prosty prototyp ustawie� 
- w trybie z w��czon� myszk� "Use Mouse" efekty przedmiot�w s� kierowane w kierunku kursora

Widok gry
Pojawia si� po u�yciu "Continue" lub "Start".
W g�rnej cze�ci ekranu znajduje si� "Topbar", na kt�rym wida� obecny stan gracza (�ycie/mana),
u�ywany przedmiot (pod przyciskiem "Z") i czar (pod "X"). W prawym g�rnym rogu jest minimapa.
Na pocz�tku gry gracz zawsze znajdzie si� w pomieszczeniu startowym, w kt�rym znajduje si�
jedna pusta skrzynia, przeciwnik poruszaj�cy si� w losowych kierunkach oraz przeciwnik
pod��aj�cy za graczem.

Klawisze
- Gra:
lewo, prawo, g�ra, d� - W/S/A/D, strza�ki
u�yj przedmiotu - Z, LPM (lewy przycisk myszy)
u�yj czaru (tzn. umiej�tno�ci) - X, PPM
szybsze poruszanie (sprint) - V
aktywacja cz�ci mapy (drzwi, skrzynia) - Spacja

- W menu:
lewo, prawo, g�ra, d� - W/S/A/D, strza�ki
dzia�anie w menu: Z/LPM, X/PPM, Spacja
w widoku minimapy: powr�t widoku do pozycji gracza - P
wyj�cie - Escape, Enter

- W��czanie menu:
pauza - Escape
ekwipunek - I
widok mapy - M
widok wszystkich czar�w (umiej�tno�ci) - T

- Debugging:
konsola (interaktywny REPL Pythona) - F2
widok debug - F3
w��cz/wy��cz u�ycie myszki - F6
w��cz/wy��cz nagrywanie - F9/F10, (uwaga: wymaga biblioteki 3rd-party: numpy)
w��cz/wy��cz tryb pe�noekranowy - F11
screenshot - F12

- W konsoli:
Mo�na u�ywa� prawie wszystkich znak�w na zwyk�ej klawiaturze.
wpisanie linii - Enter
usu� jeden znak - Backspace
usu� lini� - Delete
przewijaj widok w g�r� - Page Up
przewijaj widok w d� - Page Down
(historia to poprzednie wpisane komendy)
poprzedni z historii - strza�ka w d�
nast�pny z historii - strza�ka w g�r�
pozycja wska�nika (gdzie s� wpisywane litery) - strza�ka w lewo/prawo


Rozgrywka
- Dzia�anie
W widoku gry mo�emy u�ywa� przedmiot�w, by pokona� wrog�w. Nale�y si� te� porusza� by unika� ich atak�w.
Inaczej tracimy �ycie. Aby pokona� wrog�w mo�emy u�ywa� przedmiot�w (tyle, ile chcemy) [Z/LPM] lub czar�w [X/PPM],
kt�re zu�ywaj� man�.

- Pomieszczenia
W dowolnym momencie mo�emy przej�� do innego pomieszczenia udaj�c si� przez jedne z drzwi
(obok niego nale�y nacisn�� spacj� lub wyj�� poza map�). Znajdziemy si� wtedy w innym pomieszczeniu.
Wszystko, co zrobili�my w poprzednim pomieszczeniu jest zapisane i zapami�tane. Po tym, jak wr�cimy
do pomieszczenia przeprowadzana jest "symulacja" tego, co si� dzia�o, gdy znajdowali�my si� poza nim.
(np. przeciwnicy nadal si� poruszaj�).
Wchodz�c do innego pomieszczenia na minimapie odkrywamy wszystkie do niego s�siednie. Znaki zapytania
oznaczaj� pomieszczenie nieodkryte.

- Ekwipunek [I]
Przedmioty wybieramy kursorem myszki lub u�ywaj�c przycisk�w lewo/prawo/g�ra d�. Z/LPM wybieramy nowy
przedmiot do u�ywania pod przyciskiem u�ywania przedmiotu. U�ywaj�c X/PPM mo�emy przenosi� przedmioty
w ekwipunku pomi�dzy dwoma miejscami, co pozwala na ich uporz�dkowanie. Najechanie na przedmiot
pokazuje jego opis, powi�kszon� ikon� i statystyki.

- Czary [T]
Nale�y najecha� na czar i u�ywaj�c przycisku X odblokowa� go. Nast�pnie Z mo�emy go zaznaczy� do u�ycia.
Czary:
p�omyczki, promie� spowalniaj�cy wrog�w, kula ognia, pu�apka

- Minimapa [M]
Mo�emy j� przemieszcza� u�ywaj�c kursora myszy (przytrzymuj�c i przemieszczaj�c go) lub przyciskami
lewo/prawo/g�ra/d�.

- Pauza [Escape]
W oknie pauzy mo�na u�y� opcji "Save" by zapisa� w pe�ni stan gry do pliku "save.json" w obecnej �cie�ce. 

- Konsola [F2]
Przydatne funkcje:
get_player().reveal_all_map_tiles() - odkrycie ca�ej mapy (nale�y j� aktualizowa� przechodz�c do innego pomieszczenia)
spawn_enemy(type, col, row, count=1) - np. spawn_enemy(enemies.GrayGoo, 5, 5) - przywo�anie przeciwnika
infmana() - niesko�czona mana do czar�w

Jest to w pe�ni u�yteczna konsola Pythona, wi�c wyra�enia tj.
> x = 5
> x + 3
8
Dzia�aj� tak jak mo�na si� spodziewa�.




Jakub Bachurski � 2017 kbachurski@gmail.com