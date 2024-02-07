Aplikacja zegara napisana w języku Python przy użyciu frameworku Flask i umieszczona w kontenerze Docker.

1. Zbuduj obraz Dockera:


    docker build -t zegar .


2. Uruchom kontener:


    docker run -p 5000:5000 zegar


3. Aplikacja jest dostępna pod adresem localhost:5000

Inne szczegóły:

- app.py: Aplikacja zawierająca kod FLASK
- templates/index.html: Plik HTML
- Dockerfile: Plik konfiguracyjny dla Docker.

//Frameworki i biblioteki

- Flask==2.0.1
- Werkzeug==2.0.1


//Edycja danych

Możesz dostosować aplikację zegara, modyfikując kod w pliku `app.py`. Możesz również zmienić wygląd strony, edytując plik `templates/index.html`.

//Licencja

Ten projekt jest objęty licencją MIT.