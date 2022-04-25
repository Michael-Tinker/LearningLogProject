import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all()

for t in topics:
    print(t.id, "  ", t)
    print(t.text)
    print(t.date_added)
#set to return in the string method of the models file, that's why it returns the topics

t = Topic.objects.get(id=1)
print(t.id)
print(t.text)
print(t.date_added)


entries = t.entry_set.all()

for e in entries:
    print(e)
    print("\n\n\n")
    print(e.text)
