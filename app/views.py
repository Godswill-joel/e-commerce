from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, 'app.html', {})


def cart(request):
    return render(request, 'cart.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})