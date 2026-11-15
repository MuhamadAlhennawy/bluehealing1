# ✦ Blue Healing • Recipe Cost Calculator & Menu Engineering ✦

An integrated platform for standard recipe costing, menu engineering (Standard Recipe Cost Card), and resort wellness operations at Blue Healing Resort & Wellness. Built with a Node.js backend and a dynamic, responsive frontend.

---

## 🌟 Key Features

- **Node.js Express Backend:** High-performance, lightweight backend serving static client assets and RESTful API endpoints.
- **Dynamic Recipe Loading:** Recipe data is decoupled from the frontend code; recipes are dynamically fetched on startup from `recipes.json` (the single source of truth).
- **Accurate Food Costing:** Automated unit conversion (grams to kilograms, milliliters to liters, portions, and pieces).
- **Price Date Tracking:** Record and monitor vendor price update dates to manage market fluctuations.
- **Standard Waste Factor (5%):** Automatically calculates peeling, trimming, and cooking loss.
- **Pricing Multipliers (3.1 – 3.6):** Optimizes menu sales pricing based on target Food Cost % benchmarks.
- **Interactive Cost Breakdown:** Visual breakdown of ingredient cost contributions.
- **Financial KPIs:** Real-time calculation of gross profit per portion and profit margin percentage.
- **Professional Excel (.xlsx) Export:** One-click generation of branded Excel recipe cards with live formulas.
- **Print & PDF Ready:** Compliant with standard operating procedure (SOP) recipe card formatting.
- **Arabic Language & UTF-8 Preserved:** Native right-to-left (RTL) Arabic typography and strict UTF-8 character encoding throughout.

---

## 📁 Project Structure

```text
bluehealing/
├── public/                               # Frontend client and static assets
│   ├── index.html                        # Main web application (dynamic data loading)
│   ├── food_cost_calculator.html         # Recipe costing interface
│   ├── logo.jpg                          # Resort branding logo
│   ├── Standard_Recipe_Cost_Card.xlsx    # Master Excel cost template
│   └── recipes.json                      # Symlink to root recipes.json
├── scripts/
│   └── legacy_python/                    # Archived Python desktop and utility scripts
├── recipes.json                          # Source of truth for all recipe data (UTF-8)
├── server.js                             # Node.js backend server and REST API
├── package.json                          # Project metadata, scripts, and dependencies
├── package-lock.json                     # Dependency version lock
├── .gitignore                            # Git ignore rules (node_modules, logs, etc.)
└── README.md                             # Project documentation and instructions
```

---

## 📋 Prerequisites

- **Node.js** (v18.0.0 or higher recommended)
- **npm** (comes bundled with Node.js)

Verify your Node.js and npm installations:
```bash
node -v
npm -v
```

---

## 🚀 Getting Started

### 1. Installation

Clone or navigate to the project directory, then install the dependencies:

```bash
npm install
```

### 2. Running the Server

Start the application with npm:

```bash
npm start
```

Alternatively, you can run the server directly using Node:

```bash
node server.js
```

To run on a custom port, set the `PORT` environment variable:

```bash
PORT=8080 node server.js
```

### 3. Accessing the Application

Once the server has started, open your web browser and navigate to:

```text
http://localhost:3000
```

---

## 🔌 API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/api/recipes` | `GET` | Returns all 92 standard recipes from `recipes.json` (`Content-Type: application/json; charset=utf-8`). |
| `/api/recipes` | `POST` | Updates and persists the recipe list to `recipes.json`. |
| `/` | `GET` | Serves the main application from `public/index.html`. |
| `/*` | `GET` | Serves static assets from `public/` (images, stylesheets, templates). |

---

## 📊 Data Source of Truth

- **`recipes.json`** at the project root is the authoritative source of truth for all 92 recipes.
- When the frontend loads, it calls `GET /api/recipes` to retrieve the latest data.
- All modifications are encoded in strict UTF-8 to ensure that Arabic names, ingredient details, badges, and units are maintained without corruption.

---

### Developed by **Blue Healing Team** ✦
