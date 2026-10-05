from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, default="My Portfolio")
    banner_image = models.ImageField(upload_to='banner/', blank=True, null=True)
    banner_text = models.TextField(
        default="Welcome to my portfolio • Explore my work • Let's create something amazing",
        help_text="Text that scrolls across the banner. Use • to separate phrases."
    )
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Square profile image shown at the top right of the banner")
    about_background = models.ImageField(upload_to='about_bg/', blank=True, null=True, help_text="Background image for the About section")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True, help_text="Phone number shown in the Contact section")

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class EmploymentHistory(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False, help_text="Check if this is your current job")
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = "Employment History"
        verbose_name_plural = "Employment History"

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=50, help_text="Proficiency percentage from 0 to 100")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter / X'),
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('dribbble', 'Dribbble'),
        ('behance', 'Behance'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    username = models.CharField(max_length=200, blank=True, help_text="Display name/handle")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_platform_display()}"
