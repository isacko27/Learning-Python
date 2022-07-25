#Ingresa un Texto (text)
#Ingresa 3 letras a su eleccion ej: a,b,c
#Devolver informacion------
#1 Cuantas veces aparece cada letra count() upper
#2 Cuantas palabras hay en total
#3 Primera y ultima letra
#4 Como quedaria el Texto si lo invirtieramos
#5 Aparece python?

text = """El amor es una experiencia universal que nos conmueve a todos, pero a veces no hallamos las 
palabras adecuadas para expresarlo. A lo largo de la historia los poetas han sabido decir aquello que 
todos sentimos de formas creativas y elocuentes."""

print("Texto a escanear: \n" + text + "\n")
letras = [input("Primera letra: "),input("Segunda letra: "),input("Tercera letra: ")]

lowertext = text.lower()
counting1 = lowertext.count(letras[0].lower())
counting2 = lowertext.count(letras[1].lower())
counting3 = lowertext.count(letras[2].lower())

palabras_tot = len(text.split(" "))

pip = "python" in text

texto_inv = text[::-1]

print("------------------------------------------------------------------------")
print(f"""Bueno broda mira, ya escaneamos tu texto y los resultados que tira el servidor son\n
      Estas son el numero de veces que aparecen las letras que seleccionaste:"
      {letras[0]}: {counting1}
      {letras[1]}: {counting2}
      {letras[2]}: {counting3}
\n Dicho eso cabe mencionar que el numero de palabras de el texto es:
      {palabras_tot}
\n Ahora la pregunta dentro de el texto aparece la palabra \"Python\"?
      {pip}
      
\n Y weno para terminar asi se veria si invertimos tu texto, asi al reves bien chulo: \n
      {texto_inv}
      \n------------------------------------------------------------------------
      ALV igualito a una invocacion diabolica
      Bueno serian 100 pesacos por el trabajo
      --------------------------------------------------------------------------""")

