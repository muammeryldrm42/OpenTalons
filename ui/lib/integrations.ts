import path from "node:path";
import fs from "node:fs/promises";
import { repoRoot } from "./root";

export async function getIntegrations() {
  const p = path.join(repoRoot(), "extensions");
  const e = await fs.readdir(p, { withFileTypes: true });
  const slugs = e.filter(x => x.isDirectory()).map(x => x.name);
  const items = [];
  for (const s of slugs) {
    const manifest = JSON.parse(await fs.readFile(path.join(p, s, "manifest.json"), "utf-8"));
    items.push(manifest);
  }
  items.sort((a,b)=> (a.category||"").localeCompare(b.category||"") || (a.title||"").localeCompare(b.title||""));
  return items;
}

export async function getIntegration(slug: string) {
  const root = repoRoot();
  const manifest = JSON.parse(await fs.readFile(path.join(root, "extensions", slug, "manifest.json"), "utf-8"));
  const md = await fs.readFile(path.join(root, "extensions", slug, "README.md"), "utf-8");
  return { manifest, md };
}
