
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
      """la regla es un diccionario, su clave (antecedente) es un string y el consecuente debe ser un array o lista que contanga los elementos de la misma separados (por causa del espacio)"""
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
        for NuevoConsecuente in ReglasGramaticales[PrimerElementoDelConsecuente]:
          """recorro las reglas buscando cada consecuente que tenga a """
          NuevaRegla = { PrimerElementoDelConsecuente : NuevoConsecuente.split(" ") }
          First.extend(ObtenerFirst(NuevaRegla))
    
        if "lambda" in First:         
          First.remove("lambda")
          consecuente.remove(PrimerElementoDelConsecuente)
          NuevaRegla = {antecedente : consecuente}
          if NuevoConsecuente:
            First.extend(ObtenerFirst(NuevaRegla))
          else:
            First.append("lambda") 

      return list(OrderedDict.fromkeys(First))
    def ObtenerFollow(Antecedente):
  
      Follow = []
  
      if Antecedente == Axioma:
        Follow.append("$")

      for antecedente, consecuentes in ReglasGramaticales:
        if Antecedente in consecuentes:
            x = 1
      return  list(OrderedDict.fromkeys(Follow))

