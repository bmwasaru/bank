# Illustrating Event Sourcing in Django

# Requirements

Requires Python 3.6 and PostgreSQL

# Installation

Create, activate virtualenv `venv` and install requirements

```
virtualenv -p python3 venv
. venv/bin/activate
pip install - requirements.txt
```

Change the database settings in the `bank/settings.py`` file accordingly and create a superuser `python manage.py createsuperuser`

Run the django shell

```
python manage.py shell
```

Testing it out

```
from bank.models import Account
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from bank.models import Event
account = 
account.make_deposit(50.0)
account.make_deposit(12220.0)
account.make_withdrawal(20.0)
events = Event.objects.filter(
         content_type=ContentType.objects.get_for_model(account), 
         object_id=account.id
        )
for event in events:
    print(event.body)
```

```
{"owner_id": 1, "id": 6, "type": "created_account"}
{"amount": 50.0, "type": "make_deposit"}
{"amount": 12220.0, "type": "make_deposit"}
{"amount": 20.0, "type": "made_withdrawal"}
```

