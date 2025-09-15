from app import create_app, db
from app.models import PregnancyRecord
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    # יוצרת את כל הטבלאות אם הן לא קיימות
    db.create_all()

    # בדיקה אם הטבלה קיימת
    inspector = inspect(db.engine)
    if inspector.has_table("pregnancy_record"):
        print("✅ Table 'pregnancy_record' exists or was created successfully.")
    else:
        print("❌ Failed to create 'pregnancy_record'.")
