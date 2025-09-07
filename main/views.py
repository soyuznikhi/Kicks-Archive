from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406435830',
        'name': 'Samuel Marcelino Tindaon',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)