from django.db import models
from django.urls import reverse
from datetime import date
# thank you Django for this user :-)
from django.contrib.auth.models import User

""" Bounties {
    name,
    profile image url,
    status (missing, target, etc),
    summary ( this shows on the bounty index card )

}

"""