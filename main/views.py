from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Kicks Archive',
        'name': 'Samuel Marcelino Tindaon',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)