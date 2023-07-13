Tools Used : Django web framework, Django Rest Framework

## Installation
1. Download the zip file of this repository or clone.
2. Install the requirements.txt file.
  ```bash
  pip install -r requirements.txt
  ```
3. Run the migrations
  ```bash
  python manage.py makemigrations 
  ```    
  ```bash
  python manage.py migrate
  ```
4. Run server in your localhost
  ```bash
  python manage.py runserver
   ```
5. Open your web browser and type http://localhost:8000/login

## Working
1. To **register** http://localhost:8000/register

    Input format :
    ```json
        "name": "newd2202",
        "mobile": 9912,
        "password" : "pwd"
    ```

2. to login http://localhost:8000/login
      Input format must be
     ``` json
        "name": "newd2202",
        "password" : "pwd"
    ```
    After succesful login,you will get the token id like this 
    ```json
        "token": "4db45278826195702acd70088d6e850191481ab3"
    ```
    Save the token id for later.
3. To view Contacts http://localhost:8000/contacts/?Authorization=token "token_number".

   Example :
    
      http://localhost:8000/contacts/?Authorization=token"4db45278826195702acd70088d6e850191481ab3"
    
    prompts you to login, If you haven't logged in


    you can create new contacts by using the POST method
    Input format
    ```json
        "name": "new2222",
        "mobile": 99127,
        "password" : "new"
    ```

4. To search using names, go to http://localhost:8000/name_search/?Authorization=token "token_number"
   Input format
    ```json
        "name": "new"
    ```
5. To search using names, go to http://localhost:8000/mobile_search/?Authorization=token "token_number"
   Input format
    ```json
        "mobile": 1234
    ```
6. To mark a contact spam, go to http://localhost:8000/spam/?Authorization=token "token_number"
   Input format
    ```json
        "name": "new"
    ```