import requests

# Prueba método Pagar 
url_pagar = "http://localhost:5000/pagar"
datos_pago = {
    "numero_tarjeta": 123456789,
    "monto": 1000,
    "nombre": "Juan Perez",
    "codigo_CVV": 456
}

respuesta_pago = requests.post(url_pagar, json=datos_pago)
if respuesta_pago.status_code == 200 and respuesta_pago.json().get("resultado") is True:
    print("TRANSACCIÓN EXITOSA")
else:
    print("FALLÓ LA TRANSACCIÓN")

# Prueba método Comprar 
url_comprar = "http://localhost:5000/comprar"
datos_compra = {
    "id_producto": 101,
    "precio": 250,
    "numero_productos": 4,
    "total": 1000
}

respuesta_compra = requests.post(url_comprar, json=datos_compra)
if respuesta_compra.status_code == 200 and respuesta_compra.json().get("resultado") is True:
    print("COMPRA EXITOSA")
else:
    print("FALLÓ LA COMPRA")
