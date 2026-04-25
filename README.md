# Stock Market Simulator

A simple stock market simulator built in Python.

## Requirements

- Docker

## How to run

```bash
./start.sh 8080
```

App will be available at http://localhost:8080

## How it works

The app consists of:

- 3 FastAPI instances (Python)
- Nginx that distributes traffic between instances
- Redis that stores all data

If one instance goes down (e.g. via /chaos) the other two keep running.

## Endpoints

- `GET /stocks` — get all stocks in the bank
- `POST /stocks` — set stocks in the bank
- `GET /wallets/{wallet_id}` — get wallet state
- `GET /wallets/{wallet_id}/stocks/{stock_name}` — get quantity of a specific stock
- `POST /wallets/{wallet_id}/stocks/{stock_name}` — buy or sell a stock
- `GET /log` — history of all operations
- `POST /chaos` — kills the instance handling this request

## How to stop

```bash
./stop.sh
```

---

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
./stop.sh
```
