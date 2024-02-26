from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def calculator(request):
    # Check if the request method is POST (indicating form submission)
    if request.method == "POST":
        try:
            first_number = float(request.POST.get("first_number", 0))
            expression = request.POST.get("expression", "+")
            second_number = float(request.POST.get("second_number", 0))

            # Perform the calculation based on the selected expression
            if expression == "+":
                result = first_number + second_number
            elif expression == "-":
                result = first_number - second_number
            elif expression == "*":
                result = first_number * second_number
            elif expression == "/":
                if second_number == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = first_number / second_number
            elif expression == "%":
                result = first_number % second_number
            else:
                result = None

        except ZeroDivisionError as e:
            # Display an error message if division by zero occurs
            messages.error(request, f"Error: {e}")
            return render(request, "calculator.html")

        # If no errors occurred, display a success message and render the result
        messages.success(request, f"Calculation successful.")
        return render(
            request,
            "calculator.html",
            {
                "first_number": first_number,
                "expression": expression,
                "second_number": second_number,
                "result": result,
            },
        )

    # If the request method is not POST, simply render the empty calculator form
    else:
        return render(request, "calculator.html")
