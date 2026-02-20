import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export function getManifest() {
  const p = path.join(__dirname, "..", "manifest.json");
  return JSON.parse(fs.readFileSync(p, "utf-8"));
}