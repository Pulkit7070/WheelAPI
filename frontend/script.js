/**
 * Vehicle Balance Viewer - Frontend Script
 * Consumes the mocked WheelsEye-style API to fetch and display vehicle balances.
 */

const API_BASE_URL = 'http://localhost:8000';

/**
 * Format currency amount in INR
 */
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(amount);
}

/**
 * Format ISO-8601 timestamp to readable date
 */
function formatDate(isoString) {
    const date = new Date(isoString);
    return date.toLocaleString('en-IN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        timeZoneName: 'short'
    });
}

/**
 * Show loading indicator
 */
function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('error').classList.add('hidden');
    document.getElementById('alerts-container').classList.add('hidden');
    document.getElementById('balance-container').classList.add('hidden');
    document.getElementById('fetch-btn').disabled = true;
}

/**
 * Hide loading indicator
 */
function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
    document.getElementById('fetch-btn').disabled = false;
}

/**
 * Show error message
 */
function showError(message) {
    const errorElement = document.getElementById('error');
    errorElement.textContent = message;
    errorElement.classList.remove('hidden');
    document.getElementById('balance-container').classList.add('hidden');
}

/**
 * Format change amount with sign and color class
 */
function formatChange(change) {
    const formatted = formatCurrency(Math.abs(change));
    if (change > 0) {
        return { text: `+${formatted}`, class: 'positive' };
    } else if (change < 0) {
        return { text: `-${formatted}`, class: 'negative' };
    } else {
        return { text: formatted, class: 'neutral' };
    }
}

/**
 * Display alerts in the UI
 */
function displayAlerts(alerts) {
    const alertsContainer = document.getElementById('alerts-container');
    alertsContainer.innerHTML = '';
    
    if (alerts && alerts.length > 0) {
        alerts.forEach(alert => {
            const alertDiv = document.createElement('div');
            alertDiv.className = 'alert-item';
            
            const icon = alert.type === 'wallet' ? '💰' : alert.type === 'fuel' ? '⛽' : '💳';
            
            alertDiv.innerHTML = `
                <span class="alert-icon">${icon}</span>
                <span class="alert-message">${alert.message}</span>
            `;
            
            alertsContainer.appendChild(alertDiv);
        });
        alertsContainer.classList.remove('hidden');
    } else {
        // Show "All balances are within safe limits" message
        const noAlertsDiv = document.createElement('div');
        noAlertsDiv.className = 'no-alerts';
        noAlertsDiv.textContent = 'All balances are within safe limits';
        alertsContainer.appendChild(noAlertsDiv);
        alertsContainer.classList.remove('hidden');
    }
}

/**
 * Display usage summary in the UI
 */
function displayUsageSummary(usageSummary) {
    const usageContainer = document.getElementById('usage-summary');
    
    if (!usageSummary) {
        usageContainer.classList.add('hidden');
        return;
    }
    
    // Format wallet change
    const walletChange = formatChange(usageSummary.wallet_change);
    const walletElement = document.getElementById('wallet-change');
    walletElement.textContent = walletChange.text;
    walletElement.className = `usage-change ${walletChange.class}`;
    
    // Format fuel change
    const fuelChange = formatChange(usageSummary.fuel_change);
    const fuelElement = document.getElementById('fuel-change');
    fuelElement.textContent = fuelChange.text;
    fuelElement.className = `usage-change ${fuelChange.class}`;
    
    // Format prepaid change
    const prepaidChange = formatChange(usageSummary.prepaid_change);
    const prepaidElement = document.getElementById('prepaid-change');
    prepaidElement.textContent = prepaidChange.text;
    prepaidElement.className = `usage-change ${prepaidChange.class}`;
    
    // Update period
    document.getElementById('usage-period').textContent = usageSummary.period;
    
    usageContainer.classList.remove('hidden');
}

/**
 * Display balance data in the UI
 */
function displayBalance(data) {
    // Hide error and loading
    document.getElementById('error').classList.add('hidden');
    document.getElementById('loading').classList.add('hidden');
    
    // Update vehicle ID
    document.getElementById('display-vehicle-id').textContent = data.vehicle_id;
    
    // Update last updated timestamp
    document.getElementById('last-updated').textContent = formatDate(data.last_updated);
    
    // Update balance amounts
    document.getElementById('wallet-balance').textContent = formatCurrency(data.balances.wallet);
    document.getElementById('fuel-balance').textContent = formatCurrency(data.balances.fuel);
    document.getElementById('prepaid-balance').textContent = formatCurrency(data.balances.prepaid);
    
    // Display alerts
    displayAlerts(data.alerts || []);
    
    // Display usage summary
    displayUsageSummary(data.usage_summary);
    
    // Show balance container
    document.getElementById('balance-container').classList.remove('hidden');
}

/**
 * Fetch vehicle balance from the API
 */
async function fetchBalance() {
    const vehicleId = document.getElementById('vehicle-id').value.trim();
    
    // Validate input
    if (!vehicleId) {
        showError('Please enter a vehicle ID');
        return;
    }
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/vehicle/${encodeURIComponent(vehicleId)}/balance`);
        
        if (!response.ok) {
            // Handle HTTP error responses
            if (response.status === 404) {
                const errorData = await response.json();
                showError(`Vehicle not found: ${vehicleId}. ${errorData.detail || 'Please check the vehicle ID and try again.'}`);
            } else {
                showError(`Error: ${response.status} ${response.statusText}. Please try again later.`);
            }
            return;
        }
        
        const data = await response.json();
        displayBalance(data);
        
    } catch (error) {
        // Handle network errors or other exceptions
        console.error('Error fetching balance:', error);
        showError('Network error: Unable to connect to the server. Please ensure the backend is running on http://localhost:8000');
    } finally {
        hideLoading();
    }
}

// Allow Enter key to trigger fetch
document.getElementById('vehicle-id').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        fetchBalance();
    }
});

