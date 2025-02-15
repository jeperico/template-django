from cuser.models import AbstractCUser
from utils.models import BaseModel


class User(AbstractCUser):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
  )
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  created_at = models.DateTimeField(
    auto_now_add=True,
    editable=False,
  )
  updated_at = models.DateTimeField(
    auto_now=True,
  )
  # password = models.CharField(max_length=255)

  def __str__(self):
    return self.name
