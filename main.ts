import { writeFileSync, mkdirSync, chmodSync } from "node:fs";

mkdirSync("/output", { recursive: true });
writeFileSync("/output/entry.txt", "A", "utf8");
chmodSync("/output/entry.txt", 0o644);
console.log("A");
