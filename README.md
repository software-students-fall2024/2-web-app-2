# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

A web application that allows users to manage, organize, and interact with data stored in a MongoDB database. The app provides features for adding, editing, deleting, and searching data, ensuring a user-friendly and mobile-optimized experience.

## User stories
As a user, I want to add new items to the database so that I can manage my information effectively.
As a user, I want to view a list of all items in the database so that I can see my stored data.
As a user, I want to search for specific items so that I can find them quickly.
As a user, I want to edit existing items so that I can update or correct information when needed.
As a user, I want to delete items I no longer need so that the database does not get too large or messy.
As a mobile user, I want the application to be optimized for mobile devices so that I can use it conveniently on the go.
As an administrator, I want to ensure data integrity by validating input data before it is added to the database.

[All issues](Issues.md)

## Steps necessary to run the software
1. Clone the Repository to local

2. Set Up Environment
Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

If you’re on Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
Install all required Python packages using `pip`:
pip install -r requirements.txt

4. Set Up MongoDB
- **Option 1: Local Installation**
  - Install MongoDB Community Edition ([instructions here](https://www.mongodb.com/docs/manual/installation/)).
  - Start MongoDB locally:
    mongod --dbpath /usr/local/var/mongodb

5. Configure Environment Variables
Set up a `.env` file to store your MongoDB connection string:
MONGO_URI=mongodb://localhost:27017/yourdatabase

Replace `yourdatabase` with the name of your database.

6. Run the Application
Start the Flask development server:
python runby.py
You should see output similar to this:
Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

7. Access the Application
Open the web:
```
http://127.0.0.1:5000
```

## Task boards
sprint1:
- **To Do**: User stories planned for this sprint are placed here.
- **In Progress**: User stories currently being worked on are moved to this column.
- **Done**: User stories that are fully implemented and tested are moved 

[repository link](https://github.com/software-students-fall2024/2-web-app-2)

