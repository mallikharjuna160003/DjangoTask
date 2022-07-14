from django.contrib.auth import authenticate,login
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Tour,Profile,Address
from .serializers import UserCreateSerializer
# Create your views here.
def index(request):
    data = Tour.objects.all()
    context = { 'query_results' : data }
    return render(request,"index.html",context)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

########### register here #####################################
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})


def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})



#get all the users profile data
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def ProfileData(request):
    profiledata = Profile.objects.all()
    serializer = UserCreateSerializer(eventslist, many=True)
    return Response(serializer.data)

#create profile
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def ProfileCreate(request):
    serializer = UserCreateSerializer( data=request.data)
    if serializer.is_valid():
        print("data saved")
        serializer.save()
    else:
        print("Not valid")
    return Response(serializer.data)

#Update the event by pk:id
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def ProfileUpdate(request,pk):
    profiledata = Profile.objects.get(id=pk)
    serializer = UserCreateSerializer(instance = profiledata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

#delete the user by pk id
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def EventDelete(request,pk):
    eventslist = Events.objects.get(id=pk)
    eventslist.delete()
    return Response({"msg":"Event Deleted"})