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

Myös sovelluksesta löytyy oma vuokraushistoriaa.


Heroku
------
[FastResrve](https://fast-reserve.herokuapp.com) <br><br>
Moderator tunnarit: <br>
- login: 1212 <br>  
- password: 1212

Asennus
------
<code> git clone https://github.com/olegTervo/tyovuorolista.git </code>

Create virtual environment: <br><code> python3 -m venv venv </code>

Run server: <br><code>source venv/bin/activate</code>

Install requirements: <br><code>pip install -r requirements.txt</code>

Deploy db changes: <br><code>[heroku] psql < database/schema.sql</code> 
