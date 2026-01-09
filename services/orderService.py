
from models.orders import BuyProduct

def orderService(req, db):
    new_order = BuyProduct(**req.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order created successfully", "order": new_order}