from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.forms import NameForm
import requests
from .models import Chat
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data['your_name'])
            name = form.cleaned_data['your_name']
            text =  f"https://api.dialogflow.com/v1/query?v=20150910&contexts=smalltalk&lang=en&query={name}&sessionId=12345&timezone=America/New_York"

            Headers= {
                'Authorization' : 'Bearer 57122c63c23e49088bdeef2a187ff625',

                }
            r= requests.get(text, headers= Headers)
            print(r.json())
            res = r.json()['result']['fulfillment']['speech']
            print(res)
            Chat.objects.create(content1=name, content2= res)

            # url = f'utlhtotjquery=name&.....'
            # auth...
            # r = requests(url,header)
            #  res = r.json()....
            # chat.objects.create(content1=name,content2=res)
            #chat.save (if above code gives problem)

            return HttpResponseRedirect('/test/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        data = {
            'form': form,
            'chats': Chat.objects.all()
        }

    return render(request, 'blog/test.html', {'data': data})



