/**
 * Landing Page JavaScript
 * Handles smooth scrolling, demo functionality, and API integration
 */

const API_BASE_URL = 'http://localhost:8000';

/**
 * Scroll to demo section smoothly
 */
function scrollToDemo() {
    // If we're on a different page, navigate to homepage first
    if (window.location.pathname !== '/' && window.location.pathname !== '/index.html') {
        window.location.href = '/#demo';
        return;
    }
    
    const demoSection = document.getElementById('demo');
    if (demoSection) {
        demoSection.classList.remove('hidden');
        demoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
        // If demo section doesn't exist, navigate to homepage
        window.location.href = '/#demo';
    }
}

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
 * Show loading indicator
 */
function showLoadingDemo() {
    document.getElementById('loading-demo').classList.remove('hidden');
    document.getElementById('error-demo').classList.add('hidden');
    document.getElementById('balance-container-demo').classList.add('hidden');
    document.getElementById('fetch-btn-demo').disabled = true;
}

/**
 * Hide loading indicator
 */
function hideLoadingDemo() {
    document.getElementById('loading-demo').classList.add('hidden');
    document.getElementById('fetch-btn-demo').disabled = false;
}

/**
 * Show error message
 */
function showErrorDemo(message) {
    const errorElement = document.getElementById('error-demo');
    errorElement.textContent = message;
    errorElement.classList.remove('hidden');
    document.getElementById('balance-container-demo').classList.add('hidden');
}

/**
 * Display alerts in the UI
 */
function displayAlertsDemo(alerts) {
    const alertsContainer = document.getElementById('alerts-container-demo');
    alertsContainer.innerHTML = '';
    
    if (alerts && alerts.length > 0) {
        alerts.forEach(alert => {
            const alertDiv = document.createElement('div');
            alertDiv.className = 'alert-item';
            
            alertDiv.innerHTML = `
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
function displayUsageSummaryDemo(usageSummary) {
    const usageContainer = document.getElementById('usage-summary-demo');
    
    if (!usageSummary) {
        usageContainer.classList.add('hidden');
        return;
    }
    
    // Format wallet change
    const walletChange = formatChange(usageSummary.wallet_change);
    const walletElement = document.getElementById('wallet-change-demo');
    walletElement.textContent = walletChange.text;
    walletElement.className = `usage-change ${walletChange.class}`;
    
    // Format fuel change
    const fuelChange = formatChange(usageSummary.fuel_change);
    const fuelElement = document.getElementById('fuel-change-demo');
    fuelElement.textContent = fuelChange.text;
    fuelElement.className = `usage-change ${fuelChange.class}`;
    
    // Format prepaid change
    const prepaidChange = formatChange(usageSummary.prepaid_change);
    const prepaidElement = document.getElementById('prepaid-change-demo');
    prepaidElement.textContent = prepaidChange.text;
    prepaidElement.className = `usage-change ${prepaidChange.class}`;
    
    // Update period
    document.getElementById('usage-period-demo').textContent = usageSummary.period;
    
    usageContainer.classList.remove('hidden');
}

/**
 * Display balance data in the UI
 */
function displayBalanceDemo(data) {
    // Hide error and loading
    document.getElementById('error-demo').classList.add('hidden');
    document.getElementById('loading-demo').classList.add('hidden');
    
    // Update vehicle ID
    document.getElementById('display-vehicle-id-demo').textContent = data.vehicle_id;
    
    // Update last updated timestamp
    document.getElementById('last-updated-demo').textContent = formatDate(data.last_updated);
    
    // Update balance amounts
    document.getElementById('wallet-balance-demo').textContent = formatCurrency(data.balances.wallet);
    document.getElementById('fuel-balance-demo').textContent = formatCurrency(data.balances.fuel);
    document.getElementById('prepaid-balance-demo').textContent = formatCurrency(data.balances.prepaid);
    
    // Display alerts
    displayAlertsDemo(data.alerts || []);
    
    // Display usage summary
    displayUsageSummaryDemo(data.usage_summary);
    
    // Show balance container
    document.getElementById('balance-container-demo').classList.remove('hidden');
}

/**
 * Fetch vehicle balance from the API
 */
async function fetchBalanceDemo() {
    const vehicleId = document.getElementById('vehicle-id-demo').value.trim();
    
    // Validate input
    if (!vehicleId) {
        showErrorDemo('Please enter a vehicle ID');
        return;
    }
    
    showLoadingDemo();
    
    try {
        const response = await fetch(`${API_BASE_URL}/vehicle/${encodeURIComponent(vehicleId)}/balance`);
        
        if (!response.ok) {
            // Handle HTTP error responses
            if (response.status === 404) {
                const errorData = await response.json();
                showErrorDemo(`Vehicle not found: ${vehicleId}. ${errorData.detail || 'Please check the vehicle ID and try again.'}`);
            } else {
                showErrorDemo(`Error: ${response.status} ${response.statusText}. Please try again later.`);
            }
            return;
        }
        
        const data = await response.json();
        displayBalanceDemo(data);
        
    } catch (error) {
        // Handle network errors or other exceptions
        console.error('Error fetching balance:', error);
        showErrorDemo('Network error: Unable to connect to the server. Please ensure the backend is running on http://localhost:8000');
    } finally {
        hideLoadingDemo();
    }
}

// Allow Enter key to trigger fetch
document.addEventListener('DOMContentLoaded', function() {
    const vehicleInput = document.getElementById('vehicle-id-demo');
    if (vehicleInput) {
        vehicleInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                fetchBalanceDemo();
            }
        });
    }
    
    // Handle hash navigation to demo section
    if (window.location.hash === '#demo') {
        const demoSection = document.getElementById('demo');
        if (demoSection) {
            demoSection.classList.remove('hidden');
            setTimeout(() => {
                demoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    }
});

