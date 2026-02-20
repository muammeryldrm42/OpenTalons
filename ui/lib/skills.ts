import path from "node:path";
import fs from "node:fs/promises";
import { repoRoot } from "./root";

export async function getPacks() {
  const p = path.join(repoRoot(), "skills", "packs");
  const e = await fs.readdir(p, { withFileTypes: true });
  return e.filter(x => x.isDirectory()).map(x => x.name).sort();
}

export async function getPackIndex(pack: string) {
  const p = path.join(repoRoot(), "skills", "packs", pack, "index.json");
  return JSON.parse(await fs.readFile(p, "utf-8"));
}

export async function getSkill(pack: string, slug: string) {
  const root = repoRoot();
  const md = await fs.readFile(path.join(root, "skills", "packs", pack, "skills", slug, "SKILL.md"), "utf-8");
  const manifest = JSON.parse(await fs.readFile(path.join(root, "skills", "packs", pack, "skills", slug, "manifest.json"), "utf-8"));
  return { md, manifest };
}
