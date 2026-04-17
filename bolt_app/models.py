from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    career_goals = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(default=80, help_text='Proficiency level 0-100')
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text='Comma-separated list of technologies')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',')]

    class Meta:
        ordering = ['order', '-created_at']


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True, help_text='Leave blank if current')
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='education/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    def get_year_range(self):
        if self.end_year:
            return f"{self.start_year} – {self.end_year}"
        return f"{self.start_year} – Present"

    class Meta:
        ordering = ['-start_year']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} — {self.subject}"

    class Meta:
        ordering = ['-sent_at']
