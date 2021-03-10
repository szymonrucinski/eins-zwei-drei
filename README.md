# eins-zwei-drei
Zadanie polega na przygotowaniu programu i przeprowadzeniu serii eksperymentów w celu sklasyfikowania ręcznie pisanych cyfr ze zbioru MNIST. Ponieważ jest to typowy zbiór służący weryfikacji metod klasyfikacji obrazów (ang. benchmark) w wielu bibliotekach programistycznych można go pobrać automatycznie. Przykładem może być torchvision lub scikit-learn. Zbiór ten ma tę zaletę, że jest relatywnie liczny i posiada odgórny podział na zbiór treningowy (60000 przykładów) i testowy (10000 przykładów) co umożliwia obiektywne porównanie wyników. Przez eksperyment rozumiem wytrenowanie sieci splotowej z wykorzystaniem zbioru treningowego oraz sprawdzenie jej działania na zbiorze testowym. Wyniki eksperymentów należy zawrzeć w sprawozdaniu. Przy opisie każdego eksperymentu należy przedstawić:

architekturę użytej sieci splotowej (np. rysunek)
opis wykorzystanej funkcji celu, użytego optymalizatora oraz kryterium stopu nauki
opis innych ustawień wpływających na naukę sieci
wykres prezentujący zmiany błędu (funkcji celu) w trakcie przebiegu nauki (z częstotliwością co pewną, rozsądną liczbę epok)
informację na temat tego jak długo (czas) i na jakim sprzęcie (charakterystyka CPU lub GPU, pamięci, itp.) trwała nauka
procentową skuteczność (ang. accuracy) oraz macierz pomyłek (ang. confusion matrix) dla zbioru treningowego i testowego
przykłady (obrazy) cyfr, które zostały niepoprawnie sklasyfikowane wraz z informacją co powinno i co zostało rozpoznane
Opis każdego eksperymentu powinien mieścić się na jednej stronie. Sprawozdania, które nie będą spełniać tego warunku nie będą oceniane. Należy wykonać 4 eksperymenty:

- 2 eksperymenty dla zaproponowanej własnej architektury i różnych (skutecznych) parametrów nauki.
- 2 eksperymenty dla istniejącej architektury sieci dla przypadku gdy uczona jest cała sieć i przypadku gdy część sieci jest wyłączona z nauki oraz wybranych (skutecznych) parametrów nauki
- 
### Wskazówki:

- Ponieważ jest to zadanie rozgrzewkowe to można skorzystać z dostępnych w internecie (a jest ich wiele) przykładów, które pomogą w realizacji zadania.
- Jako funkcji celu (ang. loss) proponuję użyć funkcję entropii krzyżowej (ang. cross-entropy loss).
- Typowe optymalizatory to np. SGD, Adam.
- Przy wyborze istniejącej architektury polecam sieć SqueezeNet. Sieć ta została tak zaprojektowana aby osiągać wyniki zbliżone do sieci AlexNet przy 50-krotnie mniejszej liczbie trenowalnych parametrów (to powinno pomóc osobom nie mającym dostępu do GPU). Można jednak użyć innej architektury.
- Ponieważ trenowanie sieci trochę trwa należy realizować zadanie systematycznie w ramach dostępnego terminu realizacji.
- Zadania ma być zrealizowane indywidualnie. Jako wynik prac należy przesłać dwa pliki:

- report.pdf - raport opisujący wyniki eksperymentów zgodnie z opisanymi powyżej wytycznymi (4 strony)
- source.zip - program użyty do przeprowadzenia eksperymentów (kod źródłowy)
