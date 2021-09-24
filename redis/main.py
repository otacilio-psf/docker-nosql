import redis

r = redis.Redis()

r.set("usuario:1:nome", "Otacilio")
r.mset({"usuario:1:sobrenome": "Filho", "usuario:1:idade": 29})

print(r.get("usuario:1:nome"))
print(r.mget(["usuario:1:nome","usuario:1:sobrenome"]))

r.hmset("usuario:2", {"nome": "Pedro", "sobrenome": "Filho", "idade": 29}) #deprecated

r.hset("usuario:3", mapping={"nome": "Pedro", "sobrenome": "Filho", "idade": 29})

print(type(r.hgetall("usuario:2")))
print(r.hgetall("usuario:2"))

print(type(r.hgetall("usuario:3")))
print(r.hgetall("usuario:3"))