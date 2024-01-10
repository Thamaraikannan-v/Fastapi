FastAPI User Management System

The provided code comprises a simple User Management System using FastAPI, enabling CRUD (Create, Read, Update, Delete) operations for users. It includes endpoints to manipulate user data stored in memory.

Features:
API Endpoints:

GET /api/users: Retrieves a list of all users stored in the in-memory database.
POST /api/users: Adds a new user to the database.
PUT /api/users/{user_id}: Updates an existing user by their unique user_id.
Data Structures:

User Model: Defines the structure for a user, including id, first_name, last_name, gender, and roles.
Gender Enum: Represents gender options for users, allowing values of "male" or "female".
Role Enum: Represents roles available for users, including "admin", "user", and "student".
UserUpdateRequest Model: Specifies the fields that can be updated for a user (e.g., first_name, last_name, roles) using the PUT endpoint.
Functionality:

GET Endpoint: Fetches the list of users.
POST Endpoint: Adds a new user to the database.
PUT Endpoint: Updates an existing user by their user_id with optional fields (first_name, last_name, roles).
Error Handling:

Handles cases where the user doesn't exist (e.g., in the PUT endpoint) by raising an HTTPException with a 404 status code.
