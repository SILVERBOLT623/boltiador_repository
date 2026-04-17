from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Skill, Project, Education
from .forms import ContactForm


def get_profile():
    """Helper to get profile or return None."""
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'active_page': 'home',
    }
    return render(request, 'bolt_app/home.html', context)


def about(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'active_page': 'about',
    }
    return render(request, 'bolt_app/about.html', context)


def skills(request):
    profile = get_profile()
    all_skills = Skill.objects.all()

    # Group skills by category
    skill_categories = {}
    for skill in all_skills:
        category = skill.get_category_display()
        if category not in skill_categories:
            skill_categories[category] = []
        skill_categories[category].append(skill)

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'active_page': 'skills',
    }
    return render(request, 'bolt_app/skills.html', context)


def projects(request):
    profile = get_profile()
    all_projects = Project.objects.all()
    context = {
        'profile': profile,
        'projects': all_projects,
        'active_page': 'projects',
    }
    return render(request, 'bolt_app/projects.html', context)


def education(request):
    profile = get_profile()
    all_education = Education.objects.all()
    context = {
        'profile': profile,
        'education_list': all_education,
        'active_page': 'education',
    }
    return render(request, 'bolt_app/education.html', context)


def contact(request):
    profile = get_profile()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Send email notification
            try:
                send_mail(
                    subject=f"Portfolio Contact: {contact_message.subject}",
                    message=f"From: {contact_message.name} <{contact_message.email}>\n\n{contact_message.message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'form': form,
        'active_page': 'contact',
    }
    return render(request, 'bolt_app/contact.html', context)
