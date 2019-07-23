from django.shortcuts import render

# Create your views here.
#viwes é uma função entao criamos com def
def pagina_inicial(request):
    context = {"nome" : "Maria" , "cachorro" : ["mel", "tobias" , "cacau" ,"bob" , "madona" , "Snopy"]}
    return render(request,'index.html', context) #request 
