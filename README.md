# KPA Form Data API

A FastAPI backend for managing Kisan Parivahan App (KPA) form data, specifically designed for railway maintenance and inspection forms.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/simran1002/FastAPI-Dev.git
   cd FastAPI-Dev
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   python -m app.main
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication
- **POST** `/api/auth/login` - User login with phone number and password

### Wheel Specifications
- **POST** `/api/forms/wheel-specifications` - Submit wheel specification form
- **GET** `/api/forms/wheel-specifications` - Retrieve wheel specifications with filters

### Bogie Checksheet
- **POST** `/api/forms/bogie-checksheet` - Submit bogie checksheet form

### Documentation
- **GET** `/docs` - Swagger UI documentation



## Development

### Running in Development Mode
```bash
python -m app.main
```

The server will automatically reload when files are changed.

### Testing
Use the provided Postman collection `KPA_form_data.postman_collection.json` to test all endpoints.
