# Automatización de Presupuestos en PDF con Python 

Este proyecto fue mi primera práctica de automatización desarrollada en el marco de la formación con **Daxus Latam**. El objetivo fue crear una herramienta funcional que resuelva una tarea administrativa común mediante el uso de scripts de Python.

## Características
- **Cálculo Automático:** El script calcula el costo total del proyecto multiplicando las horas estimadas por el valor de la hora de forma interna.
- **Formato Profesional:** Utiliza la librería `fpdf` para posicionar el texto con precisión sobre una plantilla de diseño (`Template.png`).
- **Interactividad:** Entrada de datos dinámica por consola para personalizar cada presupuesto.

## Tecnologías utilizadas
- **Lenguaje:** Python 3.x
- **Librería:** `fpdf` (para la creación y manipulación de documentos PDF).
- **Diseño:** Integración de activos gráficos externos (Plantilla corporativa).

## Cómo funciona
1. El script solicita al usuario:
   - Información descriptiva del proyecto.
   - Horas de trabajo estimadas.
   - Valor de la hora trabajada (USD).
   - Tiempo de entrega estimado.
2. Calcula automáticamente el **Total**.
3. Genera un archivo llamado `Presupuesto.pdf` con todos los campos completados en sus coordenadas correspondientes.

## Próximas Mejoras (Roadmap)
- [ ] Validación de entradas de datos para evitar errores de tipo.
- [ ] Opción para elegir entre diferentes plantillas de diseño.
- [ ] Envío automático del PDF generado por correo electrónico (integración con `smtplib`).

---
*Proyecto desarrollado para optimizar procesos de consultoría y gestión administrativa.*
