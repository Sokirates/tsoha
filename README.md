# Keskustelusovellus

Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
* Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
* Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
* Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
* Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
* Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
* Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.

# nykyinen tilanne
- Käyttäjä näkee keskutelualueiden määrän
- Käyttäjä pystyy lisätä uuden keskustelualueen
- Käyttäjä näkee milloin keskustelualue on luotu
- Käyttäjä näkee keskustelualueen viestit
- Käyttäjä pystyy lisätä uuden viestin keskustelualueeseen
- Käyttäjä pystyy luoda käyttäjätunnuksen
- Käyttäjä pystyy kirjautumaan ja kirjautumaan ulos

# käynnistysohjeet

Kloonaa repostorio omalle koneellesi ja siirry juurikansioon virtuaali ympäristössä.

```bash
$ python3 -m venv venv
```
```bash
$ source venv/bin/activate
```
```bash
$ pip install -r ./requirements.txt
```
```bash
$ psql < schema.sql
```
Nyt pitäisi toimia sovellus komennolla
```bash
$ flask run
```
