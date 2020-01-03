from django.shortcuts import render, redirect
from django.contrib	import messages
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Document


def home(request):
	documents = Document.objects.all()
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your file has been uploaded!')
		return redirect('/')
	else:
		form = DocumentForm()

		return render(request, 'home.html', {'form':form, 'documents': documents})

def about(request):
	return render(request, 'about.html')

def documents(request):
	return render(request, 'documents.html')
