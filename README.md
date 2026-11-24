# documentador-jcl

Script en **Python** que genera documentación en **Markdown** a partir de archivos **JCL** (Job Control Language de z/OS).

Por cada archivo `.jcl` de una carpeta genera un `.md` con el mismo nombre, que incluye:

* El nombre del **JOB**
* Cada **paso** (`EXEC`) con su programa y una descripción de las utilidades más comunes (IEFBR14, SORT, IDCAMS, IEBGENER, IEBCOPY, IKJEFT01, DSNUTILB, etc.)
* Los **comentarios** (`//*`) que preceden a cada paso
* Una tabla con los **datasets** (`DD`) de cada paso

## Requisitos

* Python 3.8 o superior
* No usa librerías externas

## Uso

```bash
git clone https://github.com/facundogirardi/documentador-jcl.git
cd documentador-jcl
python documentador.py jcl
```

El script recibe la carpeta que contiene los `.jcl` y guarda cada `.md` al lado de su `.jcl`. Los archivos se leen y se escriben en UTF-8.

## Ejemplo

La carpeta [`jcl/`](jcl/) tiene un JCL de ejemplo ([`ejemplo.jcl`](jcl/ejemplo.jcl)) y la documentación que genera el script ([`ejemplo.md`](jcl/ejemplo.md)).

## Agregar programas

Las descripciones de los programas están en el diccionario `PROGRAM_DESCRIPTIONS` de `documentador.py`. Para documentar otro programa alcanza con agregar una entrada:

```python
PROGRAM_DESCRIPTIONS = {
    ...
    "MIPGM01": "Descripción del programa propio.",
}
```
