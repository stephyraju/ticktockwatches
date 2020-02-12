[![Build Status](https://travis-ci.com/stephyraju/ticktockwatches.svg?branch=master)](https://travis-ci.com/stephyraju/ticktockwatches)

## TickTockWatches 
#### Full Stack Framework Milestone 

## Table Of Contents

### UX

This project is part of my Code Institute Full Stack Software Development studies, specifically the Full Stack Frameworks module. The purpose of the project was to create a website for an online watch shop where the company can displays their products for the customers. This website is designed in a simple and efficient way for the customers to have a smooth and pleasant shopping experience.

### User Stories

  * As a user I want to view the site from any device (mobile, tablet, desktop).
  * As a user I want to See the products without login.
  * As a user I want to create my account.
  * As a user I want to update my profile.
  * As a user I want to login and logout.
  * As a user I want to be able to change my password.
  * As a user I want to filter the products based on gender and brand.
  * As a user I want to search for a product.
  * As a user I want to be able to navigate the shop easily, find what I need and make a safe and secure purchase.
  * As a user I want to contact the shop for any quiries.

  
### Design


##### Framework

  * Bootstrap 4
  * jQuery 3.4.1
    * In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
  * Django 1.11
    * Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap. We were taught how to use Django 1.11 in the lessons, despite Django 2.0 being the current version,I used Django 1.11

#### Color Scheme


#### Icons

* Font Awsome 5.11.2

    I prefer to use Font Awesome icons for this project, as they have significantly more icons to use. 

#### Typography

#### Wireframes


### Features

#### Accounts App

The accounts app will allow users to register for free and create their own unique account. This is built using Django's authentication and authorization to validate profile data. Passwords are hashed for security purposes!

The users will register using the registration form. Registered users will be able to login by using the login form with their username and password or with their email and password.

The users can also reset their password if they forgot the original password using the reset password link on the login.html page.

#### Products App

**Index (Home Page)**

Displays the Featured Products, and the top brands available in the shop.

In this page user can filter the products by gender.

**Product.html**

 Displays all the products available in the website.
 Pagination to display only 8 products per page.
 Users can filter the products based on gender or brand.
 Users can see the product image, name, price.
 Users can add the product to the cart.
 Users can go for more details if they click on the image.


**Product detail.html**
On this page the user can see all the details about the product. The product title, Price and the product features.
If the user want to add the product to the cart they can do from here as well.

#### Home app

 **About.html**
  This page explains about the shop and  how it works 

**Contact.html**
 In the navbar and footer, there is a link for the customer to contact the shop. The user can fill out the form to send an email to reach the shop.
 When the user clicks "send" the email is processed and sent via emailjs to Owner’s email address and user has been notified via message.

 **delivery.html**
In the footer, there is a link for the customer to reach this page. In this page, all the delivery policies are explained including delivery charges for different countries.

**Faqs.html**
 The FAQs page has some common questions and answers, so the user can easily find the relevent one.

 The user can go to the contact page from the button at the end of the page if they have further questions.
 
**Reurn.html**
 
 The reurn page features the reurn policies of the shop.

#### Cart App

**Cart Page**

The shopping cart page features the summary of all the items added to the cart.

The summary includes the the image of the item, title and the price.

A quantity field is displayed with each cart item, giving the ability to adjust the quantity in their cart.

The user can see the Total of the shopping cost and this will be updated when the user update the quantity in their cart.

#### Checkout App

**Checkout.html**

Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity. 

The user need to fill out the payment form in order to go for the payment.

Once the payment is successfull, a message will be displayed.

If there is an error with the payment, the user will be notified with an error message.

#### Search App

This will allow the user to search for a product based on the title.

The search icon is visible from all the pages. When the user click on the icon, the search bar will pop up.

#### Base template 

Features available from all the pages

**Navbar**

In order to create the navbar I have used Bootstrap 4 and the navbar is available in all the pages.

The nabar features The shop logo on the left , which is linked to the homepage, home page, Products and a dropdown for brands.

On the right side of the navbar, the user can reach to the accounts, shopping cart, search page and the contact page.

A user who is currently logged in will see options to see their profile page or log out.

A user who is logged out will see options to register or log in to the website.

The shopping cart icon can lead to cart page. Once the user has added at least one item to their cart a green circle will appear with the number of items in their cart displayed within it.

When the user click on the search icon, The search bar will appaer and the user can type in their relevent product search.

The mail icon ath the right end is linked to contact page.

**Footer**

The footer features on every page with a tag line at the top.

The footer background is dark to give a contrast and obvious separation betwwen the footer and the rest of the page content.

The headings are white and when the user hover over it gently turns to light yellow.

The footer has link to Home, Products, about us, return policy, delivery policy, Faqs and contact us page.

There is a store locator link is available on the footer

The footer also linked to social media accounts.

At the bootom of the footer has copyright information for ticktock watch shop.

### Features Left to Implement

### Technologies Used


  * Visual Studio Code - The IDE used for developing this project.
  * GitHub - Used to store and share all project code remotely.
  * Balsamiq - To create the wireframes for this project.

**Front-End Technologies**
  * HTML5 - Used as the base for markup text.
  * CSS3 -  Used to add styles to the HTML.
  * jQuery 3.4.1 - Used as the primary JavaScript functionality.
  * Stripe - Used to make secure payments.
  * AWS S3 Bucket - Used to store images entered into the database.
  * Travis - Used for continuous integration.
  * Boto3 - To enable creation, configuration and management of AWS S3.
  * Font Awsome - Used for icons in the website.
  * Bootstrap4 - Used to align the elements in the website using the grid system. And also used to create the hamburger button, the modals, the buttons, the badges, the alerts and to style the forms.

  **Back-End Technologies**

  * Python 3.6.7 - Used as the back-end programming language.
  * Django -  Used as my Python web framework.
  * Heroku - for deployment
  * PostgreSQL - Used as relational SQL database plugin via Heroku.
  
 ## Testing 


 ### GitHub Repository

1. Created a repository in GitHub called: “stephyraju/ticktockwatches” https://github.com/stephyraju/ticktockwatches.git

2. Initialised git from the terminal using Git Bash:

git init

3. Created a .gitignore file and I have added the files and folders that won't need to push to GitHub (i.e. '*.sqlite3','env.py','.vscode/','.venv/', pycache, *.pyc)

4. Added the files that I was working on to the Staging area by using:

git add .

5. Run the commit command with the first commit

git commit -m “initial commit"

6. Copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:

 git remote add origin git@github.com:stephyraju/ticktockwatches.git
 
 git push -u origin master

7. I've run regular commits after every important update to the code, and I pushed the changes to GitHub.


### Deployment

#### How to run this project locally

To run this project on your own IDE follow the instructions below:

*  Ensure you have the following tools: - An IDE such as Microsoft Visual Studio Code(or any IDE)

* In order to run this project locally on your own system, you will need the following installed  - PIP - Python 3 - Git

* To allow you to access all functionality on the site locally, create free accounts with the following services: - Stripe - AWS and set up an S3 bucket 

**Instructions**

* Clone this GitHub repository by either clicking the green "Clone or download" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
git clone https://github.com/stephyraju/ticktockwatches

* Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

* Create a .env file with your own credentials.

python -m .venv venv
NOTE: The python part of this command and the ones in other steps below assumes you are working with a windows operating system. Your Python command may differ, such as python3 or py

Activate the .venv with the command:
.venv\Scripts\activate 
Again this command may differ depending on your operating system, please check the Python Documentation on virtual environments for further instructions.

* Install all required modules with the command

 pip -r requirements.txt.
* Set up the following environment variables within your IDE.


        - SECRET_KEY

        - ENVIRONMENT

        - EMAIL_ADDRESS

        - EMAIL_PASSWORD

        - STRIPE_PUBLISHABLE

        - STRIPE_SECRET

        - DATABASE_URL

        - AWS_ACCESS_KEY_ID

        - AWS_SECRET_ACCESS_KEY

* In the IDE terminal, use the following command to launch the Django project:
python manage.py runserver.

* The Django server should be running locally now on http://127.0.0.1:8000 (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.
* When you run the Django server for the first time, it should create a new SQLite3 database file: db.sqlite3.

* Next, you'll need to make migrations to create the database schema:
      * python manage.py makemigrations
      * python manage.py migrate
* Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:

     * python manage.py createsuperuser
     * Assign an admin username,email,and secure password.
* Now you can run the program locally with the following command:

    * python manage.py runserver

* Note - If you are having issues viewing static files you may need to collect static with the below command.
    * python3 manage.py collectstatic

#### Heroku Deployment

To deploy TickTock  to heroku, take the following steps:

1. Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

2. Create a Procfile with the terminal command echo web: python app.py > Procfile.

3. git add and git commit the new requirements and Procfile and then git push the project to GitHub.

4. Sign up for a free Heroku account, Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub, and enable Automatic Deployment.

6. In the Heroku Resources tab, navigate to the Add-Ons section and search for Heroku Postgres. Select the free Hobby level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your .env file with your new database-url details.
Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on settings tab and then click on the Reveal config vars button to configure environmental variables.

Set the following config vars:

          | Key	                    |     Value                    |
          | ---------------------   | -----------------------      |
          | SECRET_KEY	            | <your_secret_key>            |
          | STRIPE_PUBLISHABLE      |	<your_stripe_publishable>    |
          | STRIPE_SECRET	          | <your_stripe_secret>         |
          | AWS_ACCESS_KEY_ID       | <your_secret_key>            |
          | AWS_SECRET_ACCESS_KEY   | <your secret key>            |
          | AWS_STORAGE_BUCKET_NAME | <your AWS S3 bucket name>    |
          | DATABASE_URL	          | <your postgres database url> |
          | EMAIL_ADDRESS           | <your email address>         | 
          | EMAIL_PASSWORD          | <your password>              |

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.
