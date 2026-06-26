# home/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render

from .models import PDFDocument
from .forms import PDFUploadForm
from rag.ingest import ingest_pdf
from rag.vectorstore import delete_collection
from rag.retriever import retrieve
from rag.pileline import answer_question


@login_required
def home_view(request):

    if request.method == "POST":

        form = PDFUploadForm(request.POST, request.FILES)

        if form.is_valid():

            pdf = form.save(commit=False)

            pdf.user = request.user

            pdf.save()
            ingest_pdf(pdf)
            return redirect("home")

    else:

        form = PDFUploadForm()
    documents = request.user.documents.all()

    return render(
        request,
        "home.html",
        {
            "form": form,
            "documents": documents
        }
    )
    


@login_required
def chat_view(request, document_id):

    document = get_object_or_404(
        PDFDocument,
        id=document_id,
        user=request.user,
    )
    answer = None
    question = None
    if request.method == 'POST': 
        question = request.POST.get('question')
        answer = answer_question(
            document.id,
            question,
        )
       

    return render(
        request,
        "chat.html",
        {
            "document": document,
            "question": question,
            "answer": answer,
        },
    )
    
    


def delete_pdf(request, document_id):
    document = get_object_or_404(PDFDocument, id = document_id, user = request.user)
    if request.method == 'POST':
         delete_collection(f"document_{document_id}")
         document.file.delete(save=False)
         document.delete()
    return redirect("home")