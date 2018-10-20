# Drugsand.me

[Drugsand.me](https://www.drugsand.me) provides accessible, objective and comprehensive educational material to help reduce the short and long term harms of drugs.
We are a group of scientists, pedagogists and analysts with extensive experience in drug education. We wanted to do something to stop the increasing number of accidents and deaths that occur in the world due to lack of drug education.

## Installation

In order to get this up and running, I personally use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

```
mkvirtualenv drugsandme
cd ~/dev [or your preferred dev directory]
git clone https://github.com/higab85/drugsandme-wagtail
cd drugsandme-wagtail
pip install -r requirements.txt
python manage.py runserver
```
The site should now be running on [localhost:8000](localhost:8000).
Log into the admin([localhost:8000/admin](localhost:8000/admin)) with the credentials admin / changeme.
