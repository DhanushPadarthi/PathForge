class DummyDB:
    db = None

    async def connect_db(self):
        print("⚠️ MongoDB skipped (dev mode)")

    async def close_db(self):
        print("🛑 MongoDB closed")

db = DummyDB()
