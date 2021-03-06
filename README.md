# RESTful_API

<a href="#"><img alt="Python 3.8" src="https://img.shields.io/badge/Python-3.8-blue"></a>
<a href="#"><img alt="Flask" src="https://img.shields.io/badge/Flask%20-%23FF6F00.svg?logo=Flask&logoColor=white"></a>
<a href="#"><img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?logo=mongodb&logoColor=white"></a>
<a href="#"><img alt="Postman" src="https://img.shields.io/badge/Postman-%20-%23F37626.svg?logo=Postman&logoColor=white%22"></a>

### FlowChart


![image](https://user-images.githubusercontent.com/55245100/129690172-24f9aa1e-5e56-4bf7-bcfa-d23349ef071d.png)

### Sequence Diagram  


![image](https://user-images.githubusercontent.com/55245100/129690225-45cbade1-d77d-4e47-9a2f-fbd330474673.png)

## Get Started:
#### Setup:
> `virtualenv <Name>` </br>
> `pip install -r requirements.txt`

### Run API:
> `python app.py`

### Steps(Postman):
1) Register

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/register.jpg)

2) Login

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/login.jpg)

3) Add x-access-token in headers

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/x_access_tokens.jpg)

4) Template:
-> Create new Template:</br>

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/post.jpg)

-> Get all Templates:</br>

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/get_all.jpg)

-> Get single Template:</br>

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/get_1.jpg)

-> Update single Template:</br>

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/update.jpg)

-> Delete particular Template:</br>

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/delete.jpg)

After deleting:</br>

![image](https://github.com/dpk-a7/RESTful_API/blob/main/images/get_1_delete.jpg)



## Task:
Create a RESTful API using flask and MongoDB with 3 URL endpoints. Use JWT access token to build a user module
You can register and host the MongoDB database files here https://account.mongodb.com/account/register
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


