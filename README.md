# Introduction

The following packages were used to implement this React project:

- flask: framework to develop Python web application
- python-dotenv: package to load environment variables from a .env file
- marshmallow: package for schema validation and data serialization

# Installation

To run this project, you need to have Python installed in your computer. The version I used was Python 3.12.

You will need to create a .env file on the root directory of the project. This file 
will contain the following environment variable:

- ACCESS_CONTROL_ALLOW_ORIGINS: the URL where the front-end project is hosted (for a local setup, http://localhost:3000)
- ACCESS_CONTROL_ALLOW_HEADERS: the headers allowed by CORS (I used "*" for all headers)
- ACCESS_CONTROL_ALLOW_METHODS: the HTTP methods allowed by CORS (you could use *, but to be as strict as possible, 
you only need "GET, POST")

Then, run "pip install -r requirements.txt" to download the dependencies from PIP. When it is done, you can run the 
application using the command "flask run --host=0.0.0.0".

# CORS

When we have an API serving a front-end application, CORS is something we have to worry about. I could have used a 
package called "flask-cors", which implement what we need to configure CORS. 

However, since CORS is a simple, I usually implement a solution by myself, which can be found in the file utils/cors.py. 
This file contains:

- A class MethodViewWithCors, which implements an option method returning the needed CORS headers.
- A decorator "cors", which must be used in endpoints that need to support CORS. For this project, it is the case of 
all the endpoints, but in a more general back-end, we could have endpoints that are not called by a browser client.

# Data validation

I used the marshmallow library to validate the data received via API because it is a good practice to validate the 
data both client- and server-side. The data schema can be found in the file schemas.py.
