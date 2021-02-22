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

Run server: <code>source venv/bin/activate</code>

Deploy db changes: <code>heroku psql < database/schema.sql</code> 


Heroku
------
[FastResrve](https://fast-reserve.herokuapp.com) <br><br>
Moderator tunnarit: <br>
- login: 1212 <br>  
- password: 1212
