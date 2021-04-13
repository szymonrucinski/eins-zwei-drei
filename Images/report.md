Cel
===

<span>Celem zadania bylo zaimplementowanie oraz porównanie skuteczności
2 metod optymalizacji funkcji jednowymiarowej: metody bisekcji oraz
dychotomii.</span>

Wprowadzenie
============

<span>Celem implementacji jest znalezienie minimum funkcji w danym
przedziale czyli najmniejszej liczby w zbiorze wartości funkcji $f(x)$.
W celu znalezienia minimum wykorzystaliśmy 2 różne od siebie algorytmy:
bisekcje oraz dychotomie.</span>

Bisekcja
--------

<span>Pierwszym krokiem w metodzie bisekcji jest wyznaczenie przedziału
nieufności ${L_0= \{a,b}\}$. Wspomniany przedział dzielimy na 4
ćwiartki, wyznaczając następujące punkty:$a,x_1,x_0,x_2,b$. Gdzie
${x_0 =}$ $ \frac{a+b}{2} $</span> to środek przedziału. Następnie
liczymy wartość funkcji dla punktów $x_1, x_2, x_0$ oraz definiujemy
$\varepsilon$ dokładność wyniku.Kolejno sprawdzamy czy funkcja rośnie
lub maleje na danym odcinku porównując wartości $f(x_1),f(x_0), f(x_2)$.
W ten sposób określamy gdzie leży minimum. Jeżeli uzyskamy przedział,
który spełnia kryterium stopu $L < 2$$\varepsilon$ gdzie $L=b-a$ to
zwracamy wynik, jeżeli nie to rozpoczynamy proces od nowa.

Dychotomia
----------

<span>W metodzie dychotomii, podobnie jak przy bisekcji, najpierw
wyznaczany jest przedział ufności ${L_0= \{a,b\}}$. Następnie wyznaczany
jest środek tego przedziału ${x_0 =}$ $ \frac{a+b}{2} $ oraz punkty
$x_1$ i $x_2$, które powstają przed odjęcie i dodanie wartości
$ \delta $ podanej przez użytkownika. Porównywane są wartości funkcji w
punkcie $x_1$ oraz $x_2$, a następnie na tej podstawie określa się po
której stronie punktu $x_0$ znajduje się minimum. Drugą połowę
przedziału odrzuca się i taką samą operację powtarza się na nowym
przedziale.</span>

Opis implementacji
==================

<span>Zadanie zostało zrealizowane w języku programowania Python.
Interfejs graficzny został stworzony za pomocą wbudowanej biblioteki
Tkinter. Do prezentowania wykresów użyliśmy biblioteki matplotlib.
Użytkownik wprowadza z poziomu GUI funkcje dla, której ma być policzone
minimum oraz $\varepsilon$, liczbę interacji, metodę optymalizacji oraz
granice przedziału $a,b$.</span>

![image](Images/gui.png) ![image](Images/graph1.png)

Czerwonym punktem na wykresie zostaje oznaczone minimum czarne zaś linie
ilustrują przedziały pośrednie, wyznaczane w trakcie kolejnych iteracji.
Projekt zostal zrealizowany proceduralnie nie obiektowo.

Materiały i metody
==================

<span> W tym miejscu należy opisać, jak przeprowadzone zostały wszystkie
badania, których wyniki i dyskusja zamieszczane są w dalszych sekcjach.
Opis ten powinien być na tyle dokładny, aby osoba czytająca go potrafiła
wszystkie przeprowadzone badania samodzielnie powtórzyć w celu
zweryfikowania ich poprawności. Przy opisie należy odwoływać się i
stosować do opisanych w sekcji drugiej wzorów i oznaczeń, a także w
jasny sposób opisać cel konkretnego testu. Najlepiej byłoby wyraźnie
wyszczególnić (ponumerować) poszczególne eksperymenty tak, aby łatwo
było się do nich odwoływać dalej.</span>

Wyniki
======

<span> W tej sekcji należy zaprezentować, dla każdego przeprowadzonego
eksperymentu, kompletny zestaw wyników w postaci tabel, wykresów
(preferowane) itp. Powinny być one tak ponazywane, aby było wiadomo, do
czego się odnoszą. Wszystkie tabele i wykresy należy oczywiście opisać
(opisać co jest na osiach, w kolumnach itd.) stosując się do przyjętych
wcześniej oznaczeń. Nie należy tu komentować i interpretować wyników,
gdyż miejsce na to jest w kolejnej sekcji. Tu również dobrze jest
wprowadzić oznaczenia (tabel, wykresów), aby móc się do nich odwoływać
poniżej.</span>

Dyskusja
========

<span> Sekcja ta powinna zawierać dokładną interpretację uzyskanych
wyników eksperymentów wraz ze szczegółowymi wnioskami z nich płynącymi.
Najcenniejsze są, rzecz jasna, wnioski o charakterze uniwersalnym, które
mogą być istotne przy innych, podobnych zadaniach. Należy również omówić
i wyjaśnić wszystkie napotkane problemy (jeśli takie były). Każdy
wniosek powinien mieć poparcie we wcześniej przeprowadzonych
eksperymentach (odwołania do konkretnych wyników). Jest to jedna z
najważniejszych sekcji tego sprawozdania, gdyż prezentuje poziom
zrozumienia badanego problemu.</span>

Wnioski
=======

<span> W tej, przedostatniej, sekcji należy zamieścić podsumowanie
najważniejszych wniosków z sekcji poprzedniej. Najlepiej jest je po
prostu wypunktować. Znów, tak jak poprzednio, najistotniejsze są wnioski
o charakterze uniwersalnym.</span>

<span>0</span> T. Oetiker, H. Partl, I. Hyna, E. Schlegl. *Nie za
krótkie wprowadzenie do systemu LaTeX2e*, 2007, dostępny online.
<https://ctan.org/tex-archive/info/lshort/polish/lshort2e.pdf>.

<span> Na końcu należy obowiązkowo podać cytowaną w sprawozdaniu
literaturę, z której grupa korzystała w trakcie prac nad
zadaniem.</span>
