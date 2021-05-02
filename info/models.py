from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# moodle's users have created resume


class Owner(models.Model):
    userId = models.BigIntegerField(blank=False, null=False, primary_key=True, unique=True)

    def __str__(self):
        return f"{self.userId}"
    


class Resume(models.Model):

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        self.personalInfoCounter = 0
    
    date_created = models.DateField(auto_now_add=True, blank=True, null= True)
    date_modified = models.DateField(auto_now_add=True, blank=True, null= True)
    resumeTitle = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(
        Owner, to_field="userId", on_delete=models.CASCADE, null=False, related_name="resumes")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.personalInfoCounter += 1
        if (self.personalInfoCounter == 1):
            print("test")
            PersonalInfo(resumeId=self).save()


class PersonalInfo(models.Model):
    """
        Model to capturing Personal info of user
    """
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True)
    resumeId = models.OneToOneField(
        Resume, on_delete=models.CASCADE, null=False, blank=False, related_name="PI_modified")
    wantedJobTitle = models.CharField(max_length=50, null=True, blank=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(
        max_length= 100, null=True, blank=True)
    city = models.CharField(
        max_length=100, null=True, blank=True)
    address = models.CharField(
        max_length=250, null=True, blank=True)
    postalCode = models.CharField(
        max_length=250, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    placeOfBirth = models.CharField(
        max_length=250, null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    personalSummary = models.TextField(null=True, blank=True)



class EmploymentHistory(models.Model):
    """
        Model to capturing employment history
    """
    date_created = models.DateField(
        auto_now_add=True, blank= True, null=True)
    date_modified = models.DateField(
        auto_now_add=True, blank= True)
    resumeId = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, blank=True, related_name="EH_modified")
    jobTitle = models.CharField(max_length=50, blank=True)
    employer = models.CharField(max_length=250, blank=True)
    startDate = models.DateField(null=True,  blank=True)
    endDate = models.DateField(null=True, blank=True)
    city = models.CharField(
        max_length=250, null=True, blank=True)
    description = models.TextField(blank=True)


class Education(models.Model):
    """
        Model to capturing Education history
    """
    date_created = models.DateField(
        auto_now_add=True, blank= True, null=True)
    date_modified = models.DateField(
        auto_now_add=True, blank= True)
    resumeId = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, blank=True, related_name="Ed_modified")
    school = models.CharField(max_length=50, blank=True)
    degree = models.CharField(max_length=250, blank=True)
    startDate = models.DateField(null=True,  blank=True)
    endDate = models.DateField(null=True, blank=True)
    city = models.CharField(
        max_length=250, null=True, blank=True)
    description = models.TextField(blank=True)


class WebsiteAndSocialMedia(models.Model):
    """
        Model to capturing Website and Social Media history
    """
    date_created = models.DateField(
        auto_now_add=True, blank= True, null=True)
    date_modified = models.DateField(
        auto_now_add=True, blank= True)

    resumeId = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, blank=True, related_name="WSMedia_modified")
    label = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=50)

    def __str__(self):
        if self.label:
            return self.label



class skill(models.Model):
    """
        Model to capturing skills
    """
    date_created = models.DateField(
        auto_now_add=True, blank= True, null=True)
    date_modified = models.DateField(
        auto_now_add=True, blank= True)
    resumeId = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, blank=True, related_name="skills_modified")
    skill = models.CharField(max_length=50)
    level = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )


class language(models.Model):
    """
        Model to capturing language skill
    """

    LEVEL_CHOICES = [
        ("1", "Native Speaker"),
        ("2", "Highly proficient"),
        ("3", "Very goog command")
    ]

    date_created = models.DateField(
        auto_now_add=True, blank= True, null=True)
    date_modified = models.DateField(
        auto_now_add=True, blank= True)

    resumeId = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, blank=True, related_name="languages_modified")
    language = models.CharField(max_length=70)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, blank= True)


class course(models.Model):
    """
        Model to capturing courses history
    """
    date_created = models.DateField(
        auto_now_add=True, blank= True, null=True)
    date_modified = models.DateField(
        auto_now_add=True, blank= True)

    resumeId = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, blank=True, related_name="courses_modified")

    course = models.CharField(max_length=50, blank=True)
    institution = models.CharField(max_length=50, blank=True)

    startDate = models.DateField(null=True,  blank=True)
    endDate = models.DateField(null=True, blank=True)










