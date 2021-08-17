# RESTful_API

<a href="#"><img alt="Python 3.8" src="https://img.shields.io/badge/Python-3.8-blue"></a>
<a href="#"><img alt="Flask" src="https://img.shields.io/badge/Flask%20-%23FF6F00.svg?logo=Flask&logoColor=white"></a>

### FlowChart


![image](https://user-images.githubusercontent.com/55245100/129690172-24f9aa1e-5e56-4bf7-bcfa-d23349ef071d.png)

### Sequence Diagram  


![image](https://user-images.githubusercontent.com/55245100/129690225-45cbade1-d77d-4e47-9a2f-fbd330474673.png)

## Get Started:
#### Setup:
> `virtualenv <Name>`
> `pip install -r requirements.txt`

# Run API:
> `python app.py`

## Task:
Create a RESTful API using flask and mongodb with 3 URL end points. Used JWT access token to build a user module
You can register and host the mongodb database files here https://account.mongodb.com/account/register
You must need to apply CRUD restriction for templates based on the user, so one user can't delete, update, or view other user's Templates

1.Register
    
    URL : localhost:5000/register
    Method : POST
    Headers : {
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                first_name : 'lead_test@subi.com',
                last_name : '123456'
                email : 'lead_test@subi.com',
                password : '123456'
              }


2 Login

    URL : localhost:5000/login
    Method : POST
    Headers : {
                 'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                email : 'lead_test@subi.com',
                password : '123456'
              }  

    
    2 Template CRUD
    
    1.Insert new Template

    URL : locahost:5000/template

    Method : POST
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
                     }  

    2.Get All Template

    URL : locahost:5000/template
    
    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}      


    3.GET Single Template

    URL : locahost:5000/template/<template_id>

    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  

    2.Update Single Template

    URL : locahost:5000/template/<template_id>
    
    Method : PUT
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
    }   

    3.DELETE Single Template

    URL : locahost:5000/template/<template_id>

    Method : DEL
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}                  


