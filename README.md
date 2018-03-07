# Rotten Cherries
Rate the lectures you took and search professors.
## Getting Started
```
git clone git://github.com/hannibal1296/rotten-cherries.git
```
### Prerequisites
```
pip install djangorestframework

pip install django-cors-headers
```

### Notice
Input your own secret keys made of 50 characters not necessarily including numbers or special characters.
```
# in settings.py
 
...
# SECRET_KEY = {your secret key}
...
```

## Structure
Four apps consist of rottencherries.
1. account: for user account management
2. mainpage: for the mainpage
3. search: for the lecture search or the professor search
4. rate: for the lecture rating
