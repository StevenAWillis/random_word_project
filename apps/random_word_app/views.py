from django.shortcuts import render, HttpResponse, redirect
from  django.utils.crypto import get_random_string

def index(request):
    return render(request,'random_word_app/index.html')



def random_word(request):
    print("///////////////////////////////////")
    print("RUNNING RANDOM_WORD FUNCTION")
    random = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 1
    request.session['counter'] += 1
    context = {
        'random': random,
        'counter': request.session['counter']
    }
    return render(request,'random_word_app/index.html', context)

def random_word_reset(request):
    print("///////////////////////////////////")
    print("RESETTING COUNTER")
    request.session['counter'] = 0
    return redirect('/random_word')

# def some_function(request):
#     if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#         val_from_field_two = request.POST["two"]
#     if request.method == "GET":
#         print(request.GET)    
#     if request.method == "POST":
#         print(request.POST)    

#     request.session['name'] = request.POST['name']
#     request.session['counter'] = 100

#     return redirect('/')

