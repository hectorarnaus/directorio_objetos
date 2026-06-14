class Provincia:
    def __init__(self,nombre,actividades,cabecera,cuerpo):
        self.nombre=nombre
        self.cabecera=cabecera
        self.cuerpo=cuerpo
        self.municipios=[]
        self.actividades=actividades
    
    def __str__(self):
        res=f"{self.nombre}\n{self.cabecera}\n{self.cuerpo}"
        aux="" 
        for actividad in self.actividades:
            aux+=actividad+"\n"
        return res+aux
        
    
    def anyade_municipio(self,municipio):
        self.municipios.append(municipio)
        
    
    
