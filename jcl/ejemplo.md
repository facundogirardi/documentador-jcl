# Documentación JCL: BORRACRE

## Paso 1: STEP1
### Programa
- `IEFBR14`
**Descripción:** Programa dummy que finaliza inmediatamente, usado para crear o borrar datasets.
### EXEC
- `//STEP1    EXEC PGM=IEFBR14`

### Datasets

| DDNAME | Definición |
|--------|------------|
| DD1 | DD DSN=FACUNDO.TEST.FILE, |

## Paso 2: STEP2
### Programa
- `IEFBR14`
**Descripción:** Programa dummy que finaliza inmediatamente, usado para crear o borrar datasets.
### EXEC
- `//STEP2    EXEC PGM=IEFBR14`

### Datasets

| DDNAME | Definición |
|--------|------------|
| DD1 | DD DSN=FACUNDO.TEST.FILE, |

## Paso 3: STEP3
### Programa
- `IEBGENER`
**Descripción:** Copia datasets secuenciales, útil para pruebas o generación de datos.
### EXEC
- `//STEP3    EXEC PGM=IEBGENER`

### Datasets

| DDNAME | Definición |
|--------|------------|
| SYSUT1 | DD * |
| SYSUT2 | DD DSN=FACUNDO.TEST.FILE, |
| SYSPRINT | DD SYSOUT=* |
| SYSIN | DD DUMMY |

