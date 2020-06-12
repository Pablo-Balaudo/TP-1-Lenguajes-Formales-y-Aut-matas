
""" Con este codigo importamos una funcion para eliminar elementos duplicados de un array o lista sin que esta se desordene"""
from collections import OrderedDict

class Gramatica():
    
    ReglasGramaticales = {}
    Axioma = None

    def __init__(self, gramatica):
        
        """Constructor de la clase.
        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.
        ------------------------------
            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
        """

        ListaReglas = gramatica.split("\n")
        Antecedentes =  list(OrderedDict.fromkeys([(x.split(":"))[0] for x in ListaReglas]))
        self.ReglasGramaticales = {x:[y.split(":")[1] for y in ListaReglas if x == y.split(":")[0]]  for x in Antecedentes}
        self.Axioma = Antecedentes[0]
    pass


    def isLL1(self):
        """Verifica si una gramática permite realizar derivaciones utilizando
           la técnica LL1.

        Returns
        -------
        resultado : bool
            Indica si la gramática es o no LL1.
        """


        pass

    def parse(self, cadena):
        """Retorna la derivación para una cadena dada utilizando las
           producciones de la gramática y los conjuntos de Fi, Fo y Se
           obtenidos previamente.

        Parameters
        ----------
        cadena : string
            Cadena de entrada.

            Ejemplo:
            babc

        Returns
        -------
        devivacion : string
            Representación de las reglas a aplicar para derivar la cadena
            utilizando la gramática.
        """
        for antecedente, consecuentes in ReglasGramaticales.items():
            for consecuente in consecuentes:
                pass

            pass
        pass

    def ObtenerFirst(Regla):
  
      First = [] 
      """la Regla es un diccionario, su clave (antecedente) es un string y el consecuente debe ser un array o lista que contanga los elementos de la misma separados (por causa de los espacios)"""
      antecedente = list(Regla.keys())[0]
      consecuente = Regla[antecedente]

      PrimerElementoDelConsecuente = consecuente[0] 

      if "lambda" in consecuente:
        First.append("lambda")
      elif PrimerElementoDelConsecuente.islower():
        """si esta en misuscula, lo trataré como a un terminal y lo pondre en el First"""
        First.append(PrimerElementoDelConsecuente)
      else:    
        """ahora sabemos que PrimerElementoDelConsecuente es un no terminal"""
        for consecuente_1 in self.ReglasGramaticales[PrimerElementoDelConsecuente]:
          """recorro las reglas buscando cada consecuente que tenga el no terminal como antecedente, y sacamos su first"""
          NuevaRegla = { PrimerElementoDelConsecuente : consecuente_1.split(" ") }
          First.extend(ObtenerFirst(NuevaRegla))
    
        if "lambda" in First:         
          First.remove("lambda")
          consecuente.remove(PrimerElementoDelConsecuente)
          NuevaRegla = {antecedente : consecuente}
          if consecuente:
            First.extend(ObtenerFirst(NuevaRegla))
          else:
            First.append("lambda") 

      return list(OrderedDict.fromkeys(First))
   
    def ObtenerFollow(antecedente_1):
        """ Este if es para utilizar mas abajo y fasilitar el convocar el metodo de follow dentro de si mismo """
        if antecedente_1.islower():
            return [antecedente_1]

        Follow = []
  
        if antecedente_1 == Axioma:
            Follow.append("$")

        for antecedente_2, consecuentes in self.ReglasGramaticales.items():
            for consecuente_1 in consecuentes:
                
                consecuente_2 = consecuente_1.split(" ")
                """ recorremos cada consecuente de cada antecedente de las reglas buscando ul antecedente a sacar su follow """
                if antecedente_1 in consecuente_2 :
                    ubicacion = consecuente_2.index(antecedente_1)
                    tamaño_consecuente_2 = len(consecuente_2)
                    while (ubicacion + 1) < tamaño_consecuente_2:
                        SiguienteElemento = consecuente_2[ubicacion + 1]
                        if consecuente_2[ubicacion + 1].islower():
                            Follow.append(SiguienteElemento)
                            break
                        elif antecedente_1 != antecedente_2:
                            Follow.extend(ObtenerFirst({antecedente_2:list(SiguienteElemento)}))
                            if "lambda" in Follow:
                                Follow.remove("lambda")
                                Follow.extend(ObtenerFollow(SiguienteElemento))
                                ubicacion = ubicacion + 1
                    if ((ubicacion + 1) == tamaño_consecuente_2) and (antecedente_1 != antecedente_2):
                        Follow.extend(ObtenerFollow(antecedente_2))

  
        return  list(OrderedDict.fromkeys(Follow))

