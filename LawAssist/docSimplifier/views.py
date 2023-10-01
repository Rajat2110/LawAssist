from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,logout
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as dj_login
from django.views.decorators.cache import cache_control
from PyPDF2 import PdfReader
from docx import Document  # Import the Document class from python-docx
from .summarize import process_legal_document  # Import the process_legal_document function
import requests
from django.http import JsonResponse
from .chatbot import cbt
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.session.has_key('is_logged'):
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        #if request.session.has_key('is_logged'):
        return render(request,'index.html')
    return redirect('login')

@cache_control(no_cache=True, must_revalidate=True)
def login(request):
    if request.method =='POST':
        # get the post parameters
        loginuname = request.POST["loginuname"]
        loginpassword=request.POST["loginpw"]
        user = authenticate(username=loginuname, password=loginpassword)
        if user is not None:
            dj_login(request, user)
            request.session['is_logged'] = True
            user = request.user.id 
            request.session["user_id"] = user
            messages.success(request, "Logged in successfully")
            return redirect('/index')
        else:
            messages.error(request," Invalid Credentials, Please try again")  
            return redirect("/")  
        return HttpResponse('404-not found')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(request," Username is already taken!")
                return redirect("/register")    
            except User.DoesNotExist:
                if len(uname)>15:
                    messages.error(request," Username must be max 15 characters, Please try again")
                    return redirect("/register")
        
                if not uname.isalnum():
                    messages.error(request," Username should only contain letters and numbers, Please try again")
                    return redirect("/register")
        
                if pass1 != pass2:
                    messages.error(request," Passwords do not match, Please try again")
                    return redirect("/register")

        #create the user
        user = User.objects.create_user(uname, email, pass1)
        user.first_name=fname
        user.last_name=lname
        user.email = email

        user.save() 

        print("User Created")
        return redirect("/login")

    return render(request,'register.html')

@cache_control(no_cache=True, must_revalidate=True)
def handleLogout(request):
    del request.session['is_logged']
    del request.session["user_id"] 
    logout(request)
    return redirect('login')

def faq(request):
    return render(request, 'FAQs.html')

def about(request):
    return render(request, 'about.html')

def extract_text_from_pdf(file):
    pdf_text = ''
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

def extract_text_from_docx(file):
    docx_text = ''
    doc = Document(file)
    for paragraph in doc.paragraphs:
        docx_text += paragraph.text
    return docx_text

def legal_document_view(request):
    if request.method == 'POST':
        # Get the input text from the POST data
        input = request.POST.get('input', '')

        # Check if a file was uploaded
        uploaded_file = request.FILES.get('document_file')

        if input or uploaded_file:
            try:
                # If both input text and a file were provided, combine them
                if input and uploaded_file:
                    file_name = uploaded_file.name.lower()
                    if file_name.endswith('.pdf'):
                        file_content = extract_text_from_pdf(uploaded_file)
                    elif file_name.endswith('.docx'):
                        file_content = extract_text_from_docx(uploaded_file)
                    elif file_name.endswith('.txt'):
                        file_content = uploaded_file.read().decode('utf-8')
                    else:
                        return HttpResponse("Unsupported file format. Please upload a PDF, DOCX, or TXT file.")

                    combined_input = f"{input}\n{file_content}"
                elif input:
                    combined_input = input
                elif uploaded_file:
                    file_name = uploaded_file.name.lower()
                    if file_name.endswith('.pdf'):
                        file_content = extract_text_from_pdf(uploaded_file)
                    elif file_name.endswith('.docx'):
                        file_content = extract_text_from_docx(uploaded_file)
                    elif file_name.endswith('.txt'):
                        file_content = uploaded_file.read().decode('utf-8')
                    else:
                        return HttpResponse("Unsupported file format. Please upload a PDF, DOCX, or TXT file.")

                    combined_input = file_content

                # Call the process_legal_document function
                modified_text = process_legal_document(combined_input)

                # Render the result
                return render(request, 'simplify.html', {'modified_text': modified_text})
            except Exception as e:
                error_message = str(e)
                return HttpResponse(f"An error occurred: {error_message}")

    # If not a POST request or if there's no input, render the input form
    return render(request, 'index.html')

def simplify(request):
    return render(request, 'simplify.html')

def slot_booking(request):
    return render(request, 'slotbooking.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def slot_booking_form(request):
    if request.method == 'POST':
        name = request.POST['first_party_name']
        return render(request, 'confirmation.html', {'name': name})
    return render(request, 'slot_booking_form.html')

def confirmation(request):
    # Retrieve booking information from query parameters
    first_party_name = request.GET.get("firstPartyName", "")
    second_party_name = request.GET.get("secondPartyName", "")
    date = request.GET.get("date", "")
    timeSlot = request.GET.get("timeSlot", "")
    district = request.GET.get("districtSelect", "")
    registration_office = request.GET.get("registrationOfficeSelect", "")

    return render(request, "confirmation.html", {
        "first_party_name": first_party_name,
        "second_party_name": second_party_name,
        "date": date,
        "timeSlot": timeSlot,
        "district": district,
        "registration_office": registration_office,
    })

def chatbot_view(request):
    if request.method == 'POST':
        # Retrieve the user's input from the POST request
        user_input = request.POST.get('user_input', '')

        # Process the user's input and generate a chatbot response (replace this with your actual chatbot logic)
        chatbot_response = cbt(user_input)

        # Return the chatbot response as JSON
        response_data = {'message': chatbot_response}
        return JsonResponse(response_data)

    return render(request, 'chatbot.html')


