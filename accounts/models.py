from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
def upload_to(instance, filename):
    return "{}/{}/{}".format("profile_photo", instance.user.username, filename)


class UserProfile(models.Model):
    men = "K"
    women = "Q"
    choice = "gender"
    genders = (
        (men, "Kişi"),
        (women, "Qadın"),
        (choice, "gender")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=15, verbose_name="Telefon", blank=True)
    gender = models.CharField(max_length=12, verbose_name="Cinsi", default=choice, choices=genders, blank=True)
    bio = models.CharField(max_length=100, verbose_name="Haqqında", blank=True)
    birth_date = models.DateField(verbose_name="Doğum tarixi", blank=True, null=True)
    profile_photo = models.ImageField(upload_to=upload_to, verbose_name="Profil şəkli", default="default/unnamed.jpg",
                                      null=True, blank=True)

    class Meta:
        verbose_name_plural = "Users Profiles"
    
    def get_full_name_or_username(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username
    

    def __str__(self):
        return "{}".format(self.get_full_name_or_username())


# using django signals for creating user profile page once time when user registering
def create_user_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(receiver=create_user_profile, sender=User)