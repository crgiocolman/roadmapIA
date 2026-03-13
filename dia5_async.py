import asyncio

async def tarea(nombre, segundos):
    print(f"{nombre} iniciada")
    await asyncio.sleep(segundos)
    print(f"{nombre} terminada")

async def main():
    await asyncio.gather(
        tarea("Tarea 1", 2),
        tarea("Tarea 2", 1)
    )

asyncio.run(main())

async def llamar_api(id_contacto):
    print(f"Consultando contacto {id_contacto}...")
    await asyncio.sleep(1)  # Simula la llamada API
    return {"id": id_contacto, "nombre": f"Contacto {id_contacto}"}

async def main_zoho():
    resultados = await asyncio.gather(
        llamar_api(1),
        llamar_api(2),
        llamar_api(3)
    )
    for r in resultados:
        print(r)

asyncio.run(main_zoho())