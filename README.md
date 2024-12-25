# FastAPI Template

To install FastAPI, you need Python version 3.7 or higher.

## Create a virtual environment
```bash
python3 -m venv <venv_name>  # Replace <venv_name> with any name you want

Activate the virtual environment
	•	Linux/Mac:

source venv/bin/activate


	•	Windows:

venv\Scripts\activate



Install the required packages

pip install -r requirements.txt

Run the FastAPI server

uvicorn app.main:app --reload

Once running, you can access the API documentation:
	•	Swagger UI: http://127.0.0.1:8000/docs

Connect the database
	1.	Create a .env file in the project root directory.
	2.	Add the following line to the file:
	•	If a password is required:

DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>


	•	If no password is required:

DATABASE_URL=postgresql://<username>@<host>:<port>/<database_name>
