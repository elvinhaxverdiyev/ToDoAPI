ToDo App API
This is a simple ToDo application API built using Django and Django REST Framework. The app allows users to create, update, read, and delete tasks.

Key Features
Create ToDo Tasks: Users can create new tasks.
Update ToDo Tasks: Users can update the status of existing tasks.
Read ToDo Tasks: Users can retrieve a list of all tasks or details of a specific task.
Delete ToDo Tasks: Users can delete existing tasks.
Usage
1. Get All ToDo Tasks (GET)
You can retrieve all tasks by using the GET method with the /api/v1/todos/ endpoint.

2. Create a New ToDo Task (POST)
To create a new task, use the POST method with the /api/v1/todos/ endpoint. You can send the task title, text, and status in the request body.

3. Get a Specific ToDo Task (GET)
To retrieve a specific task, use the GET method with the /api/v1/todos/{id}/ endpoint.

4. Update a ToDo Task (PATCH)
To update an existing task, use the PATCH method with the /api/v1/todos/{id}/ endpoint.

5. Delete a ToDo Task (DELETE)
To delete a task, use the DELETE method with the /api/v1/todos/{id}/ endpoint.
