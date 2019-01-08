# Item Catalog App

# Patricio Villar

## Overview

You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users 
will have the ability to post, edit and delete their own items. Modern web applications perform a variety of functions and provide amazing features and utilities to their users; 
but deep down, it’s really all just creating, reading, updating and deleting data. In this project, you’ll combine your knowledge of building dynamic websites with persistent data 
storage to create a web application that provides a compelling service to your users.


## Technologies Used

- Facebook / Google Login
- OAuth
- Python
- HTML
- CSS
- Bootstrap
- Flask
- Jinja2
- SQLAchemy



## Link To Udacity Vagrantfile VM

- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)

## Instructions to Run the App

- Install Vagrant and VirtualBox
- Clone the Vagrantfile from the Udacity Repo
- Clone this repo into the `catlog/` directory found in the Vagrant directory
- Run `vagrant up` to run the virtual machine, then `vagrant ssh` to login to the VM
- from the main directory run `sudo pip install -r requirements`
- Generate a fresh DB file, by running 'python database_setup.py'
- Populate DB with 3 categories, by running 'python feedcatalog.py'
- run application with `python application.py` from within its directory
- go to `http://localhost:8000` to access the application



## JSON API Endpoints

`/api/v1/catalog/JSON` - Returns JSON of all items in catalog

`/api/v1/categories/JSON` - Returns JSON of all categories in catalog


## REST Endpoints

#### Useful Categories links

`/` or `/categories` - Returns catalog page with all categories and recently added items

`/categories/new` - Allows user to create new category

`/categories/<int:category_id>/edit/` - Allows user to edit an existing category

`/categories/<int:category_id>/delete/` - Allows user to delete an existing category


#### Useful Items links

`/categories/<int:category_id>/` or `/categories/<int:category_id>/items/` - returns items in category

`/categories/<int:category_id>/item/<int:catalog_item_id>/` - returns category item

`/categories/item/new` - return "This page will be for making a new catalog item

`/categories/<int:category_id>/item/<int:catalog_item_id>/edit` - return "This page will be for making a updating catalog item"

`/categories/<int:category_id>/item/<int:catalog_item_id>/delete` - return "This page will be for deleting a catalog item"


## Future Improvements

- Add one more abstraction level "tenants", so we can store categories for different clients.
- Add Image upload support
- HTML layout and CSS styling.

