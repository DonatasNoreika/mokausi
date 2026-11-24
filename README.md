# Mokausi – Odoo 18 modulis

Rodo mokymosi svetainę adresu `/mokausi`. Naujas svetainės versijas galima įkelti per Odoo, nekeičiant failų serveryje.

## Įdiegimas (Windows, Odoo 18)
1. Nukopijuok visą katalogą `mokausi` į Odoo modulių katalogą, pvz.
   `C:\Program Files\Odoo 18.0.20250707\server\odoo\addons\`
   (tikslus kelias priklauso nuo diegimo; ten rasi kitus modulius, pvz. `website`).
2. Perkrauk Odoo: Windows „Paslaugos“ (services.msc) → Odoo paslauga → Restart.
3. Odoo: Nustatymai → Aktyvuoti kūrėjo režimą.
4. Programos → „Atnaujinti programų sąrašą“ → paieškoje nuimk filtrą „Programos“, įvesk „Mokausi“ → Aktyvuoti.
5. Atidaryk `https://tavo-svetainė/mokausi`.

## Įdėjimas į svetainę
- Meniu: svetainės redaktoriuje spausk meniu → „Redaguoti meniu“ → pridėk punktą su nuoroda `/mokausi`.
- Į bet kurį kitą puslapį: blokas „Embed Code“ (Inner Content) → Edit → įklijuok:
  `<iframe src="/mokausi/app" style="width:100%;height:90vh;border:0" allowfullscreen></iframe>`

## Naujos versijos įkėlimas
Mokausi → Svetainės versijos → Naujas → pavadinimas, `index.html` failas, „Kas pasikeitė“ → Išsaugoti.
Nauja versija iškart rodoma svetainėje. Senesnę grąžinsi mygtuku „Rodyti šią versiją svetainėje“.

## Progresas
Prisijungusio naudotojo progresas saugomas Odoo (Mokausi → Progresas) ir matomas visuose įrenginiuose.
Neprisijungus progresas saugomas tik toje naršyklėje. Sūnui galima sukurti portalo paskyrą
(Kontaktai → kontaktas → Veiksmai → Suteikti portalo prieigą) arba naudotis tavo paskyra.
