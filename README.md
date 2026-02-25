# OpenTalons → OpenClaw Mirror Bootstrap

Bu depo, `https://github.com/openclaw/openclaw` deposunu **birebir yansıtmak** için hazırlandı.

## Hızlı kullanım

```bash
./scripts/mirror_openclaw.sh
```

Script şunları yapar:

1. OpenClaw `main` branch arşivini indirir.
2. Bu depodaki mevcut dosyaları temizler (`.git` hariç).
3. OpenClaw dosyalarını bu depoya kopyalar.

## Not

Bu ortam GitHub'a erişemiyorsa (proxy/403), script indirme adımında durur. Erişim sağlandığında tekrar çalıştırmanız yeterlidir.
