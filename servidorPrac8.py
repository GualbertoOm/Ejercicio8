from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/pagar", methods=["GET"])
def pagar():
    try:
        numero_tarjeta = int(request.args.get("numero_tarjeta"))
        monto = float(request.args.get("monto"))
        nombre = request.args.get("nombre")
        codigo_CVV = int(request.args.get("codigo_CVV"))

        if monto <= 5000:
            return jsonify({"resultado": True, "mensaje": "TRANSACCIÓN EXITOSA"})
        else:
            return jsonify({"resultado": False, "mensaje": "FALLÓ LA TRANSACCIÓN (Fondos insuficientes)"})
    except:
        return jsonify({"resultado": False, "mensaje": "Datos inválidos"}), 400

@app.route("/comprar", methods=["GET"])
def comprar():
    try:
        id_producto = int(request.args.get("id_producto"))
        precio = float(request.args.get("precio"))
        numero_productos = int(request.args.get("numero_productos"))
        total = float(request.args.get("total"))

        if precio * numero_productos == total:
            return jsonify({"resultado": True, "mensaje": "COMPRA EXITOSA"})
        else:
            return jsonify({"resultado": False, "mensaje": "FALLÓ LA COMPRA (Total incorrecto)"})
    except:
        return jsonify({"resultado": False, "mensaje": "Datos inválidos"}), 400

if __name__ == "__main__":
    app.run(port=5000)
