# FastAPI_template
To install FastAPI, you need Python version 3.7 or higher

Create a virtual env
```bash
$python3 -m venv <venv_name> // Replace <venv_name> with any name you want

Activate virtual env
- Linux/Mac
```bash
source venv/bin/activate

- Windows
```bash
venv\Scripts\activate

Install the required packages
```bash
pip install -r requirements.txt

Run the FastAPI server
```bash
uvicorn app.main:app --reload

Once running, you can access the API docs at:
- Swagger UI: http://127.0.0.1:8000/docs.
  
Connect database, create a .env file in the project root directory.

Add the line

- DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>

If no password is required

- DATABASE_URL=postgresql://<username>@<host>:<port>/<database_name>.
