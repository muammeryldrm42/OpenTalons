# OpenTalons

OpenTalons, OpenClaw tarzı ajan orkestrasyonunu daha temiz bir çekirdek + daha güçlü API yüzeyi ile büyütmek için geliştirilen projedir.

## Part 2 ile Gelen Özellikler

- Task lifecycle API (`create`, `execute`, `list`, `get`)
- In-memory görev deposu (task id, status, error, timestamps)
- Araç (tool) kataloğu ve otomatik tool-call kaydı
- Senkron tek-shot (`run_goal`) + görev tabanlı çalışma modeli
- Genişletilebilir provider mimarisi

## CLI Kullanımı

```bash
python -m opentalons.cli run "Q3 GTM planı çıkar" --context "B2B AI"
python -m opentalons.cli create "MVP roadmap üret"
python -m opentalons.cli list
python -m opentalons.cli execute <task_id>
python -m opentalons.cli get <task_id>
```

## Python API Kullanımı

```python
from opentalons.api.app import OpenTalonsAPI

api = OpenTalonsAPI()
task = api.create_task("Launch plan hazırla", context="Fintech")
finished = api.execute_task(task["task_id"])
print(finished["status"])
```

## Mimari

- `opentalons.providers`: LLM/provider sözleşmesi ve implementasyonlar
- `opentalons.orchestrator`: Planlama + yürütme + task lifecycle
- `opentalons.store`: Task kalıcılık arayüzü (şimdilik in-memory)
- `opentalons.tools`: Tool registry ve built-in araçlar
- `opentalons.api`: Uygulama servis katmanı (HTTP adapter'a hazır)
- `opentalons.cli`: Komut satırı yüzeyi

## Sıradaki büyük adımlar

1. FastAPI adapter + OpenAPI + auth
2. WebSocket event stream (token/step progress)
3. Persistent DB store (PostgreSQL/SQLite)
4. Real LLM providers + tool sandbox
5. Multi-agent planner/executor mode
