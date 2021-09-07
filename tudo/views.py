from django.shortcuts import render,redirect
from.models import  Tarea
from. forms import TF

def home(request):
	tareas =Tarea.objects.all()
	context={'tareas':tareas}
	return render (request,'tudo/home.html',context)

def agregar(request):
	if request.method == "POST":
		form = TF(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	
	else:
		form = TF()
		context ={'form':form}
	return render (request,'tudo/agregar.html',context)


def eliminar(request, tarea_id):
	tarea = Tarea.objects.get(id = tarea_id)
	tarea.delete()
	return redirect("home")


def editar(request,tarea_id):
	tarea = Tarea.objects.get(id = tarea_id)
	if request.method =="POST":
		form=TF(request.POST, instance=tarea)
		if form.is_valid():
			form.save()
			return redirect("home")

	else:
		form = TF(instance=tarea)

	context = {"form": form}
	return render (request, "tudo/editar.html",context)