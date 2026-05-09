from fpdf import FPDF
proyecto=input("Ingrese información de su proyecto: ")
horas_estimadas= input("Ingrese horas estimadas: ") 
valor_hora= input("Ingrese el valor de la hora trabajada: ")
termino= input("Ingrese el timepo estimado de finalización: ")

# Se calcula el precio 
total= int(horas_estimadas)*int(valor_hora)

pdf= FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("Template.png", x=0, y=0)

pdf.text(115, 145, proyecto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, termino)
pdf.text(115, 205, str(total))

pdf.output("Presupuesto.pdf")
print("Presupuesto generado exitosamente")