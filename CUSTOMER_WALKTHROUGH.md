# Customer Walkthrough Guide
## Vehicle Balance Viewer - How to Use

### 🚀 Quick Start

**Frontend URL:** http://localhost:8080  
**Backend API:** http://localhost:8000

---

## 📋 Step-by-Step Customer Guide

### Step 1: Open the Website
1. The website should automatically open in your browser
2. If not, navigate to: **http://localhost:8080**
3. You'll see a beautiful purple gradient header with "Vehicle Balance Viewer"

### Step 2: Enter Vehicle ID
1. Look for the **"Vehicle ID"** input field below the header
2. Type in a vehicle registration number or ID
3. **Available test vehicle IDs:**
   - `DL01AB1234` (Delhi vehicle)
   - `MH12XY5678` (Maharashtra vehicle)
   - `KA03CD9012` (Karnataka vehicle)
   - `TN09EF3456` (Tamil Nadu vehicle)

**Example:** Type `DL01AB1234` in the input field

### Step 3: Fetch Balance
1. Click the **"Fetch Balance"** button (purple gradient button)
2. **OR** press the **Enter** key on your keyboard
3. You'll see a loading spinner appear with "Loading balance information..."

### Step 4: View Results

#### ✅ **Success Scenario:**
If the vehicle ID exists, you'll see:

1. **Vehicle Information Header:**
   - Vehicle ID displayed prominently
   - Last updated timestamp (in readable format)

2. **Three Balance Cards:**
   - **💰 Wallet Balance** (Green border)
     - Shows your wallet balance in INR
   - **⛽ Fuel Balance** (Orange border)
     - Shows your fuel balance in INR
   - **💳 Prepaid Balance** (Blue border)
     - Shows your prepaid balance in INR

3. **Example Display:**
   ```
   Vehicle: DL01AB1234
   Last Updated: Jan 4, 2026, 12:08:31 PM UTC
   
   💰 Wallet: ₹2,450.75
   ⛽ Fuel: ₹1,200.00
   💳 Prepaid: ₹800.00
   ```

#### ❌ **Error Scenario:**
If the vehicle ID doesn't exist (e.g., `INVALID123`):

1. A red error message box appears
2. Message: **"Vehicle not found: [vehicle_id]. Please check the vehicle ID and try again."**
3. The balance cards remain hidden
4. You can try again with a different vehicle ID

#### 🔴 **Network Error Scenario:**
If the backend server is not running:

1. A red error message appears
2. Message: **"Network error: Unable to connect to the server. Please ensure the backend is running on http://localhost:8000"**
3. Check that the backend server is running

---

## 🎯 Customer Use Cases

### Use Case 1: Check Your Vehicle Balance
**Scenario:** You want to check how much balance you have in your vehicle account.

**Steps:**
1. Enter your vehicle registration number (e.g., `DL01AB1234`)
2. Click "Fetch Balance"
3. View all three balances (Wallet, Fuel, Prepaid)

**Expected Result:** See all balances displayed in colorful cards with proper currency formatting.

---

### Use Case 2: Verify Multiple Vehicles
**Scenario:** You manage multiple vehicles and want to check each one.

**Steps:**
1. Enter first vehicle ID: `DL01AB1234` → Click "Fetch Balance"
2. View results
3. Enter second vehicle ID: `MH12XY5678` → Click "Fetch Balance"
4. View different results

**Expected Result:** Each vehicle shows its own unique balance information.

---

### Use Case 3: Handle Invalid Vehicle ID
**Scenario:** You accidentally type a wrong vehicle ID.

**Steps:**
1. Enter an invalid ID: `WRONG123`
2. Click "Fetch Balance"
3. See error message

**Expected Result:** Clear error message explaining the vehicle was not found, allowing you to correct and try again.

---

## 🎨 User Interface Features

### Visual Elements:
- **Modern Design:** Purple gradient header with clean white content area
- **Responsive Layout:** Works on desktop, tablet, and mobile devices
- **Color-Coded Cards:** Each balance type has a distinct color border
- **Smooth Animations:** Cards fade in when data loads
- **Loading Indicator:** Spinner shows during API calls
- **Error Styling:** Red error boxes for clear feedback

### Interactive Features:
- **Enter Key Support:** Press Enter to fetch balance (no need to click button)
- **Button Hover Effects:** Button lifts slightly on hover
- **Disabled State:** Button is disabled during loading to prevent multiple requests
- **Auto-formatting:** Currency amounts are automatically formatted in Indian Rupees (INR)

---

## 🔍 Available Test Vehicles

| Vehicle ID | Wallet | Fuel | Prepaid |
|------------|--------|------|---------|
| DL01AB1234 | ₹2,450.75 | ₹1,200.00 | ₹800.00 |
| MH12XY5678 | ₹1,800.00 | ₹950.50 | ₹400.00 |
| KA03CD9012 | ₹3,200.25 | ₹2,100.00 | ₹1,500.00 |
| TN09EF3456 | ₹950.00 | ₹650.75 | ₹300.00 |

---

## ⚠️ Troubleshooting

### Problem: "Network error" message
**Solution:** 
- Ensure the backend server is running on port 8000
- Check terminal/console for backend server status
- Restart backend: `cd backend && python main.py`

### Problem: Website not loading
**Solution:**
- Verify frontend server is running on port 8080
- Try refreshing the page (F5)
- Check browser console for errors (F12)

### Problem: Balance not showing
**Solution:**
- Verify you entered a valid vehicle ID (case-sensitive)
- Check that both frontend and backend servers are running
- Look for error messages in red boxes

### Problem: CORS errors in browser console
**Solution:**
- Backend CORS is already configured
- If issues persist, ensure backend is running and accessible

---

## 💡 Tips for Best Experience

1. **Use Valid Vehicle IDs:** Only the 4 test vehicles listed above will work
2. **Check Spelling:** Vehicle IDs are case-sensitive
3. **Wait for Loading:** Don't click multiple times - wait for the spinner to finish
4. **Try Different Vehicles:** Test with different vehicle IDs to see various balances
5. **Read Error Messages:** They provide helpful information about what went wrong

---

## 🎬 Quick Demo Flow

```
1. Open http://localhost:8080
   ↓
2. Type: DL01AB1234
   ↓
3. Click "Fetch Balance" or Press Enter
   ↓
4. See loading spinner (1-2 seconds)
   ↓
5. View balance cards with:
   - Wallet: ₹2,450.75
   - Fuel: ₹1,200.00
   - Prepaid: ₹800.00
   ↓
6. Try another vehicle: MH12XY5678
   ↓
7. See different balances
```

---

## 📱 Mobile Experience

The website is fully responsive and works great on mobile devices:
- Touch-friendly buttons
- Readable text sizes
- Stacked balance cards on small screens
- Easy input field for vehicle ID

---

## ✨ What Makes This Experience Great

1. **Fast Response:** API responds in < 500ms
2. **Clear Feedback:** Loading states and error messages
3. **Beautiful UI:** Modern, professional design
4. **Easy to Use:** Simple input → click → view results
5. **Reliable:** Proper error handling for all scenarios

---

**Enjoy using the Vehicle Balance Viewer! 🚗💰**

