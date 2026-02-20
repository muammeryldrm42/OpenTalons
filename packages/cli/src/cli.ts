import { Command } from "commander";
import path from "node:path";
import { listPacks, loadPackIndex } from "@opentalons/loader";

const program = new Command();
program.name("opentalons").version("0.1.0");

program.command("list-packs").action(async () => {
  const packsRoot = path.join(process.cwd(), "skills", "packs");
  console.log(JSON.stringify(await listPacks(packsRoot), null, 2));
});

program.command("list-skills").requiredOption("--pack <pack>").action(async (opts) => {
  const packDir = path.join(process.cwd(), "skills", "packs", opts.pack);
  console.log(JSON.stringify((await loadPackIndex(packDir)).skills, null, 2));
});

program.parseAsync(process.argv);
