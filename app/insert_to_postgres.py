import json
from datetime import date
from app.utils.security import hash_password
from app.database import sessionLocal
from app.models import (
    UsersModel,
    EmployeeModel,
    TodosModel,
    ProductsModel,
    SalesModel,
)


MAX_INT = 2_147_483_647

def import_users(db, users):
    for u in users:
        try:
            user_id = int(u["id"])
        except ValueError:
            print(f"건너뜀(숫자 아님): {u['id']}")
            continue

        if user_id > MAX_INT:
            print(f"건너뜀(Integer 초과): {user_id}")
            continue

        db.add(
            UsersModel(
                id=user_id,
                username=u["name"],
                password=hash_password(u["password"]),
                age=u["age"],
                email=u["email"],
                city=u["city"],
            )
        )

def import_employees(db, employees):
    for e in employees:

        # 숫자가 아닌 id는 건너뜀
        if not str(e["id"]).isdigit():
            print(f"건너뜀: {e['id']}")
            continue

        db.add(
            EmployeeModel(
                id=int(e["id"]),
                name=e["name"],
                email=e["email"],
                job=e["job"],
                pay=int(e["pay"]),
            )
        )

def import_todos(db, todos):
    for t in todos:
        db.add(
            TodosModel(
                id=int(t["id"]),
                subject=t["subject"],
                checked=t["checked"],
                created_at=date.today(),  # 👈 추가
            )
        )


def import_products(db, products):
    for p in products:
        db.add(
            ProductsModel(
                id=int(p["id"]),
                product_name=p["product_name"],
                color=p["color"],
                price=p["cost_price"],
                sale_price=p["sale_price"],
                category_code=p["category_code"],
            )
        )


def import_sales(db, sales):
    from app.models import UsersModel, ProductsModel

    db.flush()  # 👈 추가: 지금까지 add()한 것들을 DB에 반영(커밋은 아님)

    existing_user_ids = {row[0] for row in db.query(UsersModel.id).all()}
    existing_product_ids = {row[0] for row in db.query(ProductsModel.id).all()}

    for s in sales:
        if s["user_id"] not in existing_user_ids:
            print(f"건너뜀(sales id={s['id']}): user_id={s['user_id']} 없음")
            continue
        if s["product_id"] not in existing_product_ids:
            print(f"건너뜀(sales id={s['id']}): product_id={s['product_id']} 없음")
            continue

        db.add(
            SalesModel(
                id=int(s["id"]),
                user_id=s["user_id"],
                product_id=s["product_id"],
                quantity=s["quantity"],
                discount_rate=s["discount_rate"],
                total_price=s["total_price"],
                created_at=s["created_at"],
            )
        )

def main():
    db = sessionLocal()

    with open("db.json", encoding="utf-8") as f:
        data = json.load(f)

    import_users(db, data["user"])
    import_employees(db, data["employees"])
    import_todos(db, data["todos"])
    import_products(db, data["product"])
    import_sales(db, data["sales"])

    db.commit()
    db.close()

    print("데이터 Import 완료")


if __name__ == "__main__":
    main()