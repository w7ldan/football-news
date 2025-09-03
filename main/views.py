from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406396590',
        'name': 'Wildan Anshari Hidayat',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
