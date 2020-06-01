
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
        Antecedentes = [x[0] for x in ListaReglas]
        self.ReglasGramaticales = {x[0]:[y[2:len(y)] for y in ListaReglas if x[0] == y[0]]  for x in Antecedentes}
        self.Axioma = Antecedentes[0]
    pass

    def ObtenerFirst(Regla):
  
      First = []
      Consecuente = Regla[2:len(Regla)]
      PrimerElementoDelConsecuente = Consecuente.split(" ")[0]
  
      if ("lambda" in Consecuente) or Consecuente == "":
        First.append("lambda")
      elif PrimerElementoDelConsecuente.islower():
        First.append(PrimerElementoDelConsecuente)
      else:    
    
        NoTerminal = PrimerElementoDelConsecuente

        for consecuente in ReglasGramaticales[NoTerminal]:
          NuevaRegla = NoTerminal + ":" + consecuente
          First.extend(ObtenerFirst(NuevaRegla))
    
        if "lambda" in First:      
      
          First.remove("lambda")

          if (NoTerminal + " ") in Regla:
            NuevaRegla = Regla.replace((NoTerminal + " "), "")
          else:
            NuevaRegla = Regla.replace(NoTerminal , "")
          NuevoConsecuente = NuevaRegla[2:len(Regla)]
      
      
          if NuevoConsecuente != "":
            First.extend(ObtenerFirst(NuevaRegla))
          else:
            First.append("lambda") 

      return set(First) 


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
        pass
