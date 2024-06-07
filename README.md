# Blog Platform
Blog Platform is a blogging system built using Django and Django REST Framework. This system allows users to create and manage blog posts, authors, and comments.

Setup Instructions

  ->Clone the Project-Create a directory, open a terminal in the directory path, and clone the Blog Platform project:

      git clone https://github.com/yourusername/Blog-Platform.git
  ->Install Virtual Environment
  
      pip install virtualenv
      
  ->Create a virtual environment within the directory:

      python -m venv venv_name  # On Windows
      python3 -m venv venv_name  # On macOS/Linux

  ->Activate Virtual Environment

      venv_name\Scripts\activate       # On Windows
      source venv_name/bin/activate    # On macOS/Linux

  ->Install Requirements

      pip install -r requirements.txt

  ->Open the Blog Platform project in VS Code:

      code .

  ->Open a terminal in VS Code, navigate to the project directory, and run the server:
  
      cd Blog_Platform
      python manage.py runserver
      
API Endpoints

1.Blog Management
a)

    Endpoint  : api/blog/
    Method    : GET     - List All Blog Posts
b)

    Endpoint  : api/blog/
    Method    : GET     - Post a Blog
    Data      : JSON    - {"title": "string", "content": "string", "author": "int"}
c)

    Endpoint  : /blog/{id}/
    Method    : GET     - Retrieve a Specific Blog Post
d)

    Endpoint  : /blog/{id}/
    Method    : PUT     -Update a Specific Blog Post
    Data      : JSON    - {"title": "string", "content": "string", "author": "int"}
e)

    Endpoint  : /blog/{id}/
    Method    : DELETE  -  Delete a Specific Blog Post

    
2.Comment Management

    Endpoint  : /blog/{id}/comment/
    Method    : POST     - Add a Comment to a Blog Post
    Data      : JSON     - {"content": "string", "author": "int"}
    
3.Author Management
a)

    Endpoint  : /blog/authors/
    Method    : POST     - Create an Author
    Data      : JSON     - {"name": "string", "bio": "string"}
b)

    Endpoint  : /blog/authors/
    Method    : GET      - List All Authors
c)   
    
    Endpoint  : /blog/authors/{id}/
    Method    : GET      - Retrieve a Specific Author
d)

    Endpoint  : /blog/authors/{id}/
    Method    : PUT      - Update a Specific Author
    Data      : JSON     - {"name": "string", "bio": "string"}
e)

    Endpoint  : /blog/authors/{id}/
    Method    : DELETE   - Delete a Specific Author
