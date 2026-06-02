import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm


logger = logging.getLogger(__name__)


PROFILE = {
    "name": "Pramod Kumbhar",
    "title": "AI & Data Science Graduate | Aspiring AI/ML Engineer | Full-Stack Developer",
    "location": "Pune, Maharashtra",
    "phone": "+91 9067903004",
    "email": "kumbharpramod834@gmail.com",
    "instagram": "https://www.instagram.com/pamms.07/",
    "whatsapp": "https://wa.me/919067903004",
    "linkedin": "https://www.linkedin.com/in/pramod-kumbhar-658410256/",
    "github": "https://github.com/pramod-kumbhar",
    "photo_url": "/static/portfolio/img/profile-placeholder.png",
    "resume_url": "/media/Pramod_Kumbhar.pdf",
    "summary": (
        "AI and Data Science graduate with hands-on experience in Python, SQL, "
        "and Django for full-stack development. Skilled in building responsive "
        "web apps and REST APIs, with exposure to React.js, AI/ML, Data Analytics, "
        "AWS Cloud, and hardware.My goal is to build innovative software solutions while growing as a Full Stack Python Developer and gaining real-world experience in AI/ML domain"
    ),
}

SOCIAL_LINKS = [
    ("Instagram", "instagram", PROFILE["instagram"]),
    ("WhatsApp", "whatsapp", PROFILE["whatsapp"]),
    ("LinkedIn", "linkedin", PROFILE["linkedin"]),
    ("Gmail", "gmail", f"mailto:{PROFILE['email']}"),
    ("GitHub", "github", PROFILE["github"]),
]

SKILLS = [
    ("Programming", [
        {"name": "Python", "icon": "PY"},
        {"name": "HTML", "icon": "HTML"},
        {"name": "CSS", "icon": "CSS"},
        {"name": "JavaScript", "icon": "JS"},
        {"name": "Tailwind CSS", "icon": "TW"},
    ]),
    ("Cloud", [
        {"name": "Networking", "icon": "NET"},
        {"name": "Security", "icon": "SEC"},
        {"name": "Linux", "icon": "LIN"},
        {"name": "AWS EC2", "icon": "EC2"},
        {"name": "AWS S3", "icon": "S3"},
        {"name": "VPC", "icon": "VPC"},
        {"name": "CloudWatch", "icon": "CW"},
    ]),
    ("Databases & Platforms", [
        {"name": "MySQL", "icon": "SQL"},
        {"name": "Jupyter Notebook", "icon": "JUP"},
        {"name": "Visual Studio Code", "icon": "VS"},
    ]),
    ("Web Frameworks", [
        {"name": "Django", "icon": "DJ"},
        {"name": "React.js", "icon": "RE"},
        {"name": "REST APIs", "icon": "API"},
    ]),
    ("Version Control & Tools", [
        {"name": "Git", "icon": "GIT"},
        {"name": "GitHub", "icon": "GH"},
        {"name": "Postman", "icon": "POST"},
    ]),
]

EDUCATION = [
    {
        "degree": "B.Tech in Artificial Intelligence and Data Science",
        "place": "Loknete Shamrao Peje Government College of Engineering, Ratnagiri",
        "year": "2021 - 2025",
        "result": "CGPA: 6.91",
    },
    {
        "degree": "12th Grade",
        "place": "Govindrao Highschool & Jr. College, Ichalkaranji",
        "year": "2021",
        "result": "Percentage: 75.17%",
    },
    {
        "degree": "10th Grade",
        "place": "New Highschool, Kasaba Tarale",
        "year": "2019",
        "result": "Percentage: 82.40%",
    },
]

EXPERIENCE = [
    {
        "role": "Software Developer Intern",
        "company": "Landmark Techedge Pvt. Ltd.",
        "period": "Jul 2025 - Apr 2026",
        "points": [
            "Developing enterprise web applications using Django, React, and MySQL.",
            "Designing and integrating RESTful APIs for frontend-backend communication.",
            "Collaborating with senior developers in code reviews, debugging, and performance optimization.",
        ],
    },
    {
        "role": "AWS Trainee",
        "company": "Vinsys IT Services",
        "period": "Sep 2025 - Dec 2025",
        "points": [
            "Completed intensive AWS Cloud Practitioner training across cloud foundations, architecture, security, Linux, networking, databases, automation, and storage.",
            "Performed hands-on labs with EC2, S3, VPC, IAM, and CloudWatch, strengthening cloud deployment capability.",
        ],
    },
]

