# Keskustelusovellus

Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä.

Sovelluksen ominaisuuksia:

* Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen luojan, tykkäykset ja kävijämäärän.
* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Kirjauduttua sisään käyttäjä voi luoda uuden keskustelualueen antamalla aiheen, kirjoittaa uuden viestin olemassa olevaan alueeseen ja tykätä keskustelualueesta.
* Käyttäjä voi kuitenkin mennä keskustelualueeseen ilman kirjautumista sisään.

# Käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```bash
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r ./requirements.txt
```
Määritä vielä tietokannan skeema komennolla
```bash
psql < schema.sql
```
Nyt voit käynnistää sovelluksen komennolla
```bash
flask run
```
