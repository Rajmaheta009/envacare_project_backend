# Envacare Project Backend Help

## How to Run the Project

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd envacare_project_backend
   ```

2. **Create and activate a Python virtual environment (recommended)**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**
   ```sh
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**
   Create a file named `.env` in the project root with the following example content:
   ```env
   DATABASE_URL=sqlite:///./test.db  # Or your actual database URL
   SECRET_KEY=your_secret_key
   DEBUG=True
   # Add other environment variables as needed
   ```

5. **Run the backend server**
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   Or use Docker:
   ```sh
   docker build -t envacare-backend .
   docker run -p 8000:8000 envacare-backend
   ```

6. **Access the API**
   - Open your browser and go to: [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation.

## Notes
- Static files are served from the `/static` endpoint.
- Make sure your database is accessible and configured correctly in the `.env` file.
- CORS is enabled for all origins by default.

---
For more details, see the code in `main.py` and related modules in the `api/`, `model/`, and `Schema/` directories.
