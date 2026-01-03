"""
Mock data for vehicle balances.
Stores in-memory vehicle balance information simulating a WheelsEye-style API.
Contains ~100 vehicles with varied balances.
"""

# In-memory storage for vehicle balances
VEHICLE_BALANCES = {
    # Delhi vehicles
    "DL01AB1234": {"wallet": 2450.75, "fuel": 1200.0, "prepaid": 800.0},
    "DL01CD5678": {"wallet": 3200.50, "fuel": 1800.25, "prepaid": 1200.0},
    "DL02EF9012": {"wallet": 1500.0, "fuel": 850.75, "prepaid": 500.0},
    "DL02GH3456": {"wallet": 4200.0, "fuel": 2500.0, "prepaid": 1800.0},
    "DL03IJ7890": {"wallet": 980.50, "fuel": 600.0, "prepaid": 350.0},
    "DL03KL2345": {"wallet": 5600.75, "fuel": 3200.0, "prepaid": 2400.0},
    "DL04MN6789": {"wallet": 2100.25, "fuel": 1100.50, "prepaid": 750.0},
    "DL04OP0123": {"wallet": 3800.0, "fuel": 2000.0, "prepaid": 1500.0},
    "DL05QR4567": {"wallet": 1250.0, "fuel": 700.25, "prepaid": 450.0},
    "DL05ST8901": {"wallet": 4900.50, "fuel": 2800.0, "prepaid": 2100.0},
    
    # Maharashtra vehicles
    "MH12XY5678": {"wallet": 1800.0, "fuel": 950.5, "prepaid": 400.0},
    "MH12AB1234": {"wallet": 3500.75, "fuel": 1900.0, "prepaid": 1300.0},
    "MH01CD7890": {"wallet": 2200.0, "fuel": 1200.50, "prepaid": 800.0},
    "MH01EF3456": {"wallet": 4100.25, "fuel": 2300.0, "prepaid": 1700.0},
    "MH02GH9012": {"wallet": 1600.0, "fuel": 900.75, "prepaid": 550.0},
    "MH02IJ5678": {"wallet": 5300.50, "fuel": 3000.0, "prepaid": 2200.0},
    "MH03KL2345": {"wallet": 1900.0, "fuel": 1050.0, "prepaid": 650.0},
    "MH03MN8901": {"wallet": 3700.75, "fuel": 2100.25, "prepaid": 1600.0},
    "MH04OP4567": {"wallet": 1400.0, "fuel": 800.50, "prepaid": 500.0},
    "MH04QR0123": {"wallet": 4600.0, "fuel": 2600.0, "prepaid": 1900.0},
    
    # Karnataka vehicles
    "KA03CD9012": {"wallet": 3200.25, "fuel": 2100.0, "prepaid": 1500.0},
    "KA03AB5678": {"wallet": 2800.0, "fuel": 1600.75, "prepaid": 1100.0},
    "KA01EF2345": {"wallet": 3900.50, "fuel": 2200.0, "prepaid": 1700.0},
    "KA01GH8901": {"wallet": 1700.0, "fuel": 950.25, "prepaid": 600.0},
    "KA02IJ4567": {"wallet": 4400.75, "fuel": 2500.0, "prepaid": 2000.0},
    "KA02KL0123": {"wallet": 2100.0, "fuel": 1150.50, "prepaid": 750.0},
    "KA04MN7890": {"wallet": 3600.0, "fuel": 2000.25, "prepaid": 1500.0},
    "KA04OP3456": {"wallet": 1300.0, "fuel": 750.0, "prepaid": 450.0},
    "KA05QR9012": {"wallet": 5100.50, "fuel": 2900.0, "prepaid": 2300.0},
    "KA05ST5678": {"wallet": 2400.0, "fuel": 1300.75, "prepaid": 900.0},
    
    # Tamil Nadu vehicles
    "TN09EF3456": {"wallet": 950.0, "fuel": 650.75, "prepaid": 300.0},
    "TN09AB7890": {"wallet": 2700.25, "fuel": 1500.0, "prepaid": 1000.0},
    "TN01CD2345": {"wallet": 4000.0, "fuel": 2300.50, "prepaid": 1800.0},
    "TN01GH8901": {"wallet": 1500.0, "fuel": 850.0, "prepaid": 500.0},
    "TN02IJ4567": {"wallet": 3300.75, "fuel": 1900.0, "prepaid": 1400.0},
    "TN02KL0123": {"wallet": 1100.0, "fuel": 600.25, "prepaid": 400.0},
    "TN03MN7890": {"wallet": 4700.50, "fuel": 2700.0, "prepaid": 2100.0},
    "TN03OP3456": {"wallet": 2000.0, "fuel": 1100.75, "prepaid": 700.0},
    "TN04QR9012": {"wallet": 3800.0, "fuel": 2200.0, "prepaid": 1600.0},
    "TN04ST5678": {"wallet": 1200.0, "fuel": 700.50, "prepaid": 450.0},
    
    # Gujarat vehicles
    "GJ01AB1234": {"wallet": 2900.75, "fuel": 1650.0, "prepaid": 1150.0},
    "GJ01CD5678": {"wallet": 4300.0, "fuel": 2400.25, "prepaid": 1900.0},
    "GJ02EF9012": {"wallet": 1800.0, "fuel": 1000.50, "prepaid": 650.0},
    "GJ02GH3456": {"wallet": 5200.75, "fuel": 3000.0, "prepaid": 2400.0},
    "GJ03IJ7890": {"wallet": 1600.0, "fuel": 900.0, "prepaid": 550.0},
    "GJ03KL2345": {"wallet": 3600.25, "fuel": 2000.75, "prepaid": 1500.0},
    "GJ04MN6789": {"wallet": 2200.0, "fuel": 1200.0, "prepaid": 800.0},
    "GJ04OP0123": {"wallet": 4800.50, "fuel": 2800.0, "prepaid": 2200.0},
    "GJ05QR4567": {"wallet": 1400.0, "fuel": 800.25, "prepaid": 500.0},
    "GJ05ST8901": {"wallet": 3400.0, "fuel": 1900.50, "prepaid": 1400.0},
    
    # Uttar Pradesh vehicles
    "UP14AB1234": {"wallet": 3100.75, "fuel": 1750.0, "prepaid": 1200.0},
    "UP14CD5678": {"wallet": 4500.0, "fuel": 2600.25, "prepaid": 2000.0},
    "UP15EF9012": {"wallet": 1900.0, "fuel": 1050.50, "prepaid": 700.0},
    "UP15GH3456": {"wallet": 5400.75, "fuel": 3100.0, "prepaid": 2500.0},
    "UP16IJ7890": {"wallet": 1700.0, "fuel": 950.0, "prepaid": 600.0},
    "UP16KL2345": {"wallet": 3700.25, "fuel": 2100.75, "prepaid": 1600.0},
    "UP17MN6789": {"wallet": 2300.0, "fuel": 1300.0, "prepaid": 850.0},
    "UP17OP0123": {"wallet": 4900.50, "fuel": 2900.0, "prepaid": 2300.0},
    "UP18QR4567": {"wallet": 1500.0, "fuel": 850.25, "prepaid": 550.0},
    "UP18ST8901": {"wallet": 3500.0, "fuel": 2000.50, "prepaid": 1500.0},
    
    # West Bengal vehicles
    "WB01AB1234": {"wallet": 2800.75, "fuel": 1600.0, "prepaid": 1100.0},
    "WB01CD5678": {"wallet": 4200.0, "fuel": 2400.25, "prepaid": 1800.0},
    "WB02EF9012": {"wallet": 2000.0, "fuel": 1100.50, "prepaid": 750.0},
    "WB02GH3456": {"wallet": 5100.75, "fuel": 2900.0, "prepaid": 2300.0},
    "WB03IJ7890": {"wallet": 1800.0, "fuel": 1000.0, "prepaid": 650.0},
    "WB03KL2345": {"wallet": 3800.25, "fuel": 2200.75, "prepaid": 1700.0},
    "WB04MN6789": {"wallet": 2400.0, "fuel": 1350.0, "prepaid": 900.0},
    "WB04OP0123": {"wallet": 5000.50, "fuel": 3000.0, "prepaid": 2400.0},
    "WB05QR4567": {"wallet": 1600.0, "fuel": 900.25, "prepaid": 600.0},
    "WB05ST8901": {"wallet": 3600.0, "fuel": 2100.50, "prepaid": 1600.0},
    
    # Rajasthan vehicles
    "RJ01AB1234": {"wallet": 3000.75, "fuel": 1700.0, "prepaid": 1250.0},
    "RJ01CD5678": {"wallet": 4400.0, "fuel": 2500.25, "prepaid": 1950.0},
    "RJ02EF9012": {"wallet": 2100.0, "fuel": 1150.50, "prepaid": 800.0},
    "RJ02GH3456": {"wallet": 5300.75, "fuel": 3000.0, "prepaid": 2450.0},
    "RJ03IJ7890": {"wallet": 1900.0, "fuel": 1050.0, "prepaid": 700.0},
    "RJ03KL2345": {"wallet": 3900.25, "fuel": 2300.75, "prepaid": 1800.0},
    "RJ04MN6789": {"wallet": 2500.0, "fuel": 1400.0, "prepaid": 950.0},
    "RJ04OP0123": {"wallet": 5100.50, "fuel": 3100.0, "prepaid": 2500.0},
    "RJ05QR4567": {"wallet": 1700.0, "fuel": 950.25, "prepaid": 650.0},
    "RJ05ST8901": {"wallet": 3700.0, "fuel": 2200.50, "prepaid": 1700.0},
    
    # Andhra Pradesh vehicles
    "AP01AB1234": {"wallet": 2700.75, "fuel": 1550.0, "prepaid": 1050.0},
    "AP01CD5678": {"wallet": 4100.0, "fuel": 2350.25, "prepaid": 1750.0},
    "AP02EF9012": {"wallet": 2200.0, "fuel": 1200.50, "prepaid": 800.0},
    "AP02GH3456": {"wallet": 5200.75, "fuel": 2950.0, "prepaid": 2350.0},
    "AP03IJ7890": {"wallet": 2000.0, "fuel": 1100.0, "prepaid": 750.0},
    "AP03KL2345": {"wallet": 4000.25, "fuel": 2250.75, "prepaid": 1750.0},
    "AP04MN6789": {"wallet": 2600.0, "fuel": 1450.0, "prepaid": 1000.0},
    "AP04OP0123": {"wallet": 5000.50, "fuel": 2850.0, "prepaid": 2250.0},
    "AP05QR4567": {"wallet": 1800.0, "fuel": 1000.25, "prepaid": 700.0},
    "AP05ST8901": {"wallet": 3800.0, "fuel": 2150.50, "prepaid": 1650.0},
    
    # Telangana vehicles
    "TS01AB1234": {"wallet": 2900.75, "fuel": 1650.0, "prepaid": 1150.0},
    "TS01CD5678": {"wallet": 4300.0, "fuel": 2450.25, "prepaid": 1900.0},
    "TS02EF9012": {"wallet": 2300.0, "fuel": 1300.50, "prepaid": 850.0},
    "TS02GH3456": {"wallet": 5400.75, "fuel": 3050.0, "prepaid": 2450.0},
    "TS03IJ7890": {"wallet": 2100.0, "fuel": 1150.0, "prepaid": 800.0},
    "TS03KL2345": {"wallet": 4100.25, "fuel": 2350.75, "prepaid": 1850.0},
    "TS04MN6789": {"wallet": 2700.0, "fuel": 1500.0, "prepaid": 1100.0},
    "TS04OP0123": {"wallet": 5100.50, "fuel": 2950.0, "prepaid": 2350.0},
    "TS05QR4567": {"wallet": 1900.0, "fuel": 1050.25, "prepaid": 750.0},
    "TS05ST8901": {"wallet": 3900.0, "fuel": 2250.50, "prepaid": 1750.0},
    
    # Kerala vehicles
    "KL01AB1234": {"wallet": 2600.75, "fuel": 1500.0, "prepaid": 1000.0},
    "KL01CD5678": {"wallet": 4000.0, "fuel": 2300.25, "prepaid": 1700.0},
    "KL02EF9012": {"wallet": 2400.0, "fuel": 1350.50, "prepaid": 900.0},
    "KL02GH3456": {"wallet": 5300.75, "fuel": 3000.0, "prepaid": 2400.0},
    "KL03IJ7890": {"wallet": 2200.0, "fuel": 1200.0, "prepaid": 850.0},
    "KL03KL2345": {"wallet": 4200.25, "fuel": 2400.75, "prepaid": 1900.0},
    "KL04MN6789": {"wallet": 2800.0, "fuel": 1600.0, "prepaid": 1150.0},
    "KL04OP0123": {"wallet": 5200.50, "fuel": 3000.0, "prepaid": 2400.0},
    "KL05QR4567": {"wallet": 2000.0, "fuel": 1100.25, "prepaid": 800.0},
    "KL05ST8901": {"wallet": 4000.0, "fuel": 2300.50, "prepaid": 1800.0},
    
    # Madhya Pradesh vehicles
    "MP01AB1234": {"wallet": 3100.75, "fuel": 1750.0, "prepaid": 1250.0},
    "MP01CD5678": {"wallet": 4500.0, "fuel": 2600.25, "prepaid": 2000.0},
    "MP02EF9012": {"wallet": 2500.0, "fuel": 1400.50, "prepaid": 950.0},
    "MP02GH3456": {"wallet": 5500.75, "fuel": 3150.0, "prepaid": 2550.0},
    "MP03IJ7890": {"wallet": 2300.0, "fuel": 1300.0, "prepaid": 900.0},
    "MP03KL2345": {"wallet": 4300.25, "fuel": 2450.75, "prepaid": 1950.0},
    "MP04MN6789": {"wallet": 2900.0, "fuel": 1650.0, "prepaid": 1200.0},
    "MP04OP0123": {"wallet": 5300.50, "fuel": 3050.0, "prepaid": 2450.0},
    "MP05QR4567": {"wallet": 2100.0, "fuel": 1200.25, "prepaid": 850.0},
    "MP05ST8901": {"wallet": 4100.0, "fuel": 2350.50, "prepaid": 1850.0},
    
    # Punjab vehicles
    "PB01AB1234": {"wallet": 2800.75, "fuel": 1600.0, "prepaid": 1100.0},
    "PB01CD5678": {"wallet": 4200.0, "fuel": 2400.25, "prepaid": 1800.0},
    "PB02EF9012": {"wallet": 2600.0, "fuel": 1450.50, "prepaid": 1000.0},
    "PB02GH3456": {"wallet": 5400.75, "fuel": 3100.0, "prepaid": 2500.0},
    "PB03IJ7890": {"wallet": 2400.0, "fuel": 1350.0, "prepaid": 950.0},
    "PB03KL2345": {"wallet": 4400.25, "fuel": 2500.75, "prepaid": 2000.0},
    "PB04MN6789": {"wallet": 3000.0, "fuel": 1700.0, "prepaid": 1250.0},
    "PB04OP0123": {"wallet": 5200.50, "fuel": 3000.0, "prepaid": 2400.0},
    "PB05QR4567": {"wallet": 2200.0, "fuel": 1250.25, "prepaid": 900.0},
    "PB05ST8901": {"wallet": 4200.0, "fuel": 2400.50, "prepaid": 1900.0},
    
    # Haryana vehicles
    "HR01AB1234": {"wallet": 3000.75, "fuel": 1700.0, "prepaid": 1250.0},
    "HR01CD5678": {"wallet": 4400.0, "fuel": 2500.25, "prepaid": 1950.0},
    "HR02EF9012": {"wallet": 2700.0, "fuel": 1500.50, "prepaid": 1050.0},
    "HR02GH3456": {"wallet": 5500.75, "fuel": 3150.0, "prepaid": 2550.0},
    "HR03IJ7890": {"wallet": 2500.0, "fuel": 1400.0, "prepaid": 1000.0},
    "HR03KL2345": {"wallet": 4500.25, "fuel": 2600.75, "prepaid": 2100.0},
    "HR04MN6789": {"wallet": 3100.0, "fuel": 1750.0, "prepaid": 1300.0},
    "HR04OP0123": {"wallet": 5300.50, "fuel": 3050.0, "prepaid": 2450.0},
    "HR05QR4567": {"wallet": 2300.0, "fuel": 1300.25, "prepaid": 950.0},
    "HR05ST8901": {"wallet": 4300.0, "fuel": 2450.50, "prepaid": 1950.0},
}

