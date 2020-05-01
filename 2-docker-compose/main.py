from fastapi import FastAPI
import redis

app = FastAPI()

pool = redis.ConnectionPool(host="myredis", port=6379, db=0)
redis_cli = redis.StrictRedis(connection_pool=pool)

@app.get("/")
def root():
    redis_cli.set("answer", "yes!!")
    return {"connect?": redis_cli.get("answer")}
