"""
Alert calculation logic for vehicle balance insights.
Pure functions for determining low balance alerts.
"""

from typing import List, Dict, Optional

# Balance thresholds for alerts
BALANCE_THRESHOLDS = {
    "wallet": 1000,
    "fuel": 800,
    "prepaid": 500
}


def calculate_alerts(balances: Dict[str, float]) -> List[Dict[str, str]]:
    """
    Calculate low balance alerts based on thresholds.
    
    Args:
        balances: Dictionary with wallet, fuel, and prepaid balances
    
    Returns:
        List of alert dictionaries, empty if no alerts
    """
    alerts = []
    
    # Check wallet balance
    if balances.get("wallet", 0) < BALANCE_THRESHOLDS["wallet"]:
        alerts.append({
            "type": "wallet",
            "severity": "warning",
            "message": "Wallet balance is below the recommended minimum"
        })
    
    # Check fuel balance
    if balances.get("fuel", 0) < BALANCE_THRESHOLDS["fuel"]:
        alerts.append({
            "type": "fuel",
            "severity": "warning",
            "message": "Fuel balance is below the recommended minimum"
        })
    
    # Check prepaid balance
    if balances.get("prepaid", 0) < BALANCE_THRESHOLDS["prepaid"]:
        alerts.append({
            "type": "prepaid",
            "severity": "warning",
            "message": "Prepaid balance is below the recommended minimum"
        })
    
    return alerts


def calculate_usage_summary(
    current_balances: Dict[str, float],
    previous_balances: Optional[Dict[str, float]],
    period: str = "last 24 hours"
) -> Dict[str, any]:
    """
    Calculate balance usage summary comparing current vs previous balances.
    
    Args:
        current_balances: Current balance dictionary
        previous_balances: Previous balance dictionary (24h ago) or None
        period: Time period description
    
    Returns:
        Dictionary with wallet_change, fuel_change, prepaid_change, and period
    """
    # If no previous balances, assume no change
    if previous_balances is None:
        previous_balances = current_balances.copy()
    
    wallet_change = current_balances.get("wallet", 0) - previous_balances.get("wallet", 0)
    fuel_change = current_balances.get("fuel", 0) - previous_balances.get("fuel", 0)
    prepaid_change = current_balances.get("prepaid", 0) - previous_balances.get("prepaid", 0)
    
    return {
        "wallet_change": round(wallet_change, 2),
        "fuel_change": round(fuel_change, 2),
        "prepaid_change": round(prepaid_change, 2),
        "period": period
    }

