import strawberry
from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas.sales import SaleType
from app.services import sales as sale_service


def _to_sale_type(sale) -> SaleType:
    return SaleType(
        id=sale.id,
        user_id=sale.user_id,
        product_id=sale.product_id,
        quantity=sale.quantity,
        discount_rate=sale.discount_rate,
        total_price=sale.total_price,
        created_at=sale.created_at,
    )


@strawberry.type
class SaleQuery:

    @strawberry.field
    def sales(self) -> list[SaleType]:
        db = SessionLocal()
        try:
            sales = sale_service.get_all_sales(db)
            return [_to_sale_type(s) for s in sales]
        finally:
            db.close()

    @strawberry.field
    def sale(self, id: int) -> SaleType | None:
        db = SessionLocal()
        try:
            try:
                sale = sale_service.get_sale(db, id)
            except HTTPException:
                return None
            return _to_sale_type(sale)
        finally:
            db.close()