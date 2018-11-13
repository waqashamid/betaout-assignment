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
	"body" : "Hey! Welcome to the Betaout",
	"subject" : "Welcome!"
}
```

**_Response_:**
```
{
    "Success": "Emails sent"
}
```
