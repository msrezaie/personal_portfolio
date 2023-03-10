from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Operation, Page
from base.models import Profile
import json
import importlib

@csrf_exempt  # disable CSRF protection
def index(request):
    if request.method == 'POST':  # check if request method is POST
        # Get JSON data from request body and decode it
        recieved_data = json.loads(request.body.decode("utf-8"))

        # Extract keys, cipher, method, and text values from the received JSON data
        keys, cipher, method, text = recieved_data['keys'], recieved_data['cipher'], recieved_data['method'], recieved_data['text']

        try:
            # Import the module for the specified cipher
            module = importlib.import_module(f'cryptoden.ciphers.{cipher}')

            # Get the function for the specified encryption/decryption method
            cipher_function = getattr(module, method)

            # Call the specified cipher function with the provided text and keys
            result = cipher_function(text, keys)
            
            # Return the encrypted/decrypted text as an HTTP response
            return HttpResponse(result)

        except ImportError:
            # If the specified cipher module could not be found, print an error message
            print(f"Error: the cipher '{cipher}' was not found.")

    operation = Operation.objects.all()
    page = Page.objects.first()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'operations': operation,
        'pages': page
    }

    return render(request, "cryptoden/index.html", context)