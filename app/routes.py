from fastapi import APIRouter, HTTPException
from database import r
from models import TradeRequest, StocksPayload
import json
import os
import signal

router = APIRouter()

@router.post("/stocks")
def set_stocks(body: StocksPayload):
    for item in body.stocks:
        r.set(f"bank:{item.name}", item.quantity)
    return {"status": "ok"}

@router.get("/stocks")
def get_stocks():
    keys = r.keys("bank:*")
    stocks = []
    for key in keys:
        name = key.split(":")[1]
        quantity = int(r.get(key))
        stocks.append({"name": name, "quantity": quantity})
    return {"stocks": stocks}

@router.get("/wallets/{wallet_id}")
def get_wallet(wallet_id: str):
    keys = r.keys(f"wallet:{wallet_id}:*")
    stocks = []
    for key in keys:
        name = key.split(":")[2]
        quantity = int(r.get(key))
        if quantity > 0:
            stocks.append({"name": name, "quantity": quantity})
    return {"id": wallet_id, "stocks": stocks}

@router.get("/wallets/{wallet_id}/stocks/{stock_name}")
def get_wallet_stock(wallet_id: str, stock_name: str):
    if r.get(f"bank:{stock_name}") is None:
        raise HTTPException(status_code=404, detail="Stock does not exist")
    quantity = r.get(f"wallet:{wallet_id}:{stock_name}")
    if quantity is None:
        return 0
    return int(quantity)

@router.post("/wallets/{wallet_id}/stocks/{stock_name}")
def trade_stock(wallet_id: str, stock_name: str, body: TradeRequest):
    bank_key = f"bank:{stock_name}"
    wallet_key = f"wallet:{wallet_id}:{stock_name}"

    if r.get(bank_key) is None:
        raise HTTPException(status_code=404, detail="Stock does not exist")

    if body.type == "buy":
        if int(r.get(bank_key)) <= 0:
            raise HTTPException(status_code=400, detail="No stock available in bank")
        r.decr(bank_key)
        r.incr(wallet_key)

    elif body.type == "sell":
        wallet_qty = r.get(wallet_key)
        if wallet_qty is None or int(wallet_qty) <= 0:
            raise HTTPException(status_code=400, detail="No stock in wallet to sell")
        r.incr(bank_key)
        r.decr(wallet_key)

    else:
        raise HTTPException(status_code=400, detail="type must be 'buy' or 'sell'")
    
    log_entry = json.dumps({"type": body.type, "wallet_id": wallet_id, "stock_name": stock_name})
    r.rpush("log", log_entry)

    return {"status": "ok"}

@router.get("/log")
def get_log():
    entries = r.lrange("log", 0, -1)
    log = [json.loads(entry) for entry in entries]
    return {"log": log}

@router.post("/chaos")
def chaos():
    os.kill(os.getpid(), signal.SIGTERM)
    return {"status": "terminating"}
