from django.db.models import Manager
class Group: ...
class AbstractBaseUser:
  # FIXME: actually figure out args
  def __init__(self, *args, **kwargs): ...
class PermissionsMixin: ...
class UserManager(Manager): ...
class GroupManager(Manager): ...