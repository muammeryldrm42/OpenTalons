import fs from "node:fs/promises";
import path from "node:path";
import type { SkillManifest } from "@opentalons/contracts";
export interface PackIndex { pack: string; description?: string; skills: Array<{ slug: string; name: string; version: string; category?: string; tags?: string[]; permissions?: string[] }>; }
export async function readJson<T>(p:string):Promise<T>{ return JSON.parse(await fs.readFile(p,"utf-8")) as T; }
export async function loadPackIndex(packDir:string):Promise<PackIndex>{ return readJson(path.join(packDir,"index.json")); }
export async function loadSkillManifest(skillDir:string):Promise<SkillManifest>{ return readJson(path.join(skillDir,"manifest.json")); }
export async function listPacks(packsRoot:string):Promise<string[]>{ const e=await fs.readdir(packsRoot,{withFileTypes:true}); return e.filter(x=>x.isDirectory()).map(x=>x.name).sort(); }
