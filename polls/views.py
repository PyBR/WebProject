from django.shortcuts import render

from .models import Poll
# Create your views here.
def polls_list(request):


#Renderiza a poll_list.html que lista todas as polls disponiveis .
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)