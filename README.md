[![Build Status](https://travis-ci.com/stephyraju/ticktockwatches.svg?branch=master)](https://travis-ci.com/stephyraju/ticktockwatches)

# [TickTock Watches](https://ticktockwatches.herokuapp.com/)

Milestone Project - 4

This is the last milestone project for the Fullstack Web Developer course with Code Institute. The aim of the project is to showcase my skills learnt throughout this course. 

Throughout this project I have used [Python](https://www.python.org/), a high-end programming language along with [Django](https://www.djangoproject.com/), a python framework.

The deployed site can be found at [TickTock](https://ticktockwatches.herokuapp.com/).

----------

## Table Of Contents

**1. [UX](#ux)**
  * [User Stories](#user-stories)
  * [Design](#design)
    * [Framework](#framework)
    * [Color Scheme](#color-scheme)
    * [Icons](#icons)
    * [Typography](#typography)
  * [Wireframes](#wireframes)

**2. [Features](#features)**

  * [Existing Features](#existing-features)
  * [Features Left to Implement](#features-left-to-implement)

**3. [Technologies Used](#technologies-used)**

  * [Front-End Technologies](#front-end-technologies)
  * [Back-End Technologies](#back-end-technologies)

**4. [Testing](#testing)**



**5. [Github Repository](#github-repository)**

**6. [Deployment](#deployment)**

  * [Local Deployment](#how-to-run-this-project-locally)
  * [Heroku Deployment](#heroku-deployment)

**7. [Credits](#credits)**

-----------------------------

## UX

This project is part of my Code Institute Full Stack Software Development studies, specifically the Full Stack Frameworks module. The purpose of the project was to create a website for an online watch shop where the company can displays their products for the customers. This website is designed in a simple and efficient way for the customers to have a smooth and pleasant shopping experience.

## User Stories

  * As a user I want to view the site from any device (mobile, tablet, desktop).
  * As a user I want to see the products without login.
  * As a user I want to create my account.
  * As a user I want to view my profile.
  * As a user I want to update my profile.
  * As a user I want to login and logout.
  * As a user I want to be able to change my password.
  * As a user I want to filter the products based on gender and brand.
  * As a user I want to search for a product.
  * As a user I want to be able to save products as favourites.
  * As a user I want to be able to see the product details.
  * As a user I want to be able add product to my cart and remove if I change my mind.
  * As a user I want to be able to navigate the shop easily, find what I need and make a safe and secure purchase.
  * As a user I can view my order summary before checkout.
  * As a userI want to be able to follow the shop on social media.
  * As a user I can see the services and policies of the shop.
  * As a user I can view the frequently asked questions page for any questions about the order.
  * As a user I want to be able to contact the shop for any quiries via contact form.

  
## Design


### Framework

  * [Bootstrap 4](https://getbootstrap.com/)
  * [jQuery 3.4.1](https://code.jquery.com/jquery/)
    * In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
  * [Django 1.11](https://www.djangoproject.com/)
    * Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap. We were taught how to use Django 1.11 in the lessons, despite Django 2.0 being the current version,I used Django 1.11

### Color Scheme

  For the color scheme, I've used gray and black in the navbar and most pages. I chose teal and thistle for some icons and headings to highlight. Overall, I tried to keep a simple classic look.

### Icons

* [Font Awsome 5.11.2](https://fontawesome.com/)

    I prefer to use Font Awesome icons for this project, as they have significantly more icons to use. 

### Typography

The following fonts were used :

  * [Bree](https://fonts.google.com/specimen/Bree+Serif)
  * [sans-serif](https://fonts.google.com/specimen/Open+Sans?selection.family=Open+Sans)

### Wireframes

Mock-ups were created early on in this project.

I've used [Balsamiq](https://balsamiq.com/) Wireframes during the Scope Plane part of the design and planning process for this project.

All of my wireframes for this project can be found [here](https://github.com/stephyraju/ticktockwatches/tree/master/documents/wireframes)

------------------------

## Features

### Accounts App

The accounts app will allow users to register for free and create their own unique account. This is built using Django's authentication and authorization to validate profile data. Passwords are hashed for security purposes.

The users will register using the registration form. Registered users will be able to login by using the login form with their username and password or with their email and password.

The users can also reset their password if they forgot the original password using the reset password link on the login.html page.

### Products App

**index (Home Page)**

Displays the Featured Products, and the top brands available in the shop.

In this page user can filter the products by gender.

**product.html**

 Displays all the products available in the website.
 Pagination to display only 8 products per page.
 Users can filter the products based on gender or brand.
 Users can see the product image, name, price.
 Users can add the product to the cart.
 Users can go for more details if they click on the image.


**product_detail.html**

On this page the user can see all the details about the product. The product title, Price and the product features.
If the user want to add the product to the cart they can do from here as well.

### Home app

 **about.html**

  This page explains about the shop and  how it works.

**contact.html**

 In the navbar and footer, there is a link for the customer to contact the shop. The user can fill out the form to send an email to reach the shop.
 When the user clicks "send" the email is processed and sent to Owner’s email address and user has been notified via message.

**delivery.html**

In the footer, there is a link for the customer to reach this page. In this page, all the delivery policies are explained including delivery charges for different countries.

**faqs.html**

 The FAQs page has some common questions and answers, so the user can easily find the relevent one.

 The user can go to the contact page from the button at the end of the page if they have further questions.
 
**return.html**
 
 The reurn page features the reurn policies of the shop.

### Cart App

**cart.html**

The shopping cart page features the summary of all the items added to the cart.

The summary includes the the image of the item, title and the price.

A quantity field is displayed with each cart item, giving the ability to adjust the quantity in their cart.

The user can see the Total of the shopping cost and this will be updated when the user update the quantity in their cart.

### Checkout App

**checkout.html**

Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity. 

The user need to fill out the payment form in order to go for the payment.

Once the payment is successfull, a message will be displayed.

If there is an error with the payment, the user will be notified with an error message.

### Search App

This will allow the user to search for a product based on the title.

The search icon is visible from all the pages. When the user click on the icon, the search bar will pop up.

### Favourite App

This will allow users to add or remove the products by clicking the heart icon on the product card.

The user can see all their favourite products in the favourite page which can be accessed by clicking on the heart icon from the navbar.

### Base Template 

Features available from all the pages

**Navbar**

In order to create the navbar I have used Bootstrap 4 and the navbar is available in all the pages.

The nabar features The shop logo on the left , which is linked to the homepage, home page, Products and a dropdown for brands.

On the right side of the navbar, the user can reach to the Accounts, Shopping cart, Search page and the Contact page.

A user who is currently logged in will see options to see their profile page or log out.

A user who is logged out will see options to register or log in to the website.

The shopping cart icon can lead to cart page. Once the user has added at least one item to their cart a green circle will appear with the number of items in their cart displayed within it.

When the user click on the search icon, The search bar will appaer and the user can type in their relevent product search.

The mail icon at the right end is linked to contact page.

**Footer**

The footer features on every page with a tag line at the top.

The footer background is dark to give a contrast and obvious separation betwwen the footer and the rest of the page content.

The headings are white and when the user hover over it gently turns to light yellow.

The footer has link to Home, Products, About Us, Return policy, Delivery policy, Faqs and Contact us page.

There is a store locator link is available on the footer which can lead to the google map location.

The footer also linked to social media accounts.

At the bootom of the footer has copyright information for ticktock watch shop.

## Features Left to Implement

1. Order confirmation report and emails to customer when they place an order.
2. Checkout pages to include a field for customer to get delivery charges.
3. Add sorting and filtering options to make it more easier to slelect the product.
4. Review and rating section for users for each product they buy.
5. User profile page will show more details like buying history of the user.

-----------------------

## Technologies Used


  * [Visual Studio Code](https://code.visualstudio.com/) - The IDE used for developing this project.
  * [GitHub](https://github.com/) - Used to store and share all project code remotely.
  * [Balsamiq](https://balsamiq.com/) - To create the wireframes for this project.

**Front-End Technologies**
  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
  * [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3) -  Used to add styles to the HTML.
  * [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
  * [Stripe](https://stripe.com/docs/api) - Used to make secure payments.
  * [AWS S3 Bucket](https://aws.amazon.com/) - Used to store images entered into the database.
  * [Travis](https://travis-ci.org/) - Used for continuous integration.
  * [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - To enable creation, configuration and management of AWS S3.
  * [Font Awsome](https://www.bootstrapcdn.com/fontawesome/) - Used for icons in the website.
  * [Bootstrap4](https://www.bootstrapcdn.com/) - Used to align the elements in the website using the grid system. And also used to create the hamburger button, the modals, the buttons, the badges, the alerts and to style the forms.

  **Back-End Technologies**

  * [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.
  * [Django](https://docs.djangoproject.com/) -  Used as my Python web framework.
  * [Heroku](https://www.heroku.com/) - for deployment
  * [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.
  
------------------------
 # Testing 

## Automated Testing

### Validation Services

  * **HTML**: I have used [https://validator.w3.org/](https://validator.w3.org/) in order to validate the HTML code.

  * **CSS**: I have used [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) in order to validate the CSS code.

  * **JavaScript**: I have used [https://jshint.com/](https://jshint.com/) in order to check the JavaScript code.

### Coverage
coverage.py was used to provide feedback during testing to check that enough of my code had been tested.

 I built 52 different tests to encompass most of my python views, forms, and models. Using the coverage.py test package, those 52 tests have provided an overall result of 75% test coverage.

 In some cases the tests were quite complicated and in these cases I have chosen to test manually since I was running out of time to present the project.

How to run coverage
  * Activate your virtual environment.
  * In the terminal enter the following command:
    * coverage html
    * Open the newly created htmlcov directory in the root of your project folder.
    * Open the index.html file inside it.
    * Run the file in the browser to see the output.

All the **coverage report** for this project can be found **[here](https://github.com/stephyraju/ticktockwatches/tree/master/documents/coverage_report)**

### Travis

Travis was used for continuous integration testing. At the top of this Readme file you can see that the website passes the Travis test. The Travis Documentation provides all the info needed to set it up.

[![Build Status](https://travis-ci.com/stephyraju/ticktockwatches.svg?branch=master)](https://travis-ci.com/stephyraju/ticktockwatches)

## Manual Testing


I have a detailed **checklist** of all the manual testing that has been done to confirm all areas of the site work as expected.

**Click** **[here](https://github.com/stephyraju/ticktockwatches/blob/master/documents/my_checklist%20.pdf)** to see the **checklist** that I have used to test the main features.

#### Stripe payment testing

My checkout app is using the stripe payment for the payment option. I tested this by using Stripes test card (4242 4242 4242 4242) I tested the forms and ensured all my validation worked as expected and my logic was performing as expected. The checkout app works from the Stripe API.

Card number - 4242424242424242

CVC - Any 3 digit number.

Expiry date - Any date in the future.


### Responsiveness

Chrome DevTools and physical devices were used throughout development for a number of purposes, one of which was to test the responsiveness and rendering across a range of sizes and devices. As issues were found they were either fixed at the time or noted and returned to later.

The site has been tested successfully on

Apple Macbook Air - Safari browser

Apple iPhone 6,7 &8S - Safari Browser

iPad Mini - Safari Browser

Desktop - Chrome v.74

Desktop - Firefox v.67


### Known Bug

I have added favourite functionality to facilitate user to add their favourite products and would be able to view favourites when click on the heart icon on the navbar. When user click on the heart icon on the product card it will turn to solid to indicate that product is added to favourite list, this part is working. But the user can't see their favourite product from the favourite page. I have decided to keep it as it is for now and will tackle this bug for the future release.

-------------------------
### GitHub Repository

1. Created a repository in GitHub called: “stephyraju/ticktockwatches” https://github.com/stephyraju/   ticktockwatches

2. Initialised git from the terminal using Git Bash:

    git init

3. Created a .gitignore file and I have added the files and folders that won't need to push to GitHub (i.e. '*.  sqlite3','env.py','.vscode/','.venv/', pycache, *.pyc)

4. Added the files that I was working on to the Staging area by using:

   git add .

5. Run the commit command with the first commit

  git commit -m “initial commit"

6. Copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:

 git remote add origin git@github.com:stephyraju/ticktockwatches.git
 
 git push -u origin master

7. I've run regular commits after every important update to the code, and I pushed the changes to GitHub.


## Deployment

### How to run this project locally

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


### Heroku Deployment

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
  | AWS_SECRET_ACCESS_KEY   | <your_secret_key>            |
  | AWS_STORAGE_BUCKET_NAME | <your_AWS_S3_bucket_name>    |
  | DATABASE_URL	          | <your_postgres_database url> |
  | EMAIL_ADDRESS           | <your_email_address>         | 
  | EMAIL_PASSWORD          | <your_password>              |

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

------------------------

## Credits

**Content**

All the product details, images and the contents for the services and policies are from https://www.watchshop.com/, https://www.fields.ie/ & Wikipedia and I modifed to use in the project.

**Tutorials**

* [Python Django Tutorial by Corey Schafer](https://www.youtube.com/watch?v=F5mRW0jo-U4)

* [https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859](https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859)

* The [Django documentation](https://devdocs.io/django~1.11/)

### Acknowledgement
The tutors, mentors and support staff at Code Institute

Special thanks to Guido Cecilio Garcia, my Code Institute mentor, for his guidance and advice whilst working on this project.

**Disclaimer**

 The content of this website is for educational purposes only.