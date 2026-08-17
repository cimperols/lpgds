const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

// Extract the JS code from <script>
const match = html.match(/<script>([\s\S]*?)<\/script>/);
if (!match) {
    console.log("No script tag found!");
    process.exit(1);
}
const js = match[1];

// Mock basic DOM environment
global.window = {
    innerWidth: 1024,
    innerHeight: 768,
    addEventListener: () => {}
};
global.document = {
    getElementById: (id) => {
        console.log(`Mock getElementById: ${id}`);
        return {
            width: 0,
            height: 0,
            getContext: () => ({
                fillRect: () => {},
                fillText: () => {}
            }),
            addEventListener: () => {}
        };
    },
    querySelectorAll: (selector) => {
        console.log(`Mock querySelectorAll: ${selector}`);
        return [];
    },
    addEventListener: () => {}
};

try {
    eval(js);
    console.log("Execution successful under mock DOM!");
} catch (e) {
    console.error("Runtime Exception:", e);
}
