# Pet Adoption Django Project

ეს პროექტი არის Django-based აპლიკაცია ცხოველთა თავშესაფრისთვის.

## ფუნქციები
- მომხმარებლის პროფილის გვერდი
- ცხოველთა CRUD ოპერაციები (create, read, update, delete)
- კონკრეტული ცხოველის დეტალური გვერდი
- მარტივი ძებნა ცხოველებში
- თემფლეითები და CSS სტილები
- Docker მხარდაჭერა

## სქემები / ტექნოლოგიები
- Python 3.9
- Django 4.2
- SQLite (ან სხვა DB მოთხოვნის მიხედვით)
- Bootstrap / CSS
- Docker & Docker Compose (optional)

## Project Setup

### 1. კლონირება GitHub-დან
```bash
git clone https://github.com/username/pet-adoption-django-project.git
cd pet-adoption-django-project
2. ვირტუალური გარემო (თუ Docker არ გამოიყენება)
bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
3. მიგრაციები
bash
Copy code
python manage.py makemigrations
python manage.py migrate
4. აპლიკაციის გაშვება
bash
Copy code
python manage.py runserver
გახსენით ბრაუზერში: http://localhost:8000

Docker Instructions
Build Docker Image
bash
Copy code
docker build -t pet-adoption .
Run Docker Container
bash
Copy code
docker run -it -p 8000:8000 pet-adoption
გახსენით ბრაუზერში: http://localhost:8000

Docker Compose (თუ გამოიყენება)
bash
Copy code
docker-compose up --build
Git Ignore
.gitignore უკვე მოიცავს:

__pycache__/, .pyc ფაილები

.env, db.sqlite3

media/ და staticfiles/

დამატებითი ინფორმაცია
პროექტის დოკუმენტაცია და სიტყვიერი აღწერა დოკუმენტაციაშია.

ნებისმიერი საკითხი შეგიძლიათ ჩაწეროთ GitHub Issues-ში.

markdown
Copy code
