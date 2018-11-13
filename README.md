# betaout-assignment
Email marketing application

#### Steps to run the project.

1. Clone the repository
2. `python3 manage.py migrate`
3. `python3 manage.py runserver`

### Endpoints:

**1. Send emails endpoint**

**_Request_:**

POST `localhost:8000/api/v1/bouncer/send/emails`

BODY 
```
{
	"emails" : [
				"waqashamid722@gmail.com",
				"waqas@gmail.com"
				],
	"body" : "Hey! Welcome to Betaout",
	"subject" : "Welcome!"
}
```

**_Response_:**
```
{
    "Success": "Emails sent"
}
```

**1. Get user data endpoint**

**_Request_:**

GET `localhost:8000/api/v1/bouncer/user/data/waqashamid722@gmail.com`


**_Response_:**
```
{
    "id": 2,
    "email": "waqashamid722@gmail.com",
    "emails_received": [
        {
            "id": 1,
            "subject": "Welcome!",
            "body": "Hey! Welcome to Betaout",
            "created": "2018-11-13T08:29:13.291557Z",
            "modified": "2018-11-13T08:29:13.291628Z"
        }
    ],
    "created": "2018-11-13T08:29:13.373497Z",
    "modified": "2018-11-13T08:29:13.525045Z"
}
```

