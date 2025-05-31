from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ebook, Chapter
from store.models import Category
from .forms import EbookForm, ChapterForm

def ebook_view(request):
    ebooks = Ebook.objects.all().order_by('-created_at')

    if request.user.is_authenticated:
        my = Ebook.objects.filter(author=request.user)
        
        return render(request, 'ebook/home.html', {'ebooks': ebooks, 'my':my})
    return render(request, 'ebook/home.html', {'ebooks':ebooks})

@login_required
def add_ebook(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save(commit=False)
            ebook.author = request.user
            ebook.save()
            form.save_m2m()
            messages.success(request, 'Ebook added successfully!')
            return redirect('ebook')
    else:
        form = EbookForm()

    if request.user.is_superuser:
        return render(request, 'ebook/add_ebook.html', {'form': form})
    return redirect('ebook')

@login_required
def delete_ebook(request, id):
    ebook = get_object_or_404(Ebook, id=id)
    if request.user != ebook.author:
        messages.error(request, 'You are not authorized to delete this ebook!')
        return redirect('ebook')
    
    if request.method == 'POST':
        ebook.delete()
        messages.success(request, 'Ebook deleted successfully!')
        return redirect('ebook')
    
    return render(request, 'ebook/confirm_delete.html', {'ebook': ebook})

@login_required
def update_ebook(request, id):
    ebook = get_object_or_404(Ebook, id=id)
    if request.user != ebook.author:
        messages.error(request, 'You are not authorized to edit this ebook!')
        return redirect('ebook')
    
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ebook updated successfully!')
            return redirect('ebook_details', id=ebook.id)
    else:
        form = EbookForm(instance=ebook)
    
    return render(request, 'ebook/update_ebook.html', {'form': form, 'ebook': ebook})

def ebook_details(request, id):
    ebook = get_object_or_404(Ebook, id=id)
    is_author = request.user == ebook.author

    # Get the first chapter (or None if no chapter exists)
    first_chapter = ebook.chapters.first()

    return render(request, 'ebook/ebook_details.html', {
        'ebook': ebook,
        'is_author': is_author,
        'chapter': first_chapter  
    })



def read_chapter(request, ebook_id, chapter_id):
    ebook = get_object_or_404(Ebook, id=ebook_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, ebook=ebook)

    all_chapters = list(ebook.chapters.all())
    index = all_chapters.index(chapter)
    
    prev_chapter = all_chapters[index - 1] if index > 0 else None
    next_chapter = all_chapters[index + 1] if index < len(all_chapters) - 1 else None

    return render(request, 'ebook/read_chapter.html', {
        'ebook': ebook,
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter
    })


@login_required
def add_chapter(request, ebook_id):
    ebook = get_object_or_404(Ebook, id=ebook_id, author=request.user)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.ebook = ebook
            chapter.save()
            messages.success(request, "Chapter added!")
            return redirect('ebook_details', id=ebook.id)
    else:
        form = ChapterForm()
    return render(request, 'ebook/add_chapter.html', {'form': form, 'ebook': ebook})
