from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LostItem, FoundItem, Issue1, Collaborative, User

def login(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))

        if user.password == request.POST.get('username'):
            request.session['username'] = user.username
            return redirect('home')
        
    return render(request, "wordleapp/login.html")

def register(request):
    if request.method == 'POST':
        user = User(request.POST.get('username'), request.POST.get('password'))
        user.save()
        request.session['username'] = user.username
        return redirect('home')
    return render(request, "wordleapp/register.html")

def home(request):
    return render(request, "wordleapp/user.html")

# View to process the lost item form and add new items
def process_item_lost(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_descr = request.POST.get('item_descr')
        owner_name = request.POST.get('owner_name')
        owner_contact = request.POST.get('owner_contact')
        date_lost = request.POST.get('date_lost')  # Assuming date is sent as a string in the format 'YYYY-MM-DD'

        # Create a new LostItem entry
        item = LostItem(
            item_name=item_name,
            item_descr=item_descr,
            owner_name=owner_name,
            owner_contact=owner_contact,
            date_lost=date_lost if date_lost else None  # Handle empty date
        )
        item.save()

        # Fetch updated items to display
        items_lost = LostItem.objects.all()
        items_found = FoundItem.objects.all()
        return render(request, 'wordleapp/lost_and_found.html', {'items_lost': items_lost, 'items_found' : items_found})

# View to process the found item form and add new items
def process_item_found(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_descr = request.POST.get('item_descr')
        finder_name = request.POST.get('finder_name')
        finder_contact = request.POST.get('finder_contact')
        date_found = request.POST.get('date_found')  # Assuming date is sent as a string in the format 'YYYY-MM-DD'

        # Create a new FoundItem entry
        item = FoundItem(
            item_name=item_name, 
            item_descr=item_descr,
            finder_name=finder_name,
            finder_contact=finder_contact,
            date_found=date_found if date_found else None  # Handle empty date
        )
        item.save()

        # Fetch updated items to display
        items_lost = LostItem.objects.all()
        items_found = FoundItem.objects.all()
        return render(request, 'wordleapp/lost_and_found.html', {'items_lost': items_lost, 'items_found' : items_found})

def process_issue(request):
    if request.method == 'POST':
        issue_name = request.POST.get('issue_name')
        issue_descr = request.POST.get('issue_descr')
        # Create a new patient entry in the database using the Patient model
        issue = Issue1(issue_name=issue_name, issue_descr=issue_descr)
        issue.save()
        issues=Issue1.objects.all()
        return render(request, 'wordleapp/issue_central.html', {'issues' : issues})

def process_collaboration(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        organizer = request.POST.get('organizer', '')  # Optional
        collaboration_descr = request.POST.get('collaboration_descr')
        skills_preferred = request.POST.get('skills_preferred')
        team_size = request.POST.get('team_size')
        deadline = request.POST.get('deadline')
        posted_by = request.POST.get('posted_by')
        contact_email = request.POST.get('contact_email')
        if not all([event_name, collaboration_descr, skills_preferred, team_size, deadline, posted_by]):
            return HttpResponse("Error: All fields except organizer are required.", status=400)

        # Save collaboration to DB
        collab = Collaborative(
            event_name=event_name,
            organizer=organizer,
            collaboration_descr=collaboration_descr,
            skills_preferred=skills_preferred,
            team_size=team_size,
            deadline=deadline,
            posted_by=posted_by,
            contact_email=contact_email,
        )
        collab.save()

        return redirect('collaboration')  # Redirect to collaboration list page after submitting

def collaboration(request):
    collabs = Collaborative.objects.all()
    return render(request, 'wordleapp/collaboration.html', {'collabs': collabs})

def collaboration_form(request):
    return render(request, "wordleapp/collaboration_form.html")

# def collaboration_dashboard(request):
#     collaborations = CollaborationRequest.objects.all()
#     applications = Application.objects.filter(collaboration__in=collaborations)
    
#     return render(request, 'collaboration_dashboard.html', {'collaborations': collaborations, 'applications': applications})

# def update_application_status(request, application_id, status):
#     application = Application.objects.get(id=application_id)
#     application.status = status
#     application.save()
    
#     return redirect('collaboration_dashboard')
from django.contrib.auth.decorators import login_required

@login_required
def collaboration_detail(request, collaboration_id):
    # Get the collaboration post
    collaboration = get_object_or_404(CollaborationRequest, id=collaboration_id)
    
    # Check if the logged-in user is the author of the collaboration post
    if collaboration.posted_by != request.user:
        # If the user is not the author, redirect or show a permission error
        return redirect('collaboration_dashboard')
    
    # Get the applications related to this collaboration
    applications = Application.objects.filter(collaboration=collaboration)

    return render(request, 'collaboration_detail.html', {'collaboration': collaboration, 'applications': applications})

@login_required
def update_application_status(request, application_id, status):
    application = get_object_or_404(Application, id=application_id)
    # Ensure the current user is the author of the collaboration post
    if application.collaboration.posted_by != request.user:
        return redirect('collaboration_dashboard')
    
    # Update the application status
    application.status = status
    application.save()
    
    return redirect('collaboration_detail', collaboration_id=application.collaboration.id)

def process_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        issue_id = request.POST.get('issue_id')
        # print(comment, issue_id)
        # Create a new patient entry in the database using the Patient model
        for i in Issue1.objects.filter(id__in=issue_id):
            print(i.comment1, i.comment2)
            if i.comment1=="":
                i.comment1=comment
            elif i.comment2=="":
                i.comment2=comment
            elif i.comment3=="":
                i.comment3=comment
            elif i.comment4=="":
                i.comment4=comment
            elif i.comment5=="":
                i.comment5=comment


            i.save()
        issues=Issue1.objects.all()
        return render(request, 'wordleapp/issue_central.html', {'issues' : issues})

def lost_and_found(request):
    items_lost = LostItem.objects.all()
    items_found = FoundItem.objects.all()
    return render(request, 'wordleapp/lost_and_found.html', {'items_lost': items_lost, 'items_found' : items_found})
# View to render the lost item form page
def lost_form(request):
    return render(request, "wordleapp/lost_form.html")

# View to render the found item form page
def found_form(request):
    return render(request, "wordleapp/found_form.html")
def issue_form(request):
    return render(request, "wordleapp/issue_form.html")



def issue_central(request):
    if request.method == 'POST':
        issue_name = request.POST.get('issue_name')
        issue_descr = request.POST.get('issue_descr')
        # Create a new patient entry in the database using the Patient model
        issue = Issue1(issue_name=issue_name, issue_descr=issue_descr)
        issue.save()
    issues = Issue1.objects.all()
    return render(request, "wordleapp/issue_central.html", {'issues' : issues})




