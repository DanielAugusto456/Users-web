import os
from datetime import datetime
from pathlib import Path

class GeneradorReporteDesdeCarpeta:
    def __init__(self, carpeta_screenshots, carpeta_reportes="reportes"):
        self.carpeta_screenshots = carpeta_screenshots
        self.carpeta_reportes = carpeta_reportes
        self.pruebas = []
        
        os.makedirs(carpeta_reportes, exist_ok=True)
    
    def obtener_screenshots(self):
        screenshots = []
        if os.path.exists(self.carpeta_screenshots):
            for archivo in os.listdir(self.carpeta_screenshots):
                if archivo.lower().endswith('.png'):
                    # Extraer nombre de la prueba (sin extensión)
                    nombre_prueba = os.path.splitext(archivo)[0]
                    ruta_completa = os.path.join(self.carpeta_screenshots, archivo)
                    screenshots.append({
                        "nombre": nombre_prueba,
                        "archivo": archivo,
                        "ruta": ruta_completa
                    })
        return screenshots
    
    def generar_html(self, nombre_archivo="reporte.html"):
        
        # Obtener screenshots
        screenshots = self.obtener_screenshots()
        
        if not screenshots:
            print("⚠️ No se encontraron screenshots en la carpeta")
            return None
        
        # Leer template
        with open("template_reporte.html", "r", encoding="utf-8") as f:
            template = f.read()
        
        # Generar filas de la tabla
        filas = []
        for i, img in enumerate(screenshots, 1):
            # Ruta relativa para el HTML
            ruta_relativa = os.path.relpath(
                img["ruta"], 
                self.carpeta_reportes
            ).replace("\\", "/")
            
            fila = f"""
            <tr>
                <td>{i}</td>
                <td>{img['nombre']}</td>
                <td><span class="ver-screenshot" onclick="verScreenshot('{ruta_relativa}')">Ver imagen</span></td>
            </tr>
            """
            filas.append(fila)
        
        # Reemplazar placeholders
        ahora = datetime.now()
        html_final = template.replace("{{FECHA}}", ahora.strftime("%d/%m/%Y"))
        html_final = html_final.replace("{{HORA}}", ahora.strftime("%H:%M:%S"))
        html_final = html_final.replace("{{TOTAL}}", str(len(screenshots)))
        html_final = html_final.replace("{{FILAS_TABLA}}", "\n".join(filas))
        
        # Guardar archivo
        ruta_reporte = os.path.join(self.carpeta_reportes, nombre_archivo)
        with open(ruta_reporte, "w", encoding="utf-8") as f:
            f.write(html_final)
        
        print(f"Reporte generado: {ruta_reporte}")
        print(f"Total de screenshots: {len(screenshots)}")
        
        return ruta_reporte
    
if __name__ == '__main__':
    # Ruta de tu carpeta de screenshots existente
    carpeta_screenshots = r"C:\Users\marti\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\Itla\Cuatrimestre 5\Programacion 3\Proyectos\Users web\screenshots"
    
    reporte = GeneradorReporteDesdeCarpeta(
        carpeta_screenshots=carpeta_screenshots,
        carpeta_reportes="reportes"
    )
    
    reporte.generar_html("mi_reporte.html")