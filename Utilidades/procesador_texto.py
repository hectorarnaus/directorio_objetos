class ProcesadorTexto:
    @staticmethod
    def extraer_parrafos(texto: str):
        trozos=texto.split("</p>")

        i=0
        while i<len(trozos):
            if "<p>" in trozos[i]:
                trozos[i]=trozos[i].replace("<p>","")
                trozos[i]=trozos[i].strip()
            i+=1
        return trozos
    
    @staticmethod
    def dividir_parrafo(parrafo: str):
        parrafos=parrafo.split(".")    
        if len(parrafos)==3:
            return [parrafos[0]+".",parrafos[1]+"."]
        else:
            primero=""
            for i in range(0,int(len(parrafos)/2)):
                primero+=parrafos[i]+"."
            segundo=""
            for i in range(int(len(parrafos)/2+1),len(parrafos)-1):
                segundo+=segundo[i]+"."
            return [primero,segundo]