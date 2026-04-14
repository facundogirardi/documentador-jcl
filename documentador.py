# jcl_doc.py
import os
import sys

PROGRAM_DESCRIPTIONS = {
    "IEFBR14": "Programa dummy que finaliza inmediatamente, usado para crear o borrar datasets.",
    "SORT": "Ordena registros de un dataset según criterios definidos en SYSIN.",
    "IDCAMS": "Utility para administrar catálogos y datasets VSAM (definir, borrar, listar).",
    "IEBGENER": "Copia datasets secuenciales, útil para pruebas o generación de datos.",
    "IEBCOPY": "Copia y reorganiza miembros de librerías PDS.",
    "IEBPTPCH": "Imprime datasets secuenciales o miembros de PDS en formato legible.",
    "IEHLIST": "Lista información de volúmenes y datasets.",
    "DFSRRC00": "Programa de control para ejecutar aplicaciones IMS.",
    "DSNUTILB": "Utility de DB2 para ejecutar comandos y tareas de mantenimiento.",
    "IKJEFT01": "TSO en batch, permite ejecutar comandos CLIST/REXX o SQL.",
    "FTP": "Cliente FTP en batch para transferir archivos entre sistemas.",
}

def describe_program(program: str) -> str:
    return PROGRAM_DESCRIPTIONS.get(
        program,
        "Descripción no disponible, consultar documentación oficial."
    )

def parse_jcl(jcl_text: str) -> dict:
    lines = jcl_text.splitlines()
    job_name = None
    steps = []
    current_comments = []
    current_step = None

    for line in lines:
        line = line.rstrip()
        if line.startswith("//*"):  # comentario
            current_comments.append(line.lstrip("//*").strip())
        elif line.startswith("//") and "JOB" in line:
            job_name = line.split()[0].replace("//", "")
        elif line.startswith("//") and "EXEC" in line:
            if current_step:
                steps.append(current_step)
            parts = line.split()
            step_name = parts[0].replace("//", "")
            pgm = [p for p in parts if p.startswith("PGM=")]
            current_step = {
                "name": step_name,
                "exec": line.strip(),
                "program": pgm[0].split("=")[1] if pgm else None,
                "comments": current_comments.copy(),
                "dds": []
            }
            current_comments.clear()
        elif line.startswith("//") and "DD" in line and current_step:
            parts = line.split()
            ddname = parts[0].replace("//", "")
            current_step["dds"].append({"ddname": ddname, "definition": " ".join(parts[1:])})

    if current_step:
        steps.append(current_step)

    return {"job": job_name, "steps": steps}

def to_markdown(parsed: dict) -> str:
    md = f"# Documentación JCL: {parsed['job']}\n\n"
    for i, step in enumerate(parsed["steps"], 1):
        md += f"## Paso {i}: {step['name']}\n"
        if step["comments"]:
            md += "### Comentarios\n"
            for c in step["comments"]:
                md += f"- {c}\n"
        md += f"### Programa\n- `{step['program']}`\n"
        md += f"**Descripción:** {describe_program(step['program'])}\n"
        md += f"### EXEC\n- `{step['exec']}`\n"
        if step["dds"]:
            md += "\n### Datasets\n\n| DDNAME | Definición |\n|--------|------------|\n"
            for ds in step["dds"]:
                md += f"| {ds['ddname']} | {ds['definition']} |\n"
        md += "\n"
    return md

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python jcl_doc.py carpeta_con_jcls")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"⚠️ No es una carpeta válida: {folder}")
        sys.exit(1)

    files = [f for f in os.listdir(folder) if f.lower().endswith(".jcl")]
    if not files:
        print("⚠️ No se encontraron archivos .jcl en la carpeta.")
        sys.exit(1)

    for jcl_file in files:
        path = os.path.join(folder, jcl_file)
        with open(path) as f:
            jcl = f.read()
        parsed = parse_jcl(jcl)
        md_output = to_markdown(parsed)

        base_name = os.path.splitext(jcl_file)[0]
        output_file = os.path.join(folder, base_name + ".md")

        with open(output_file, "w") as out:
            out.write(md_output)

        print(f"✅ Documentación generada: {output_file}")
