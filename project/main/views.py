from django.shortcuts import render
from main.models import *

def delete():
    film = Film.objects.all()
    newspapers = Newspapers.objects.all()

    lst = [film,newspapers]

    for model in lst:
        for i in range(0,len(model),1):
            if model[i].pk % 2 != 0:
                temp = model[i]
                temp.delete()