# Blog-App
A simple Django-powered blogging application where users can view posts, leave comments, and explore posts by categories.
## Features

- **Post Management**: Users can view published blog posts and browse posts by category.
- **Comments Section**: Each blog post has a comment section where users can leave their feedback.
- **Category Filter**: Posts can be filtered based on categories using the dropdown in the navigation bar.
- **Responsive Design**: The app is fully responsive and styled using Bootstrap for an optimal user experience on any device.
- **Admin Interface**: Django’s built-in admin interface is available to manage posts, categories, and comments.

## Prerequisites 

Ensure you have the following installed on your machine:
- Python 3.12
- Django 5.1

## Setup and Installation

1. **Clone the repository:**

```bash
git clone https://github.com/abiboo-123/Blog-App.git
cd Blog-App
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install the dependencies:**

```bash
pip install django
pip install pillow
```

4. **Run database migrations:**

```bash
python manage.py migrate
```

5. **Create a superuser:** A superuser with the following credentials is already set up:

- Username: ``` admin ```
- Password: ``` admin ```

If you want to create your own, you can do so using:

```bash
python manage.py createsuperuser
```

6. **Run the development server:**


```bash
python manage.py runserver
```

7. **Access the application: Open your browser and visit:**
- **Frontend**: ```http://127.0.0.1:8000/```
- **Admin panel**: ```http://127.0.0.1:8000/admin```

## How to Use

- Browse posts from the homepage.
- Use the dropdown menu in the navbar to filter posts by categories.
- Open a post to view its content and leave a comment.
- Admins can log in via the admin panel to create, update, or delete posts and manage comments.
