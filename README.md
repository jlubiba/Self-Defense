# Self-Defense
# Self-Defense Learning Platform

## Description

This project is a **comprehensive self-defense learning platform** designed to teach users the art of self-defense through:
- **Video tutorials**
- **Written content**
- A **blog** for additional tips and insights.

Additionally, the platform incorporates an **e-commerce module**, enabling users to purchase premium content, self-defense equipment, and other related products. The application is built with a modern tech stack to ensure scalability, user-friendliness, and high performance.

## Features

### General
	•	User Authentication: Secure registration and login functionality with role-based access.
	•	Admin Dashboard: Manage users, blog posts, tutorials, and product listings.

### Blog
	•	Rich Content Management: Publish articles with subtitles, images, and tables.
	•	Categorization & Tags: Organize posts into categories with tagging functionality.
	•	Commenting System: Allow users to engage by commenting on blog posts.

### Tutorial Section
	•	Video Tutorials: Stream high-quality instructional videos.
	•	Written Tutorials: Provide detailed step-by-step guides.
	•	Progress Tracking: Track users’ learning progress through tutorials.

### E-Commerce
- **Product Listings**: Sell self-defense equipment and premium content.
- **Secure Payments**: Integrates with payment gateways like Stripe or PayPal for transactions.
- **Order History**: Users can view their order history and invoices.

### Technology Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: JavaScript, Bootstrap, Django Templates (DTL)
- **Databases**: SQLite (development) & MySQL (production)
- **Deployment**: Ready for deployment on platforms like Heroku or AWS.

## Table of Contents
1.	[Description](#description)
2.	[Features](#features)
3.	[Installation](#installation)
4.	[Usage](#usage)
5.	[Technologies Used](#technologies-used)
6.	[Contributing](#contributing)
7.	[Screenshots](#screenshots)

### Installation

Follow these steps to set up the project locally:
1.	Clone the repository:

```
git clone <repository-url>
cd self-defense-platform
```


2.	Create and activate a virtual environment:

```
pipenv shell
```


3.	Install dependencies:

```
pipenv install django
pipenv install django-ckeditor
pipenv install djangorestframework
pipenv install djangorestframework-xml 
pipenv install djangorestframework-yaml
pipenv install django-filter
pipenv install djoser
pipenv install bleach
```


4.	Set up the database:
- For development, SQLite is used by default.
- For production, configure MySQL in the settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5.	Apply migrations:

```
python manage.py migrate
```

6.	Create a superuser:

```
python manage.py createsuperuser
```

7.	Start the development server:

```
python manage.py runserver
```

8.	Access the app in your browser at 
- http://127.0.0.1:8000.

## Usage

### Blog
- Visit /blog/ to view blog posts.
- Admins can create, edit, and delete posts through the admin panel (/admin).

### Tutorials
- Video tutorials are accessible at /tutorials/videos/.
- Written guides can be found at /tutorials/written/.

### E-Commerce
- Products are listed under /store/.
- Users can add products to their cart, proceed to checkout, and view order history.

## Technologies Used

### Backend
- **Django**: Backend framework for building the core logic.
- **Django REST Framework (DRF)**: API development for integrating with the frontend and external services.

### Frontend
- **JavaScript**: Interactive UI elements.
- **Bootstrap**: Responsive design for mobile and desktop users.
- **Django Templates (DTL)**: Server-side rendering of dynamic content.

### Databases
- **SQLite**: Development environment.
- **MySQL**: Production environment for better scalability. # Will be added later

### Additional Tools
- **Payment Gateway**: Stripe/PayPal integration.
- **Rich Text Editor**: CKEditor for creating formatted blog posts and tutorials.

## Contributing

We welcome contributions to this project! To contribute:
1.	Fork the repository.
2.	Create a new branch for your feature or bug fix:

```
git checkout -b feature-name
```

3.	Commit your changes:

```
git commit -m "Add your message here"
```

4.	Push the branch to your fork:

```
git push origin feature-name
```

5.	Open a pull request on the main repository.


## Screenshots

<!-- Need to include screenshots of the blog, tutorial pages, e-commerce pages, and admin panel to give users a visual overview of the project. -->