from django.contrib import admin
from .models import Question,Choice,User,Vote

admin.site.register([Question,Choice,User,Vote])


