# KPA Form Data API

A FastAPI backend for managing Kisan Parivahan App (KPA) form data, specifically designed for railway maintenance and inspection forms.

## Features

- **Wheel Specifications API** - Submit and retrieve wheel specification forms
- **Bogie Checksheet API** - Submit bogie inspection forms
- **Simple Authentication** - Basic login system with bearer tokens
- **PostgreSQL Database** - Robust data storage with async operations
- **Swagger Documentation** - Interactive API documentation

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip or poetry

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Assignment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/kpa_db
   SECRET_KEY=your-secret-key-here
   HOST=0.0.0.0
   PORT=8000
   DEBUG=true
   ```

4. **Run the server**
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
- **GET** `/redoc` - ReDoc documentation
- **GET** `/health` - Health check endpoint

## API Examples

### Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "7760873976",
    "password": "to_share@123"
  }'
```

### Submit Wheel Specification
```bash
curl -X POST "http://localhost:8000/api/forms/wheel-specifications" \
  -H "Content-Type: application/json" \
  -d '{
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "fields": {
      "treadDiameterNew": "915 (900-1000)",
      "lastShopIssueSize": "837 (800-900)",
      "condemningDia": "825 (800-900)",
      "wheelGauge": "1600 (+2,-1)"
    }
  }'
```

### Get Wheel Specifications
```bash
curl -X GET "http://localhost:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001"
```

## Database Schema

### Wheel Specifications
- `form_number` (Primary Key)
- `submitted_by`
- `submitted_date`
- `fields` (JSON)
- `status`
- `created_at`
- `updated_at`

### Bogie Checksheets
- `form_number` (Primary Key)
- `inspection_by`
- `inspection_date`
- `bogie_details` (JSON)
- `bogie_checksheet` (JSON)
- `bmbc_checksheet` (JSON)
- `status`
- `created_at`
- `updated_at`

## Project Structure

```
Assignment/
├── app/
│   ├── api/
│   │   ├── railway_auth.py      # Authentication endpoints
│   │   ├── railway_forms.py     # Form data endpoints
│   │   └── __init__.py
│   ├── core/
│   │   ├── auth.py              # Authentication utilities
│   │   └── __init__.py
│   ├── models/
│   │   ├── railway_forms.py     # Database models
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── railway_forms.py     # Pydantic schemas
│   │   └── __init__.py
│   ├── config.py                # Configuration settings
│   ├── database.py              # Database connection
│   └── main.py                  # FastAPI application
├── KPA_form_data.postman_collection.json
├── .gitignore
└── README.md
```

## Development

### Running in Development Mode
```bash
python -m app.main
```

The server will automatically reload when files are changed.

### Testing
Use the provided Postman collection `KPA_form_data.postman_collection.json` to test all endpoints.

## Production Deployment

1. Set `DEBUG=false` in environment variables
2. Configure proper CORS settings
3. Use a production-grade PostgreSQL instance
4. Set up proper logging and monitoring
5. Implement proper JWT authentication for production use

## License

MIT License - see LICENSE file for details.

## Support

For support and questions, please contact the development team. 