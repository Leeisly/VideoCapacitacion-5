from django.db import models





class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)
    

    #objects = BillingProfileManager()

    def __str__(self):
        return self.email


# class BillingProfileManager(models.Manager):
#     def new_or_get(self, request):
#         user = request.user
#         guest_email_id = request.session.get('guest_email_id')
#         created = False
#         obj = None
#         if user.is_authenticated():
#             'logged in user checkout; remember payment stuff'
#             obj, created = self.model.objects.get_or_create(
#                             user=user, email=user.email)
#         elif guest_email_id is not None:
#             'guest user checkout; auto reloads payment stuff'
#             guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
#             obj, created = self.model.objects.get_or_create(
#                                             email=guest_email_obj.email)
#         else:
#             pass
#         return obj, created
