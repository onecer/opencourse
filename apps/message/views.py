from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def get_form(request):
    # user_message = UserMessage.objects.filter(id=1)
    # user_message = UserMessage.objects.all()
    # user_message.delete()
    # for message in user_message:
    #     message.delete()
    # UserMessage.objects.all()
    # UserMessage.objects.all().values('name')
    # UserMessage.objects.all().values_list('id', 'name')
    # UserMessage.objects.get(id=1)
    # UserMessage.objects.get(name='bob')
    if request.method == 'POST':
        user_message = UserMessage()
        user_message.name = request.POST.get('name', '')
        user_message.email = request.POST.get('email', '')
        user_message.address = request.POST.get('address', '')
        user_message.message = request.POST.get('message', '')
        user_message.save()

    user_message = UserMessage.objects.filter(id=1)
    return render(request, 'message_form.html', {
        'user_message': user_message[0],
    })
