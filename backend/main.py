"""
FastAPI backend for Vehicle Balance Viewer.
Exposes a mocked WheelsEye-style API for fetching vehicle balances.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Dict
from mock_data import VEHICLE_BALANCES, VEHICLE_BALANCES_PREVIOUS
from alert_logic import calculate_alerts, calculate_usage_summary

app = FastAPI(
    title="Vehicle Balance Viewer API",
    description="Mocked WheelsEye-style API for vehicle balance information",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint for API health check."""
    return {
        "message": "Vehicle Balance Viewer API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/vehicle/{vehicle_id}/balance")
async def get_vehicle_balance(vehicle_id: str) -> Dict:
    """
    Fetch all balances associated with a given vehicle.
    
    Args:
        vehicle_id: Vehicle registration number or unique vehicle ID (string)
    
    Returns:
        JSON response with vehicle balances including wallet, fuel, and prepaid amounts
    
    Raises:
        HTTPException: 404 if vehicle_id not found in mock data
    """
    # Check if vehicle exists in mock data
    if vehicle_id not in VEHICLE_BALANCES:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )
    
    # Retrieve balances for the vehicle
    current_balances = VEHICLE_BALANCES[vehicle_id]
    
    # Get previous balances (24 hours ago) for usage summary
    previous_balances = VEHICLE_BALANCES_PREVIOUS.get(vehicle_id)
    
    # Calculate alerts for low balances
    alerts = calculate_alerts(current_balances)
    
    # Calculate usage summary (change over last 24 hours)
    usage_summary = calculate_usage_summary(
        current_balances,
        previous_balances,
        period="last 24 hours"
    )
    
    # Construct response with ISO-8601 timestamp
    response = {
        "vehicle_id": vehicle_id,
        "balances": {
            "wallet": current_balances["wallet"],
            "fuel": current_balances["fuel"],
            "prepaid": current_balances["prepaid"]
        },
        "alerts": alerts,
        "usage_summary": usage_summary,
        "currency": "INR",
        "last_updated": datetime.utcnow().isoformat() + "Z"
    }
    
    return response


if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*50)
    print("🚀 Vehicle Balance Viewer API Server")
    print("="*50)
    print(f"✅ Server running on: http://localhost:8000")
    print(f"📚 API Docs: http://localhost:8000/docs")
    print("="*50 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)

