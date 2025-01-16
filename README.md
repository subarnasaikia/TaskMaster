# TaskMaster

TaskMaster is a simple and efficient To-Do List web application created using Django and Django templates. It provides CRUD (Create, Read, Update, Delete) functionality to manage your to-do items efficiently.

## Features

- **Add Tasks**: Create new to-do items with a title and description.
- **View Tasks**: Display a list of all your tasks with their details.
- **Edit Tasks**: Update existing to-do items to modify their content.
- **Delete Tasks**: Remove tasks that are no longer needed.

## Installation

### Prerequisites

- Python 3.6+
- Django 3.0+
- Git

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/subarnasaikia/TaskMaster.git
   cd TaskMaster
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   This step ensures that the required dependencies for the project are isolated from your global Python installation.
   
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   Once activated, your command prompt should change to indicate that you're now working within the virtual environment.

3. **Install Dependencies**:
   Now, install the required Python packages that the project depends on by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   The application uses a database to store the to-do items. Apply the migrations to create the necessary database tables:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   You can now start the development server to view the application in your browser:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:8000` to access TaskMaster.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy task managing with TaskMaster!
