from django.db import models


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    converted_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# # class Agent(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.user.email


class Agent(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname


