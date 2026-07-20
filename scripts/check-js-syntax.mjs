import fs from "node:fs";

const files = [
  "course/assets/course.js",
  "course/assets/classification.js",
  "course/assets/reader.js",
];

for (const file of files) {
  const source = fs.readFileSync(file, "utf8");
  new Function(source);
  console.log(`OK: ${file}`);
}
