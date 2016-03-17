# project_django_allauth_slate_razorpay
This is a demo django project to show the use of allauth to create and manage authentication. It also uses slate(the famous static api documentation UI) and lastly it uses Razorpay payment gateway integration.  
  
### Django allauth  
Django allauth is a very nice django package for authentication.  
You can find more about it here https://readthedocs.org/projects/django-allauth/  
  
### Slate
Slate helps in making beautiful static documentation for your API. It is very cool.    
You can find more about it here https://github.com/tripit/slate  
##### Slate is not supported with django so, this only uses it as a template.  
  
### Razorpay  
Razorpay is a very nice and very very easy to use payment gateway for India.  
You can find more about it here https://razorpay.com/  

### Grappelli
It also uses  the django-grappelli package which makes the django admin site look
very cool.
You can find more about it here https://django-grappelli.readthedocs.org/en/latest/  

### Used basic registration bootstrap template from http://azmind.com/  
  
  
 ---
  
          
  
###                                                HOW TO USE  
##### Generally I am very fond of giving long "How to use instructions" but  
##### sometimes I find it really boring like today :P so I'll keep it short.

1. Clone the project or download the zip.
2. Make a virtual environment( Helps you keep the global system-wide packages  
   and local project-wise packages seperate )
3. Go to settings.py and put your database connection variables. Also add EMAIL_HOST,  
   EMAIL_HOST_USER, EMAIL_HOST_PASSWORD of the SMTP server you have chosen or simply   
   remove all email variables except EMAIL_BACKEND to show test email in cmd/terminal. 
   Also add your RAZOR_KEY_ID and RAZOR_KEY_SECRET after registering at Razorpay.
4. Now run commands:-  
   a. python manage.py makemigrations registerApp  
   b. python manage.py syncdb  
   c. python manage.py collectstatic  
5. Now run the app by typing in "python manage.py runserver"
6. Go to "localhost:8000" in your web-browser and this is the user registration page.
7. You can login using localhost:8000/login
8. You find other URL-patterns in the urls.py of both project and app.

## NOTE: There might be some issues with the UI Templates and other stuff as well so, you can open an issue on this repository if you want to ask something from me/ need my help. 

Cheers


  
  
  
  
   

