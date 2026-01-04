# Vehicle Balance Viewer (Mocked WheelsEye API)

**Version:** 1.0.0

A full-stack application demonstrating API design clarity and clean Python backend implementation using a mocked WheelsEye-style service for viewing vehicle balances.

## Project Overview

This project provides a simple way to view all balances associated with a vehicle. Since real API access is not provided, the system simulates a WheelsEye-like backend and exposes clean, predictable REST APIs for frontend consumption.

### Goals

- ✅ Mock a real-world vehicle balance API
- ✅ Expose a clean REST endpoint
- ✅ Consume the API from a frontend
- ✅ Handle happy and failure paths gracefully

### Non-Goals

- ❌ No real WheelsEye API integration
- ❌ No authentication or authorization
- ❌ No database persistence
- ❌ No production deployment

## Tech Stack

### Backend
- **Language:** Python >= 3.9
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Port:** 8000 (default)

### Frontend
- **Technology:** HTML5 + CSS3 + Vanilla JavaScript
- **No build tools required** - runs directly in the browser

## Project Structure

```
wheels/
├── backend/
│   ├── main.py              # FastAPI app and routes
│   ├── mock_data.py         # In-memory vehicle balance data (current + previous)
│   ├── alert_logic.py       # Alert calculation and usage summary logic
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html           # Main HTML page
│   ├── style.css            # Styling (including alerts and usage summary)
│   └── script.js            # API consumption logic
└── README.md                # This file
```

## API Endpoints

### GET `/vehicle/{vehicle_id}/balance`

Fetches all balances associated with a given vehicle, including actionable insights (alerts and usage summary).

**Path Parameters:**
- `vehicle_id` (string, required): Vehicle registration number or unique vehicle ID
  - Example: `DL01AB1234`

**Success Response (200 OK):**
```json
{
  "vehicle_id": "DL01AB1234",
  "balances": {
    "wallet": 2450.75,
    "fuel": 1200.0,
    "prepaid": 800.0
  },
  "alerts": [
    {
      "type": "fuel",
      "severity": "warning",
      "message": "Fuel balance is below the recommended minimum"
    }
  ],
  "usage_summary": {
    "wallet_change": -450.0,
    "fuel_change": -200.0,
    "prepaid_change": 0.0,
    "period": "last 24 hours"
  },
  "currency": "INR",
  "last_updated": "2024-01-15T10:30:45.123456Z"
}
```

**Response Fields:**
- `vehicle_id`: Vehicle registration number
- `balances`: Current wallet, fuel, and prepaid balances
- `alerts`: Array of low balance alerts (empty if no alerts)
- `usage_summary`: Balance changes over the last 24 hours
- `currency`: Currency code (INR)
- `last_updated`: ISO-8601 timestamp

**Error Response (404 Not Found):**
```json
{
  "detail": "Vehicle not found"
}
```

**Example Request:**
```bash
curl http://localhost:8000/vehicle/DL01AB1234/balance
```

### GET `/`

Health check endpoint.

**Response (200 OK):**
```json
{
  "message": "Vehicle Balance Viewer API",
  "version": "1.0.0",
  "status": "running"
}
```

## Mock Data Explanation

The backend uses in-memory Python dictionaries to store vehicle balance information. The mock data is defined in `backend/mock_data.py` and includes the following vehicles:

- `DL01AB1234` - Wallet: ₹2,450.75, Fuel: ₹1,200.00, Prepaid: ₹800.00
- `MH12XY5678` - Wallet: ₹1,800.00, Fuel: ₹950.50, Prepaid: ₹400.00
- `KA03CD9012` - Wallet: ₹3,200.25, Fuel: ₹2,100.00, Prepaid: ₹1,500.00
- `TN09EF3456` - Wallet: ₹950.00, Fuel: ₹650.75, Prepaid: ₹300.00

**Note:** All balances are stored in INR (Indian Rupees) and are reset to these default values on each server restart since data is stored in-memory only.

## Actionable Vehicle Balance Insights

The API now includes two powerful features that help users understand when to act and track balance usage trends:

### 1. Low Balance Alerts

**Business Value:** Helps fleet users immediately know when any balance is critically low and requires action.

**How It Works:**
- The system monitors each balance type against predefined thresholds:
  - **Wallet:** ₹1,000 minimum
  - **Fuel:** ₹800 minimum
  - **Prepaid:** ₹500 minimum
- If any balance falls below its threshold, an alert is generated
- Alerts are displayed prominently in the frontend with clear messaging

**Example Alert:**
```json
{
  "type": "fuel",
  "severity": "warning",
  "message": "Fuel balance is below the recommended minimum"
}
```

**Why This Adds Value:**
- **Proactive Management:** Users don't need to manually check if balances are sufficient
- **Prevents Service Interruption:** Early warning prevents running out of funds during operations
- **Actionable:** Clear indication of which balance type needs attention

### 2. Balance Usage Summary

**Business Value:** Provides quick insight into whether balances are increasing or decreasing over time.

**How It Works:**
- Compares current balances with previous snapshot (24 hours ago)
- Calculates the change (positive for increases, negative for decreases)
- Displays changes with color coding:
  - **Green:** Positive change (balance increased)
  - **Red:** Negative change (balance decreased)
  - **Gray:** No change

**Example Usage Summary:**
```json
{
  "wallet_change": -450.0,
  "fuel_change": -200.0,
  "prepaid_change": 0.0,
  "period": "last 24 hours"
}
```

