from django.db import models
import uuid
# Create your models here.


class AbstractModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    server_created_on = models.DateTimeField(auto_now_add=True)
    server_updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(null=False, default=False)

    class Meta:
        abstract = True


class Ticket(AbstractModel):
    heading = models.TextField()


class Commit(AbstractModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='commit_set')
    message = models.TextField()
