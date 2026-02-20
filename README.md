# OpenTalons

Full-version monorepo skeleton:
- Core/contracts/loader/cli (TypeScript)
- 200 skills in packs
- Runtime-ready extension packages (showcase docs now)
- Next.js UI catalog (Vercel-ready, no run UI yet)

## Install
```bash
corepack enable
pnpm install
pnpm -r build
pnpm -r test
```

## UI
```bash
pnpm -C ui dev
```

## Vercel
Deploy `ui/` only. See `docs/vercel.md`.
