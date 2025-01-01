OVERVIEW
The DRF Movie Review API is an application programming interface (API) built using Django and Django REST Framework (DRF) that allows users to manage and interact with movie reviews. It is designed to handle tasks like user authentication, managing reviews for movies, and providing endpoints to perform CRUD (Create, Read, Update, Delete) operations on reviews. This API serves as a backend system for applications that require movie review functionality.

OBJECTIVES
Implement the ability to Create, Read, Update, and Delete (CRUD) reviews.
Implement CRUD operations for users.
Efficient Database designs using ORM
Use Django Rest Framework (DRF) to design and expose the API endpoints.
Ensure secure access through token-based authentication.
Provide endpoints for searching and filtering data.
Implement efficient error handling and data validation ith relevant HTTP status codes 
Deploy the API on live environment.


Key Features of the DRF Movie Review API:

Review Management (CRUD):
Users can create, read, update, and delete reviews.
Each review includes:
Movie Title: The title of the movie being reviewed.
Review Content: The text describing the user's opinion.
Rating: A numerical score (e.g., out of 5 stars).
User ID: The identifier for the user who submitted the review.
Timestamps: Created and updated dates for reviews.

User Management (CRUD):
Custom user model with unique usernames, emails, and passwords.
Users can register, log in, and manage their accounts.
Authentication ensures that only registered users can submit or modify reviews.
Movie Review Retrieval:
Users can view reviews for a specific movie by searching or filtering by the movie's title.
Pagination ensures efficient handling of large datasets.
Review Search and Filtering:
Search by movie title or rating.
Filter reviews to display only those with specific ratings (e.g., 4-star or 5-star reviews).
Authentication and Authorization:
Uses JWT (JSON Web Token) for secure authentication.
Ensures only authenticated users can create or modify their reviews.
Enforces permissions to prevent users from editing or deleting reviews by others.
Database Management:
Django ORM (Object-Relational Mapping) manages the database.
Models for users and reviews ensure a robust relational data structure.


Technology Stack
Python
Django
Backend Framework: Django and Django Rest Framework (DRF).
Database: MYSQL for both development and  production.
Json Web Token(JWT): JWT was used to generate Authentication token
Postman: Postman was used for user authentication using Token(JWT)

Use Case:
This API is ideal for:
Movie review websites or apps.
Platforms where users can share and browse reviews for films.
Backend services for movie-related applications requiring user-generated content.