# Previous balance snapshots (24 hours ago) for usage summary calculation
# Some vehicles show decreasing balances (usage), some increasing (top-ups), some stable
VEHICLE_BALANCES_PREVIOUS = {
    # Delhi vehicles - mix of decreasing and stable
    "DL01AB1234": {"wallet": 2900.75, "fuel": 1400.0, "prepaid": 800.0},  # wallet decreased
    "DL01CD5678": {"wallet": 3200.50, "fuel": 1800.25, "prepaid": 1200.0},  # stable
    "DL02EF9012": {"wallet": 1500.0, "fuel": 850.75, "prepaid": 500.0},  # stable
    "DL02GH3456": {"wallet": 4200.0, "fuel": 2500.0, "prepaid": 1800.0},  # stable
    "DL03IJ7890": {"wallet": 1200.50, "fuel": 750.0, "prepaid": 400.0},  # all decreased
    "DL03KL2345": {"wallet": 5600.75, "fuel": 3200.0, "prepaid": 2400.0},  # stable
    "DL04MN6789": {"wallet": 2100.25, "fuel": 1100.50, "prepaid": 750.0},  # stable
    "DL04OP0123": {"wallet": 3800.0, "fuel": 2000.0, "prepaid": 1500.0},  # stable
    "DL05QR4567": {"wallet": 1500.0, "fuel": 850.25, "prepaid": 500.0},  # all decreased
    "DL05ST8901": {"wallet": 4900.50, "fuel": 2800.0, "prepaid": 2100.0},  # stable
    
    # Maharashtra vehicles
    "MH12XY5678": {"wallet": 2000.0, "fuel": 1100.5, "prepaid": 450.0},  # all decreased
    "MH12AB1234": {"wallet": 3500.75, "fuel": 1900.0, "prepaid": 1300.0},  # stable
    "MH01CD7890": {"wallet": 2200.0, "fuel": 1200.50, "prepaid": 800.0},  # stable
    "MH01EF3456": {"wallet": 4100.25, "fuel": 2300.0, "prepaid": 1700.0},  # stable
    "MH02GH9012": {"wallet": 1800.0, "fuel": 1000.75, "prepaid": 600.0},  # all decreased
    "MH02IJ5678": {"wallet": 5300.50, "fuel": 3000.0, "prepaid": 2200.0},  # stable
    "MH03KL2345": {"wallet": 1900.0, "fuel": 1050.0, "prepaid": 650.0},  # stable
    "MH03MN8901": {"wallet": 3700.75, "fuel": 2100.25, "prepaid": 1600.0},  # stable
    "MH04OP4567": {"wallet": 1600.0, "fuel": 900.50, "prepaid": 550.0},  # all decreased
    "MH04QR0123": {"wallet": 4600.0, "fuel": 2600.0, "prepaid": 1900.0},  # stable
    
    # Karnataka vehicles
    "KA03CD9012": {"wallet": 3200.25, "fuel": 2100.0, "prepaid": 1500.0},  # stable
    "KA03AB5678": {"wallet": 3000.0, "fuel": 1700.75, "prepaid": 1200.0},  # all decreased
    "KA01EF2345": {"wallet": 3900.50, "fuel": 2200.0, "prepaid": 1700.0},  # stable
    "KA01GH8901": {"wallet": 1900.0, "fuel": 1050.25, "prepaid": 650.0},  # all decreased
    "KA02IJ4567": {"wallet": 4400.75, "fuel": 2500.0, "prepaid": 2000.0},  # stable
    "KA02KL0123": {"wallet": 2100.0, "fuel": 1150.50, "prepaid": 750.0},  # stable
    "KA04MN7890": {"wallet": 3600.0, "fuel": 2000.25, "prepaid": 1500.0},  # stable
    "KA04OP3456": {"wallet": 1500.0, "fuel": 850.0, "prepaid": 500.0},  # all decreased
    "KA05QR9012": {"wallet": 5100.50, "fuel": 2900.0, "prepaid": 2300.0},  # stable
    "KA05ST5678": {"wallet": 2400.0, "fuel": 1300.75, "prepaid": 900.0},  # stable
    
    # Tamil Nadu vehicles
    "TN09EF3456": {"wallet": 1100.0, "fuel": 750.75, "prepaid": 350.0},  # all decreased
    "TN09AB7890": {"wallet": 2700.25, "fuel": 1500.0, "prepaid": 1000.0},  # stable
    "TN01CD2345": {"wallet": 4000.0, "fuel": 2300.50, "prepaid": 1800.0},  # stable
    "TN01GH8901": {"wallet": 1700.0, "fuel": 950.0, "prepaid": 550.0},  # all decreased
    "TN02IJ4567": {"wallet": 3300.75, "fuel": 1900.0, "prepaid": 1400.0},  # stable
    "TN02KL0123": {"wallet": 1300.0, "fuel": 700.25, "prepaid": 450.0},  # all decreased
    "TN03MN7890": {"wallet": 4700.50, "fuel": 2700.0, "prepaid": 2100.0},  # stable
    "TN03OP3456": {"wallet": 2000.0, "fuel": 1100.75, "prepaid": 700.0},  # stable
    "TN04QR9012": {"wallet": 3800.0, "fuel": 2200.0, "prepaid": 1600.0},  # stable
    "TN04ST5678": {"wallet": 1400.0, "fuel": 800.50, "prepaid": 500.0},  # all decreased
    
    # Gujarat vehicles
    "GJ01AB1234": {"wallet": 2900.75, "fuel": 1650.0, "prepaid": 1150.0},  # stable
    "GJ01CD5678": {"wallet": 4300.0, "fuel": 2400.25, "prepaid": 1900.0},  # stable
    "GJ02EF9012": {"wallet": 2000.0, "fuel": 1100.50, "prepaid": 700.0},  # all decreased
    "GJ02GH3456": {"wallet": 5200.75, "fuel": 3000.0, "prepaid": 2400.0},  # stable
    "GJ03IJ7890": {"wallet": 1800.0, "fuel": 1000.0, "prepaid": 600.0},  # all decreased
    "GJ03KL2345": {"wallet": 3600.25, "fuel": 2000.75, "prepaid": 1500.0},  # stable
    "GJ04MN6789": {"wallet": 2200.0, "fuel": 1200.0, "prepaid": 800.0},  # stable
    "GJ04OP0123": {"wallet": 4800.50, "fuel": 2800.0, "prepaid": 2200.0},  # stable
    "GJ05QR4567": {"wallet": 1600.0, "fuel": 900.25, "prepaid": 550.0},  # all decreased
    "GJ05ST8901": {"wallet": 3400.0, "fuel": 1900.50, "prepaid": 1400.0},  # stable
    
    # Uttar Pradesh vehicles
    "UP14AB1234": {"wallet": 3100.75, "fuel": 1750.0, "prepaid": 1200.0},  # stable
    "UP14CD5678": {"wallet": 4500.0, "fuel": 2600.25, "prepaid": 2000.0},  # stable
    "UP15EF9012": {"wallet": 2100.0, "fuel": 1150.50, "prepaid": 750.0},  # all decreased
    "UP15GH3456": {"wallet": 5400.75, "fuel": 3100.0, "prepaid": 2500.0},  # stable
    "UP16IJ7890": {"wallet": 1900.0, "fuel": 1050.0, "prepaid": 650.0},  # all decreased
    "UP16KL2345": {"wallet": 3700.25, "fuel": 2100.75, "prepaid": 1600.0},  # stable
    "UP17MN6789": {"wallet": 2300.0, "fuel": 1300.0, "prepaid": 850.0},  # stable
    "UP17OP0123": {"wallet": 4900.50, "fuel": 2900.0, "prepaid": 2300.0},  # stable
    "UP18QR4567": {"wallet": 1700.0, "fuel": 950.25, "prepaid": 600.0},  # all decreased
    "UP18ST8901": {"wallet": 3500.0, "fuel": 2000.50, "prepaid": 1500.0},  # stable
    
    # West Bengal vehicles
    "WB01AB1234": {"wallet": 2800.75, "fuel": 1600.0, "prepaid": 1100.0},  # stable
    "WB01CD5678": {"wallet": 4200.0, "fuel": 2400.25, "prepaid": 1800.0},  # stable
    "WB02EF9012": {"wallet": 2200.0, "fuel": 1200.50, "prepaid": 800.0},  # all decreased
    "WB02GH3456": {"wallet": 5100.75, "fuel": 2900.0, "prepaid": 2300.0},  # stable
    "WB03IJ7890": {"wallet": 2000.0, "fuel": 1100.0, "prepaid": 700.0},  # all decreased
    "WB03KL2345": {"wallet": 3800.25, "fuel": 2200.75, "prepaid": 1700.0},  # stable
    "WB04MN6789": {"wallet": 2400.0, "fuel": 1350.0, "prepaid": 900.0},  # stable
    "WB04OP0123": {"wallet": 5000.50, "fuel": 3000.0, "prepaid": 2400.0},  # stable
    "WB05QR4567": {"wallet": 1800.0, "fuel": 1000.25, "prepaid": 650.0},  # all decreased
    "WB05ST8901": {"wallet": 3600.0, "fuel": 2100.50, "prepaid": 1600.0},  # stable
    
    # Rajasthan vehicles
    "RJ01AB1234": {"wallet": 3000.75, "fuel": 1700.0, "prepaid": 1250.0},  # stable
    "RJ01CD5678": {"wallet": 4400.0, "fuel": 2500.25, "prepaid": 1950.0},  # stable
    "RJ02EF9012": {"wallet": 2300.0, "fuel": 1250.50, "prepaid": 850.0},  # all decreased
    "RJ02GH3456": {"wallet": 5300.75, "fuel": 3000.0, "prepaid": 2450.0},  # stable
    "RJ03IJ7890": {"wallet": 2100.0, "fuel": 1150.0, "prepaid": 750.0},  # all decreased
    "RJ03KL2345": {"wallet": 3900.25, "fuel": 2300.75, "prepaid": 1800.0},  # stable
    "RJ04MN6789": {"wallet": 2500.0, "fuel": 1400.0, "prepaid": 950.0},  # stable
    "RJ04OP0123": {"wallet": 5100.50, "fuel": 3100.0, "prepaid": 2500.0},  # stable
    "RJ05QR4567": {"wallet": 1900.0, "fuel": 1050.25, "prepaid": 700.0},  # all decreased
    "RJ05ST8901": {"wallet": 3700.0, "fuel": 2200.50, "prepaid": 1700.0},  # stable
    
    # Andhra Pradesh vehicles
    "AP01AB1234": {"wallet": 2700.75, "fuel": 1550.0, "prepaid": 1050.0},  # stable
    "AP01CD5678": {"wallet": 4100.0, "fuel": 2350.25, "prepaid": 1750.0},  # stable
    "AP02EF9012": {"wallet": 2400.0, "fuel": 1300.50, "prepaid": 850.0},  # all decreased
    "AP02GH3456": {"wallet": 5200.75, "fuel": 2950.0, "prepaid": 2350.0},  # stable
    "AP03IJ7890": {"wallet": 2200.0, "fuel": 1200.0, "prepaid": 800.0},  # all decreased
    "AP03KL2345": {"wallet": 4000.25, "fuel": 2250.75, "prepaid": 1750.0},  # stable
    "AP04MN6789": {"wallet": 2600.0, "fuel": 1450.0, "prepaid": 1000.0},  # stable
    "AP04OP0123": {"wallet": 5000.50, "fuel": 2850.0, "prepaid": 2250.0},  # stable
    "AP05QR4567": {"wallet": 2000.0, "fuel": 1100.25, "prepaid": 750.0},  # all decreased
    "AP05ST8901": {"wallet": 3800.0, "fuel": 2150.50, "prepaid": 1650.0},  # stable
    
    # Telangana vehicles
    "TS01AB1234": {"wallet": 2900.75, "fuel": 1650.0, "prepaid": 1150.0},  # stable
    "TS01CD5678": {"wallet": 4300.0, "fuel": 2450.25, "prepaid": 1900.0},  # stable
    "TS02EF9012": {"wallet": 2500.0, "fuel": 1400.50, "prepaid": 900.0},  # all decreased
    "TS02GH3456": {"wallet": 5400.75, "fuel": 3050.0, "prepaid": 2450.0},  # stable
    "TS03IJ7890": {"wallet": 2300.0, "fuel": 1250.0, "prepaid": 850.0},  # all decreased
    "TS03KL2345": {"wallet": 4100.25, "fuel": 2350.75, "prepaid": 1850.0},  # stable
    "TS04MN6789": {"wallet": 2700.0, "fuel": 1500.0, "prepaid": 1100.0},  # stable
    "TS04OP0123": {"wallet": 5100.50, "fuel": 2950.0, "prepaid": 2350.0},  # stable
    "TS05QR4567": {"wallet": 2100.0, "fuel": 1150.25, "prepaid": 800.0},  # all decreased
    "TS05ST8901": {"wallet": 3900.0, "fuel": 2250.50, "prepaid": 1750.0},  # stable
    
    # Kerala vehicles
    "KL01AB1234": {"wallet": 2600.75, "fuel": 1500.0, "prepaid": 1000.0},  # stable
    "KL01CD5678": {"wallet": 4000.0, "fuel": 2300.25, "prepaid": 1700.0},  # stable
    "KL02EF9012": {"wallet": 2600.0, "fuel": 1450.50, "prepaid": 900.0},  # stable
    "KL02GH3456": {"wallet": 5300.75, "fuel": 3000.0, "prepaid": 2400.0},  # stable
    "KL03IJ7890": {"wallet": 2400.0, "fuel": 1300.0, "prepaid": 900.0},  # all decreased
    "KL03KL2345": {"wallet": 4200.25, "fuel": 2400.75, "prepaid": 1900.0},  # stable
    "KL04MN6789": {"wallet": 2800.0, "fuel": 1600.0, "prepaid": 1150.0},  # stable
    "KL04OP0123": {"wallet": 5200.50, "fuel": 3000.0, "prepaid": 2400.0},  # stable
    "KL05QR4567": {"wallet": 2200.0, "fuel": 1200.25, "prepaid": 850.0},  # all decreased
    "KL05ST8901": {"wallet": 4000.0, "fuel": 2300.50, "prepaid": 1800.0},  # stable
    
    # Madhya Pradesh vehicles
    "MP01AB1234": {"wallet": 3100.75, "fuel": 1750.0, "prepaid": 1250.0},  # stable
    "MP01CD5678": {"wallet": 4500.0, "fuel": 2600.25, "prepaid": 2000.0},  # stable
    "MP02EF9012": {"wallet": 2700.0, "fuel": 1500.50, "prepaid": 1000.0},  # all decreased
    "MP02GH3456": {"wallet": 5500.75, "fuel": 3150.0, "prepaid": 2550.0},  # stable
    "MP03IJ7890": {"wallet": 2500.0, "fuel": 1400.0, "prepaid": 950.0},  # all decreased
    "MP03KL2345": {"wallet": 4300.25, "fuel": 2450.75, "prepaid": 1950.0},  # stable
    "MP04MN6789": {"wallet": 2900.0, "fuel": 1650.0, "prepaid": 1200.0},  # stable
    "MP04OP0123": {"wallet": 5300.50, "fuel": 3050.0, "prepaid": 2450.0},  # stable
    "MP05QR4567": {"wallet": 2300.0, "fuel": 1300.25, "prepaid": 900.0},  # all decreased
    "MP05ST8901": {"wallet": 4100.0, "fuel": 2350.50, "prepaid": 1850.0},  # stable
    
    # Punjab vehicles
    "PB01AB1234": {"wallet": 2800.75, "fuel": 1600.0, "prepaid": 1100.0},  # stable
    "PB01CD5678": {"wallet": 4200.0, "fuel": 2400.25, "prepaid": 1800.0},  # stable
    "PB02EF9012": {"wallet": 2800.0, "fuel": 1550.50, "prepaid": 1050.0},  # all decreased
    "PB02GH3456": {"wallet": 5400.75, "fuel": 3100.0, "prepaid": 2500.0},  # stable
    "PB03IJ7890": {"wallet": 2600.0, "fuel": 1450.0, "prepaid": 1000.0},  # all decreased
    "PB03KL2345": {"wallet": 4400.25, "fuel": 2500.75, "prepaid": 2000.0},  # stable
    "PB04MN6789": {"wallet": 3000.0, "fuel": 1700.0, "prepaid": 1250.0},  # stable
    "PB04OP0123": {"wallet": 5200.50, "fuel": 3000.0, "prepaid": 2400.0},  # stable
    "PB05QR4567": {"wallet": 2400.0, "fuel": 1350.25, "prepaid": 950.0},  # all decreased
    "PB05ST8901": {"wallet": 4200.0, "fuel": 2400.50, "prepaid": 1900.0},  # stable
    
    # Haryana vehicles
    "HR01AB1234": {"wallet": 3000.75, "fuel": 1700.0, "prepaid": 1250.0},  # stable
    "HR01CD5678": {"wallet": 4400.0, "fuel": 2500.25, "prepaid": 1950.0},  # stable
    "HR02EF9012": {"wallet": 2900.0, "fuel": 1600.50, "prepaid": 1100.0},  # all decreased
    "HR02GH3456": {"wallet": 5500.75, "fuel": 3150.0, "prepaid": 2550.0},  # stable
    "HR03IJ7890": {"wallet": 2700.0, "fuel": 1500.0, "prepaid": 1050.0},  # all decreased
    "HR03KL2345": {"wallet": 4500.25, "fuel": 2600.75, "prepaid": 2100.0},  # stable
    "HR04MN6789": {"wallet": 3100.0, "fuel": 1750.0, "prepaid": 1300.0},  # stable
    "HR04OP0123": {"wallet": 5300.50, "fuel": 3050.0, "prepaid": 2450.0},  # stable
    "HR05QR4567": {"wallet": 2500.0, "fuel": 1400.25, "prepaid": 1000.0},  # all decreased
    "HR05ST8901": {"wallet": 4300.0, "fuel": 2450.50, "prepaid": 1950.0},  # stable
}
