# Dream Garage 

A full-stack web application built to catalog and manage a collection of high-performance vehicles. This project demonstrates core database operations, media handling, and dynamic user interfaces using the Django framework.

##  Features
* **Full CRUD Operations:** Create, Read, Update, and Delete vehicles directly from the frontend interface.
* **Media Management:** Securely upload and serve custom vehicle images.
* **Dynamic Search:** Query the SQLite database by make, model, or engine specifications.
* **Pagination:** Clean, scalable UI that limits the number of vehicles displayed per page.
* **Responsive Design:** Styled with Bootstrap 5 for a seamless mobile and desktop experience.

##  Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Libraries:** Pillow (Image Processing)

##  Local Setup & Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/briankimani640/dream-garage.git
   cd dream-garage
  
2. **Create and activate a virtual environment:** 
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **  Install the required dependencies: **
   ```bash
   pip install django pillow



4. ** Apply database migrations: **
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. ** Run the development server: **
   ```bash
   python manage.py runserver

6. ** viewing the page **
   ```bash
   Open http://127.0.0.1:8000/ in your browser to view the application 

