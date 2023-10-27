# Blog Internetowy

To jest aplikacja Django umożliwiająca tworzenie i zarządzanie blogiem internetowym. Aplikacja obsługuje różne typy użytkowników, takie jak administratorzy, redaktorzy i czytelnicy.

## Funkcje

### Dla wszystkich użytkowników

1. **Rejestracja**: Wszyscy użytkownicy mogą zarejestrować się w aplikacji, a po rejestracji otrzymają uprawnienia do komentowania postów. Administrator może nadawać uprawnienia redaktora wybranym użytkownikom.

2. **Logowanie**: Użytkownicy mogą zalogować się do swoich kont.

3. **Strona główna**: Wyświetla listę postów.

4. **Widok szczegółów posta**: Umożliwia użytkownikom przeglądanie pojedynczych postów.

5. **Widok postów autora**: Użytkownicy, po kliknięciu na nazwę autora posta mogą przejrzeć wszystkie jego posty.

### Dla zarejestrowanych użytkowników

5. **Tworzenie komentarzy**: Zarejestrowani użytkownicy mogą tworzyć komentarze do postów.

### Dla redaktorów

6. **Tworzenie postów**: Redaktorzy mogą tworzyć nowe posty.

7. **Edycja postów**: Redaktorzy mogą edytować swoje posty.

8. **Usuwanie postów**: Redaktorzy mogą usuwać swoje posty.

9. **Widok listy moich postów**: Redaktorzy mogą przeglądać listę swoich postów.

### Dla administratora

- **Panel administratora**: Administrator ma dostęp do panelu admina, gdzie może zarządzać użytkownikami, ich rolami i innymi ustawieniami.

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/aoibaraa/blog_internetowy.git
cd blog_internetowy
```

2. Zainstaluj wymagane pakiety:

```bash
pip install -r requirements.txt
```

3. Uruchom migrację:

```bash
python manage.py migrate
```

4. Utwórz superusera:

```bash
python manage.py createsuperuser
```

5. Uruchom serwer:

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem `http://localhost:8000/`.

## Użytkowanie
* Zaloguj się na konto superusera w panelu administracyjnym Django pod adresem `http://localhost:8000/admin/`.

* Dodaj innych użytkowników i nadaj im odpowiednie role.

* Zaloguj się jako redaktor i rozpocznij tworzenie i edycję postów.

* Zaloguj się jako czytelnik, aby przeglądać i komentować posty.

## Autorzy
Klaudia Sławińska, Krzysztof Wierzchowiecki

## Licencja
Program stworzony w celach edukacyjnych. 
