# Dnes je... v Instagram biu
> Program který každý den aktualizuje bio určitého Instagram profilu aby obsahovalo co je za den a kdo má svátek.

Používám [instagrapi](https://github.com/subzeroid/instagrapi) pro upravení profilu a k získání svátků a dat používám [svátky API](https://svatkyapi.cz/).
## Jak začít?
Je to jednoduché. Nejprve je potřeba si stáhnout kód, např. pomocí:
```
git clone https://github.com/Limit-sest/den-v-biu
```
Poté, v `main.py` je potřeba doplnit username a heslo účtu pro který chcete měnit bio.
```python
username = ""
password = ""
```
A teď by všechno (snad) mělo fungovat!

---
Nezaručuju že to nezablokuje daný účet, všechno je na vlastní nebezpečí!