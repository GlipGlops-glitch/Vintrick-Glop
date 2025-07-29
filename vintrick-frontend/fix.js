// File: generate-css-and-imports.js
const fs = require("fs");
const path = require("path");

const screensDir = path.join(__dirname, "src", "screens");

// Get all JS files in screens dir
fs.readdirSync(screensDir).forEach((file) => {
  if (file.endsWith(".js")) {
    const baseName = path.basename(file, ".js");
    const cssName = `${baseName}.css`;
    const cssPath = path.join(screensDir, cssName);
    const jsPath = path.join(screensDir, file);

    // 1. Create empty CSS file if not exist
    if (!fs.existsSync(cssPath)) {
      fs.writeFileSync(cssPath, `/* Styles for ${baseName} */\n`);
      console.log(`Created ${cssName}`);
    }

    // 2. Add import statement if not already present
    let jsContents = fs.readFileSync(jsPath, "utf8");
    const importLine = `import './${cssName}';`;
    if (!jsContents.includes(importLine)) {
      jsContents = `${importLine}\n${jsContents}`;
      fs.writeFileSync(jsPath, jsContents, "utf8");
      console.log(`Added import to ${file}`);
    }
  }
});

console.log("All done!");
