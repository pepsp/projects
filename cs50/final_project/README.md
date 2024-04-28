# WEEK PLANNER
#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=M_9NLNJ4opk)>
#### Description:
This Week Planner is a simple web application that allows users to plan their week by adding tasks, you can set a task every half-hour of the day.
Monday to Friday.
Users can view their weekly schedule, edit tasks, and clear all tasks.
The application utilizes Flask as the web framework and SQLite for the database to store tasks and days of the week.

### Features:
1. **View Weekly Schedule**: Users can view their weekly schedule with tasks displayed Monday thru Friday by half-hour intervals.
2. **Edit Tasks**: Users can edit existing tasks by overwritting them, or add new tasks for specific days and times.
3. **Clear All Tasks**: Users can clear all tasks from the schedule.

### Project Structure:
- `app.py`: Contains the Flask application code, including routes for rendering templates and handling user requests.
- `index.html`: HTML template for displaying the weekly schedule table.
- `edit.html`: HTML template for editing tasks.
- `missing.html`: HTML template for displaying an error message if any required field is missing.
- `week.db`: SQLite database file containing tables for days and tasks.
- `table-index.html` HTML template for the week table, it allows it to be displayed more easily with less code.

## Project Routes

### 1. /
- **Method:** GET
- **Function:** index()
- **Description:** Renders the index.html template with data fetched from the database.
- **Variables Passed:** days, tasks, starts
- **Template Rendered:** index.html

### 2. /edit
- **Methods:** GET, POST
- **Function:** edit()
- **Description:** Allows users to edit tasks. If accessed via GET method, renders edit.html template with existing data. If accessed via POST method, updates or inserts tasks into the database.
- **Variables Passed (GET):** days, tasks, starts
- **Variables Passed (POST):** day, start, task
- **Template Rendered (GET):** edit.html
- **Template Rendered (POST):** Redirects to /edit if successful, else renders missing.html template if any required field is missing.

### 3. /clear
- **Method:** GET
- **Function:** clear()
- **Description:** Clears all tasks from the database.
- **Template Rendered:** Redirects to /



## Database Tables

### 1. days
- **Columns:**
  - id: INTEGER (Primary Key, Autoincrement)
  - day_name: TEXT (Not Null, Unique)

### 2. tasks
- **Columns:**
  - id: INTEGER (Primary Key, Autoincrement)
  - title: TEXT (Not Null)
  - start: TIME (Not Null)
  - day_id: INTEGER (Not Null, Foreign Key referencing days(id))



### Usage:
1. Run the Flask application using `Flask run` inside the correct directory.
2. Open your web browser and navigate to `http://localhost:5000` to access the application.
3. Enter the 'Edit Week' link on the page's header.
4. Select one or more days to input a task that occurs at the same hour but different day.
5. Select the time for a task you want to set-up on the table.
6. Input the title for the task.

This project is a basic example of using Flask and SQLite to create a web application for managing tasks and scheduling.
