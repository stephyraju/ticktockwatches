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
