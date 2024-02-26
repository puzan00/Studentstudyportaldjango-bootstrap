from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def todo_list(request):
    # Retrieve and display a list of todos associated with the current user
    todos = Todo.objects.filter(user=request.user)
    return render(request, "todo.html", {"todos": todos})


# for creating the todos
@login_required
def todo_create(request):
    try:
        if request.method == "POST":
            # If the form is submitted, validate and save the todo
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                todo.save()
                messages.success(request, "Todo created successfully.")
                return redirect("todo")
        else:
            # If the request method is not POST, display a blank form
            form = TodoForm()
    except Exception as e:
        messages.error(request, f"Error creating todo: {str(e)}")
    return render(request, "todo_form.html", {"form": form})


# for updating the todos
@login_required
def todo_update(request, pk):
    try:
        # Retrieve the todo to be updated
        todo = get_object_or_404(Todo, pk=pk)
        if request.method == "POST":
            # If the form is submitted, validate and update the todo
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                messages.success(request, "Todo updated successfully.")
                return redirect("todo")
        else:
            # If the request method is not POST, display the existing todo in the form
            form = TodoForm(instance=todo)
    except Exception as e:
        messages.error(request, f"Error updating todo: {str(e)}")
    return render(request, "todo_form.html", {"form": form})


# for deleting the todos
@login_required
def todo_delete(request, pk):
    try:
        # Retrieve the todo to be deleted
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        messages.success(request, "Todo deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting todo: {str(e)}")
    return redirect("todo")


# Toggle the 'complete' status of the todo
@login_required
def todo_complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect("todo")


# Delete all the todos
@login_required
def todo_delete_all(request):
    Todo.objects.all().delete()
    return redirect("todo")
