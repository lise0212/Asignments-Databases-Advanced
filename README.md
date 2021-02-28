# Scraper01

Zorg ervoor dat in je Virtual Machine (VM) python3 en pip3 hebt geïnstalleerd. 
Download met pip3 bs4 en pandas. 

Om te beginnen importeer ik alle nodige packages waaronder
- bs4 
- requests
- pandas
- time

Hierna maak ik een functie aan die alle informatie van de website gaat scrapen.
Hier importeer ik de url van de website via de requests package en maak ik een lege dataframe aan.
Daarna ga ik alle informatie scrapen, dit deel ik in vier kolommen (hash, hour, amountBTC & amountUSD). 
Deze data stop ik in een tweede dataframe die ik ga omkeren, de kolommen worden rijen en die rijen worden kolommen. Deze dataframe ga ik dan toevoegen aan de lege dataframe die ik eerder had gemaakt. 

Dan ga ik de data in de vierde (amountUSD) kolom (of 3e gezien we beginnen met tellen vanaf 0) vervangen. Het dollar teken verwijderen we en de komma vervangen we door niets. We zetten het type van de kolom als float zo kunnen we steeds het maximum bedrag van de kolom nemen. Dit resultaat return ik dan. 

Als laatste stap neem ik een loop hierin gaan we de functie uitvoeren en uitprinten en dan wachten we één minuut voor de volgende output. 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mongo02

Voor de tweede opdracht heb ik een bash file gemaakt die je kan runnen zodat Mongo wordt gedownload op je VM. Dit script kan je vinden onder de naam myscript_download.sh. In het pythonscript mongo02.py vind je de code die het gevraagde resultaat opslaagt in de database. Hoe we op het resultaat komen is hierboven reeds vermeld. Het verschil is dat ik nu eerst nog een nieuwe database aanmaak in mongo en hier ook een nieuwe collectie aan toevoeg. Wanneer ik dan op het resultaat kom door de website te scrapen zet ik het resultaat in de reeds aangemaakte collectie. Verder vind je nog myscript_run_realtime.sh, wanneer je deze file runt gaat het python script automatisch elke 60 seconden opnieuw runnen.
