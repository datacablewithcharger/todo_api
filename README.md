
# Todo App - Django Project

This is a simple Todo application built using Django. It includes basic CRUD operations for managing tasks. Users can create, update, delete, and view tasks using both a web interface and an API.

## Project Setup Instructions

### Prerequisites

- **Python 3.x**
- **Django 3.x or higher**
- **Django REST Framework**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/todo_api.git
   cd todo_api
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   
   # If requirements.txt doesn't exist, you can manually install the required packages:
   pip install django djangorestframework
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser to access the Django admin panel (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Project Structure

```
/Todo-App-Assignment
│
├── todos/                      # Application folder
│   ├── migrations/             # Django migrations
│   ├── models.py               # Todo model
│   ├── forms.py                # Todo form
│   ├── views.py                # Views for handling CRUD operations
│   ├── serializers.py          # API serializers
│   └── templates/              # HTML templates for web interface
│       └── todos/
│           ├── todo_list.html  # Displays the list of todos
│           ├── todo_form.html  # Form for creating/updating todos
│
├── manage.py                   # Django management script
└── requirements.txt            # Dependencies list
```

## How to Use the Application

### Home Screen
This is how the home screen looks:
![Screenshot (891)](https://github.com/user-attachments/assets/97c43437-f2b2-4ed3-a0fb-fc466d9cd53e)


### Add a New Task
Click on the "Add New Task" button on the homepage, fill out the title and description, then submit the form.
![Screenshot (892)](https://github.com/user-attachments/assets/9863aabb-e263-4a15-a712-576dee21d02f)


### Error Handling
If the title or description is empty or not filled, an error will be displayed.
![Screenshot (894)](https://github.com/user-attachments/assets/2e75c61d-0570-44be-a3bb-28ea4ee8f6d4)


### Update a Task
Click on a task's title to update its details.
![Screenshot (893)](https://github.com/user-attachments/assets/525489b4-0d67-4a19-8279-fddc35884c5c)


### Delete a Task
Click the trash icon next to a task to delete it.
![Screenshot (895)](https://github.com/user-attachments/assets/ce6c5be4-ddb0-4629-a230-c74ddfa6cc4d)


---

### Make sure to replace `your-username` in the clone URL with your actual GitHub username. 

---

### License
This project is licensed under the MIT License. You are free to use, modify, and distribute this code as long as the original license is included.


