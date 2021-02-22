# FastReserve

FastReserve on web sovellus, jossa käyttäjä voi vuokrata jotain:
- välinet 
- autot
- konsolipelit
- saunat
- mökit
- palvelut
...

On kaksi käyttäjäärooleja, user ja moderator. Moderator voi luoda ilmoitukset, user ei.

Ilmoitus on post tyyppinen, siinä on valokuva, nimi, teksti, info milloin se on saatavilla ja author.
Ilmoitukset ovat ryhmitelty tyypin mukaan (kodinkoneet, vaateet,...) ja sen Ryhmän mukaan.
Ryhmä voi olla esim kauppa tai ihan joku ryhmä, jossa on joku osa ilmoituksista. Sen voi lisätä itselle, että jotkut tuotteet ovat helposti saatavia, ilman globaalihakua.

## Heroku demo palvelin

[FastResrve](https://fast-reserve.herokuapp.com) <br><br>
Moderator tunnarit: <br>
- login: 1212 <br>  
- password: 1212

## Tilaa

 - On olemassa 2 käyttäjärooleja: user, moderator
 - Kirautumisjärjestelmä perustietoturvallisudella: 
   - salattu salasana myös tietokannassa
 - Käyttäjä voi luoda, muokkaa ja poistaa ilmoitukset
   - CRUD (Moderator), R (User)
 - Käyttäjä voi luoda, muokkaa ja poistaa ryhmät
   - CRUD (Moderator), R (User)
 - Myös jokainen ilmoitus tai ryhmä voi olla julkinen tai ei
   - Julkiset näkee muut käyttäjät
   - Tilan voi vaihtaa myöhemmin (Moderator)
 - Ryhmään kuuluu Käyttäjät ja Ilmoitukset niin
   - Ryhmässä voi olla monta Käyttäjää
   - Myös Käyttäjällä voi olla monta Ryhmää
   - Ryhmässä on monta Ilmoitusta
   - Ilmoitus voi kuullaa moneen ryhmii
 - Sen takia on tehty ChannelUser ja ChannelItem taulut tietokantaan
 - Ryhmään voi lisätä käyttäjän ID:lla (Oma ID näkee etusivulla)
 - Ilmoituksia voi tehdä ryhmässä, että ne kuulu ryhmään

## TODO

  - Varaus tietokantataulu
  - Historiaa
  - Calenteri
  - Olemassa olevan Ilmoituksen lisäminen ryhmään
  - Pilvi palvelin kuvien takia
  - E-mail form -> WhatsUp form
  - Keskustelut
  - Kiellisyydet ( en, ru )
  - Oma profiili
  - Testit

## Asennus omaan kehitysympäristöön

<code> git clone https://github.com/olegTervo/tyovuorolista.git </code>

Create virtual environment: <br><code> python3 -m venv venv </code>

Run server: <br><code>source venv/bin/activate</code>

Install requirements: <br><code>pip install -r requirements.txt</code>

Deploy db changes: <br><code>[heroku] psql < database/schema.sql</code> 
