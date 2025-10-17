from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["shopDB"]
products = db["products"]

products.delete_many({})

products_data = [
    {"name": "Laptop", "category": "Electronics", "price": 450000},
    {"name": "Mouse", "category": "Electronics", "price": 8000},
    {"name": "Desk", "category": "Furniture", "price": 120000},
    {"name": "Chair", "category": "Furniture", "price": 70000}
]
products.insert_many(products_data)

query = {"category": "Electronics", "price": {"$gt": 10000}}
projection = {"_id": 0, "name": 1, "price": 1}
result = products.find(query, projection).sort("price", 1)

print("\n📦 Товары категории 'Electronics' с ценой > 10000 (по возрастанию):")
for product in result:
    print(f"- {product['name']}: {product['price']}₸")

client.close()
print("\n✅ Готово!")
