import docx
from constants import reemplazos

def replaceInDoc():
    doc = docx.Document("./Pruebas del corrector.docx")

    for p in doc.paragraphs: 
        for r in reemplazos:
            p.text = p.text.replace(r[0], r[1])

    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        # Replace the text with your new text
                        a = run.text
                        run.text = run.text.replace(r[0], r[1])
                        print(a, run.text)

    doc.save('result1.docx')