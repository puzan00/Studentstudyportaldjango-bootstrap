from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Notes
from .forms import NoteForm


@login_required
def notes(request):
    # Retrieve and display a list of notes associated with the current user
    notes_list = Notes.objects.filter(user=request.user)
    return render(request, "notes.html", {"notes_list": notes_list})


@login_required
def note_create(request):
    try:
        if request.method == "POST":
            # If the form is submitted, validate and save the note
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.user = request.user
                note.save()
                messages.success(request, "Note created successfully.")
                return redirect("notes")
        else:
            # If the request method is not POST, display a blank form
            form = NoteForm()
    except Exception as e:
        messages.error(request, f"Error creating note: {str(e)}")
    return render(request, "note_form.html", {"form": form})


# for updating the note
@login_required
def note_update(request, id):
    try:
        note = get_object_or_404(Notes, id=id, user=request.user)
        if request.method == "POST":
            # If the form is submitted, validate and update the note
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                messages.success(request, "Note updated successfully.")
                return redirect("notes")
        else:
            # If the request method is not POST, display the existing note in the form
            form = NoteForm(instance=note)
    except Exception as e:
        messages.error(request, f"Error updating note: {str(e)}")
    return render(request, "note_form.html", {"form": form})


# for deleting the note
@login_required
def note_delete(request, id):
    try:
        note = get_object_or_404(Notes, id=id, user=request.user)
        note.delete()
        messages.success(request, "Note deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting note: {str(e)}")
    return redirect("notes")
