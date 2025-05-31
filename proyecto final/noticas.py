import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
class Noticia:
    def __init__(self, texto: str, categoria: str): #__init__ constructor
        self.texto = texto
        self.categoria = categoria

    def __str__(self):
        return f"Categoría: {self.categoria}, Noticia: {self.texto}"

class Nodo:
    def __init__(self, noticia: Noticia, izq=None, der=None):
        self.noticia = noticia
        self.izq = None
        self.der = None
class ArbolBinario:
    def __init__(self, raiz=None) -> None:
        self.raiz = raiz

    def insertar(self, noticia) -> None:
        if self.raiz is None:
            self.raiz = Nodo(noticia)
        else:
            self._insertar(noticia, self.raiz)

    def _insertar(self, noticia, nodo) -> None:
        if noticia.texto.lower() < nodo.noticia.texto.lower():
            if nodo.izq is None:
                nodo.izq = Nodo(noticia)
            else:
                self._insertar(noticia, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(noticia)
            else:
                self._insertar(noticia, nodo.der)

    def buscar(self, texto) -> bool:
        return self._buscar(texto, self.raiz)

    def _buscar(self, texto, nodo) -> bool:
        if nodo is None:
            return None
        if texto.lower() == nodo.noticia.texto.lower():
            return nodo
        elif texto.lower() < nodo.noticia.texto.lower():
            return self._buscar(texto, nodo.izq)
        else:
            return self._buscar(texto, nodo.der)
        
    def inorden(self) -> None:
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo) -> None:
        if nodo.izq is not None:
            self._inorden(nodo.izq)
        print(nodo.noticia)
        if nodo.der is not None:
            self._inorden(nodo.der)
    
    def buscar_por_categoria(self, categoria_buscada):
        noticias = []
        self._buscar_categoria(self.raiz, categoria_buscada, noticias)
        return noticias
    
    def _buscar_categoria(self, nodo, categoria, lista):
        if nodo:
            if nodo.noticia.categoria.lower() == categoria.lower():
                lista.append(nodo.noticia)
            self._buscar_categoria(nodo.izq, categoria, lista)
            self._buscar_categoria(nodo.der, categoria, lista)

class Clasificador:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=2000)
        self.modelo = MultinomialNB()
        
    def entrenar(self, textos, categorias):
        X = self.vectorizer.fit_transform(textos) #aprender vocabulario
        self.modelo.fit(X, categorias)
        
    def predecir(self, texto):
        X = self.vectorizer.transform([texto])
        categoria = self.modelo.predict(X)[0]
        confianza = max(self.modelo.predict_proba(X)[0]) * 100 #max optiene la probabilidad mas alta
        return categoria, confianza

noticias = pd.read_csv('proyecto final/noticias_clasificadas.csv')

arbol = ArbolBinario()
for index, row in noticias.iterrows():
    noticia = Noticia(row['Noticia'], row['Categoría'])
    arbol.insertar(noticia)

clasificador = Clasificador()
clasificador.entrenar(noticias['Noticia'].tolist(), noticias['Categoría'].tolist())

while True:
    print("\n--- MENÚ ---")
    print("1. Clasificar nueva noticia")
    print("2. Buscar noticia exacta")
    print("3. Ver noticias por categoría")
    print("4. Ver todas las noticias ordenadas")  
    print("5. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        texto = input("Ingresa la noticia: ")
        if texto.strip(): #script elimina espacios
            categoria, confianza = clasificador.predecir(texto)
            print(f"Categoría: {categoria} (Confianza: {confianza:.1f}%)")
            
            nueva_noticia = Noticia(texto, categoria)
            arbol.insertar(nueva_noticia)
            print("Noticia agregada al árbol.")
    
    elif opcion == "2":
        texto = input("Texto exacto a buscar: ")
        nodo = arbol.buscar(texto)
        if nodo:
            print(f"Encontrada: {nodo.noticia}")
        else:
            print("No encontrada.")
    
    elif opcion == "3":
        categoria = input("Categoría a buscar: ")
        noticias = arbol.buscar_por_categoria(categoria)
        if noticias:
            print(f"\nNoticias de '{categoria}' ({len(noticias)}):")
            for noticia in noticias:
                print(f"• {noticia.texto}")
        else:
            print("No se encontraron noticias de esa categoría.")
    
    elif opcion == "4":
        print("\n--- Noticias ordenadas ---")
        arbol.inorden()  
    
    elif opcion == "5":
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida.")
