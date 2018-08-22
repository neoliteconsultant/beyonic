

### About
Loginsite is a web application that extends Django's inbuilt user authentication  


### Prerequisites
Before running the application, ensure you have installed and configured
the following tools

- Pip v18.0
- Django v2.1
- Python v3.5.0 or higher



### Installation
1. Copy the project, loginsite, to any directory of your choice.

2. Navigate to the root directory (loginsite) containing the manage.py file in a command line.

3.  install django-two-factor-auth and its dependencies
    ```
   $ pip install django-two-factor-auth
   ``` 

 
3. Run the migrate command in a shell to create the database tables automatically.
   ```
   $ python manage.py migrate 
   ``` 
   
   
4. Execute the runserver command in a shell to start the development server.This will enable you to access
   the web aplication in a browser.
   ```
   $ python manage.py runserver
   ```


   
5. Copy the following url in a browser
   
   http://localhost:8000/
   
   NB: The development server runs on port 8000 by default  

### Running tests
In a terminal navigate to the root directory of the project containing the manage.py file, 
then run the following command in a shell:  
  ```
  $ python manage.py test 
  ``` 
