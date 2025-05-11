from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'Crud/book_form.html', {'form': form})

# Read
def list_books(request):
    books = Book.objects.all()
    return render(request, 'Crud/book_list.html', {'books': books})

# Update
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'Crud/book_form.html', {'form': form})

# Delete
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'Crud/book_confirm_delete.html', {'book': book})