PROJECTS = [
    {
        "name": "E-Commerce Restaurant Management System",
        "stack": "Django, SQL, HTML, CSS, React.js, REST APIs",
        "link": "https://github.com/pramod-kumbhar/E-commerce-restaurant-demo-project",
        "points": [
            "Developed a full-stack ecommerce web application with secure authentication and product management.",
            "Built REST APIs and optimized SQL queries and CRUD operations to improve response time by 30%.",
            "Integrated frontend components and managed database operations for a scalable, responsive application.",
        ],
    },
    {
        "name": "Student Attendance Management System",
        "stack": "React.js, HTML, Tailwind CSS",
        "link": "https://github.com/pramod-kumbhar/SAMSTRACK-Student-Attendance-Management-System",
        "points": [
            "Built a web-based system for digitally recording and managing student attendance.",
            "Enabled admins and teachers to track attendance, manage student data, and generate reports centrally.",
            "Reduced manual errors and improved accuracy compared with traditional attendance methods.",
        ],
    },
]

CERTIFICATIONS = [
    "AWS Re/Start Graduate",
    "Python Full-Stack Development Certificate - Kiran Academy",
]

ACHIEVEMENTS = [
    "Led the college cricket team to a championship victory as captain and secured top positions in multiple games.",
]

INTERESTS = [
    "AI and GenAI tools",
    "Editing",
    "Self-learning from online resources",
    "Traveling",
    "Leadership",
    "Sports",
]


def context(page_title):
    return {
        "page_title": page_title,
        "profile": PROFILE,
        "social_links": SOCIAL_LINKS,
        "skills": SKILLS,
        "education": EDUCATION,
        "experience": EXPERIENCE,
        "projects": PROJECTS,
        "certifications": CERTIFICATIONS,
        "achievements": ACHIEVEMENTS,
        "interests": INTERESTS,
    }


def send_contact_email(form):
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        raise RuntimeError(
            "Email is not configured. Set EMAIL_HOST_USER and EMAIL_HOST_PASSWORD."
        )

    name = form.cleaned_data["name"]
    sender_email = form.cleaned_data["email"]
    subject = form.cleaned_data.get("subject") or "New portfolio contact message"
    message = form.cleaned_data["message"]
    body = (
        f"New message from your portfolio website\n\n"
        f"Name: {name}\n"
        f"Email: {sender_email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n"
    )

    email = EmailMessage(
        subject=f"Portfolio Contact: {subject}",
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_RECEIVER_EMAIL],
        reply_to=[sender_email],
    )
    return email.send(fail_silently=False)


def home(request):
    return render(request, "portfolio/home.html", context("Home"))


def about(request):
    return render(request, "portfolio/about.html", context("About"))


def skills(request):
    return render(request, "portfolio/skills.html", context("Skills"))


def education(request):
    return render(request, "portfolio/education.html", context("Education"))


def experience(request):
    return render(request, "portfolio/experience.html", context("Experience"))


def projects(request):
    return render(request, "portfolio/projects.html", context("Projects"))


def certifications(request):
    return render(request, "portfolio/certifications.html", context("Certifications"))


def contact(request):
    page_context = context("Contact")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_contact_email(form)
            except BadHeaderError:
                messages.error(request, "Invalid email header. Please try again.")
            except Exception as error:
                logger.exception("Contact form email failed")
                error_message = (
                    f"Email send failed: {error}"
                    if settings.DEBUG
                    else "Message could not be sent. Please check the email setup and try again."
                )
                messages.error(
                    request,
                    error_message,
                )
            else:
                messages.success(
                    request,
                    "Thank you. Your message has been sent successfully.",
                )
                return redirect("contact")
    else:
        form = ContactForm()

    page_context["form"] = form
    return render(request, "portfolio/contact.html", page_context)
