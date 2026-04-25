from pydantic import BaseModel

class TradeRequest(BaseModel):
    type: str

class StockItem(BaseModel):
    name: str
    quantity: int

class StocksPayload(BaseModel):
    stocks: list[StockItem]