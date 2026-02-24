# OpenTalons

OpenTalons, OpenClaw benzeri ajan orkestrasyon yaklaşımını daha sade, test edilebilir ve genişletilebilir bir çekirdekle başlatmak için hazırlanmış bir projedir.

## Vizyon

- **Modüler sağlayıcı sistemi**: Farklı LLM/araç sağlayıcıları tak-çalıştır şekilde eklenir.
- **Görev odaklı orkestrasyon**: Planlama + yürütme tek çekirdekten yönetilir.
- **CLI + kütüphane kullanımı**: Hem terminalden hem Python içinden çalışır.
- **Test-first mimari**: Çekirdek davranışlar testlerle güvence altındadır.

## Hızlı Başlangıç

```bash
PYTHONPATH=src pytest
python -m opentalons.cli "Bir proje yol haritası hazırla" --context "AI automation startup"
```

## Mimari

- `opentalons.providers`: Sağlayıcı arayüzü ve implementasyonlar
- `opentalons.orchestrator`: Görev yürütme akışı
- `opentalons.api`: Servis katmanı için saf Python giriş fonksiyonları
- `opentalons.cli`: Komut satırı arayüzü

## Sonraki Adımlar (OpenClaw'dan daha iyi olmak için)

1. Gerçek LLM adaptörleri (OpenAI/Anthropic/local)
2. Tool-calling ve güvenli aksiyon yürütme katmanı
3. Kalıcı bellek (event log + vector memory)
4. Web panel + gözlemlenebilirlik (trace, token, latency)
5. Multi-agent görev devri ve geri bildirim döngüsü
