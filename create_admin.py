from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv
load_dotenv(override=True)
User = get_user_model()
if not User.objects.filter(username=os.getenv("ADMIN_USERNAME")).exists():
    User.objects.create_superuser(os.getenv("ADMIN_USERNAME"), os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))