**Why This Adds Value:**
- **Trend Visibility:** Users can quickly see if balances are trending up or down
- **Usage Patterns:** Helps identify which balance types are being used most
- **Budget Planning:** Understanding usage patterns helps with future budget allocation
- **Anomaly Detection:** Sudden large changes may indicate issues or unusual activity

**Implementation Details:**
- Previous balance snapshots are stored in-memory alongside current balances
- Some vehicles show decreasing balances (simulating usage), others show stable balances
- The comparison window is set to "last 24 hours" to provide recent, actionable insights

## How to Run Backend

### Prerequisites
- Python >= 3.9 installed
- pip (Python package manager)

### Steps

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server:**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Verify the server is running:**
   - The server will start on `http://localhost:8000`
   - Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)
   - Visit `http://localhost:8000/redoc` for alternative API documentation

### Backend Features

- **CORS enabled** - Allows frontend to make requests from any origin
- **Automatic API documentation** - Available at `/docs` endpoint
- **Error handling** - Returns proper HTTP status codes (404 for not found)
- **ISO-8601 timestamps** - All timestamps in UTC format

## How to Use Frontend

### Prerequisites
- Backend server running on `http://localhost:8000`
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Steps

1. **Ensure the backend is running** (see "How to Run Backend" above)

2. **Open the frontend:**
   - Simply open `frontend/index.html` in your web browser
   - Or use a local web server (recommended):
     ```bash
     # Using Python 3
     cd frontend
     python -m http.server 8080
     # Then visit http://localhost:8080
     
     # Using Node.js (if installed)
     npx http-server frontend -p 8080
     ```

3. **Use the application:**
   - Enter a vehicle ID (e.g., `DL01AB1234`) in the input field
   - Click "Fetch Balance" or press Enter
   - View the balances displayed in cards (Wallet, Fuel, Prepaid)
   - If the vehicle is not found, an error message will be displayed

### Frontend Features

- **Responsive design** - Works on desktop and mobile devices
- **Loading indicators** - Shows spinner during API calls
- **Error handling** - Displays user-friendly error messages
- **Currency formatting** - Properly formatted INR amounts
- **Date formatting** - Human-readable timestamps
- **Keyboard support** - Enter key triggers balance fetch

## Assumptions & Limitations

### Assumptions

1. **Vehicle Identifier:** Vehicle registration number or unique vehicle ID as string (e.g., `DL01AB1234`)
2. **Currency:** All balances are in INR (Indian Rupees)
3. **Balances Supported:**
   - Wallet balance
   - Fuel balance
   - Prepaid balance
4. **Time Format:** ISO-8601 timestamps in UTC (e.g., `2024-01-15T10:30:45.123456Z`)
5. **Network:** Frontend assumes backend is running on `http://localhost:8000`

### Limitations

1. **No Persistence:** All data is stored in-memory and is lost when the server restarts
2. **No Authentication:** The API has no authentication or authorization mechanisms
3. **Limited Mock Data:** Only 4 vehicles are available in the mock dataset
4. **No Validation:** Vehicle ID format is not strictly validated (accepts any string)
5. **CORS:** Currently allows all origins (not suitable for production)
6. **No Rate Limiting:** API has no rate limiting or throttling
7. **Single Currency:** Only INR is supported
8. **No History:** No historical balance tracking or audit logs

### Known Issues

- If the backend is not running, the frontend will show a network error message
- Vehicle IDs are case-sensitive in the mock data
- No input sanitization for XSS prevention (acceptable for demo purposes)

## Development Notes

### API Design Principles

- **RESTful naming:** Clear, resource-based endpoint paths
- **Stateless requests:** Each request contains all necessary information
- **Explicit HTTP status codes:** 200 for success, 404 for not found
- **Predictable JSON responses:** Consistent response structure

### Code Organization

- **Separation of concerns:** Routes in `main.py`, data in `mock_data.py`
- **Clear function naming:** Descriptive function and variable names
- **Error handling:** Graceful error handling with proper HTTP status codes
- **Documentation:** Inline comments and docstrings for clarity

## Testing the Application

### Manual Testing

1. **Test successful balance fetch:**
   - Enter `DL01AB1234` and click Fetch Balance
   - Should display all three balances

2. **Test vehicle not found:**
   - Enter `INVALID123` and click Fetch Balance
   - Should display "Vehicle not found" error

3. **Test empty input:**
   - Leave input empty and click Fetch Balance
   - Should display validation error

4. **Test network error:**
   - Stop the backend server
   - Try to fetch balance
   - Should display network error message

### API Testing with curl

```bash
# Test successful request
curl http://localhost:8000/vehicle/DL01AB1234/balance

# Test 404 error
curl http://localhost:8000/vehicle/INVALID123/balance

# Test health check
curl http://localhost:8000/
```

## Future Enhancements (Out of Scope)

If this were a production system, the following enhancements would be considered:

- Database persistence (PostgreSQL/MongoDB)
- Authentication and authorization (JWT tokens)
- Input validation and sanitization
- Rate limiting and API throttling
- Logging and monitoring
- Unit and integration tests
- Docker containerization
- CI/CD pipeline
- Real-time balance updates (WebSockets)
- Balance history and audit logs
- Multi-currency support
- Pagination for vehicle lists

## License

This is a demonstration project created for evaluation purposes.

## Author

Created as part of Round 1 assignment for WheelsEye.

