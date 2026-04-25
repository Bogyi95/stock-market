# Stock Market Simulator

Projekt na rekrutację. Symulator giełdy napisany w Pythonie.

## Jak uruchomić

Potrzebujesz mieć zainstalowanego Dockera.

```bash
./start.sh 8080
```

Aplikacja będzie dostępna pod adresem http://localhost:8080

## Jak działa

Aplikacja składa się z:

- 3 instancji FastAPI (Python)
- Nginx który rozdziela ruch między instancje
- Redis który przechowuje dane

Dzięki temu jeśli jedna instancja padnie to pozostałe dwie dalej działają.

## Endpointy

- `GET /stocks` — sprawdź ile stocków ma bank
- `POST /stocks` — dodaj stocki do banku
- `GET /wallets/{wallet_id}` — sprawdź portfel
- `GET /wallets/{wallet_id}/stocks/{stock_name}` — sprawdź ile masz danego stocka
- `POST /wallets/{wallet_id}/stocks/{stock_name}` — kup lub sprzedaj stock
- `GET /log` — historia operacji
- `POST /chaos` — zabija jedną instancję

## Zatrzymanie

```bash
docker compose down
```
