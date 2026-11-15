const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;
const RECIPES_FILE = path.join(__dirname, 'recipes.json');
const PUBLIC_DIR = path.join(__dirname, 'public');

// Parse JSON request bodies
app.use(express.json({ limit: '50mb' }));

// Serve static assets from public directory
app.use(express.static(PUBLIC_DIR));

// API: Get recipes (source of truth: recipes.json)
app.get(['/api/recipes', '/recipes.json'], (req, res) => {
    fs.readFile(RECIPES_FILE, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading recipes.json:', err);
            return res.status(500).json({ error: 'Failed to load recipes from source of truth' });
        }
        try {
            const recipes = JSON.parse(data);
            res.setHeader('Content-Type', 'application/json; charset=utf-8');
            res.json(recipes);
        } catch (parseErr) {
            console.error('Error parsing recipes.json:', parseErr);
            res.status(500).json({ error: 'Invalid JSON in recipes source file' });
        }
    });
});

// API: Save/Update recipes (persists back to recipes.json)
app.post('/api/recipes', (req, res) => {
    const updatedRecipes = req.body;
    if (!Array.isArray(updatedRecipes)) {
        return res.status(400).json({ error: 'Invalid recipes format: expected array' });
    }

    const jsonString = JSON.stringify(updatedRecipes, null, 2);
    fs.writeFile(RECIPES_FILE, jsonString, 'utf8', (err) => {
        if (err) {
            console.error('Error writing recipes.json:', err);
            return res.status(500).json({ error: 'Failed to save recipes to disk' });
        }
        res.setHeader('Content-Type', 'application/json; charset=utf-8');
        res.json({ success: true, count: updatedRecipes.length });
    });
});

// Fallback to index.html for root or unknown GET routes
app.get('*', (req, res) => {
    res.sendFile(path.join(PUBLIC_DIR, 'index.html'));
});

// Start Server
let server;
if (require.main === module) {
    server = app.listen(PORT, () => {
        console.log(`=======================================================`);
        console.log(`  Blue Healing Resort & Wellness Platform Server       `);
        console.log(`  Running at: http://localhost:${PORT}                 `);
        console.log(`  Source of Truth: ${RECIPES_FILE}                     `);
        console.log(`  Static Directory: ${PUBLIC_DIR}                      `);
        console.log(`=======================================================`);
    });
}

// Graceful termination
process.on('SIGINT', () => {
    server.close(() => {
        console.log('Server stopped gracefully.');
        process.exit(0);
    });
});

process.on('SIGTERM', () => {
    server.close(() => {
        console.log('Server stopped gracefully.');
        process.exit(0);
    });
});

module.exports = app;
