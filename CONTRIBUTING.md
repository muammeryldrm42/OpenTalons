# Contributing

## Branch sync and conflict strategy

Bu repoda PR branch'leri hızlı ilerlediği için zaman zaman `This branch has conflicts that must be resolved` durumu oluşabilir.

### 1) Normal yol: main ile sync + otomatik çözüm

```bash
scripts/sync_with_main.sh origin main
```

Bu script:
1. `origin/main` fetch eder
2. `rerere` açar (aynı conflict bir daha çıkarsa otomatik uygular)
3. Rebase dener
4. Conflict olursa deterministic policy uygular:
   - `README.md` ve `tests/*`: `theirs`
   - `src/opentalons/*`: `ours`
   - Diğerleri: `ours`
5. Rebase birden fazla committe tekrar conflict verirse otomatik döngü ile her turu çözer

### 2) Hızlı yol: halihazırdaki conflict'i direkt çöz

GitHub PR ekranında conflict dosyaları listelenmişse:

```bash
scripts/resolve_conflicts_now.sh
```

Dry-run görmek için:

```bash
scripts/resolve_conflicts_now.sh --dry-run
```

Bu script açık olan merge/rebase/cherry-pick durumundaki `U` dosyalarını tek seferde kural bazlı çözer ve uygun durumda `--continue` komutunu dener.

### 3) GitHub üstünden tek tık çözüm (manual workflow)

Repo sahibiysen Actions -> **Autofix PR conflicts** workflow'unu çalıştır:

- `pr_number` gir
- workflow ilgili PR branch'ini checkout eder
- base branch ile merge eder
- conflict olursa kurallı şekilde çözer
- branch'e otomatik push atar

Kullanılan script: `scripts/autofix_pr_conflicts.sh`

## Config resolution guardrails

Provider config her zaman geçerli olmayabilir. Bu yüzden orchestrator, provider çözümünde fallback uygular:

- İstenen provider varsa onu kullanır.
- Yoksa `mock` fallback'e düşer.
- Fallback da yoksa defensive olarak `MockProvider()` döner.

Bu davranış `src/opentalons/providers/__init__.py` içindeki `resolve_provider` fonksiyonunda uygulanır.
