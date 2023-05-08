
from Notebook import Notebook
from Desktop import Desktop

desktop = Desktop("Dell Inspiron", "Preto", 3500, 500)
notebook = Notebook("Lenovo Ideapad", "Cinza", 2800, 6)

print(desktop.getInformacoes())
print(notebook.getInformacoes())

desktop.cadastrar()
notebook.cadastrar()