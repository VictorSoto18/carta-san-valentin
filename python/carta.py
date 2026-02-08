html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>San Valentín 💖</title>
    <style>
        body {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        .carta {
            background: white;
            padding: 30px;
            border-radius: 20px;
            width: 350px;
            text-align: center;
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
            position: relative;
        }

        h1 {
            color: #e63946;
        }

        p {
            font-size: 18px;
            color: #333;
        }

        button {
            margin: 10px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 10px;
            background: #e63946;
            color: white;
            cursor: pointer;
            position: relative;
            transition: all 0.2s;
        }

        button:hover {
            background: #d62828;
        }

        .corazon {
            font-size: 40px;
            display: inline-block;
            animation: latido 1s infinite;
        }

        @keyframes latido {
            0% { transform: scale(1); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }

        .corazon-enorme {
            font-size: 150px;
            display: block;
            margin: 20px auto;
            animation: latido 1s infinite;
        }

        #botones-si-no {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="carta">
    <div class="corazon">❤️</div>
    <h1>Feliz San Valentín</h1>
    <p id="mensaje">
        Tengo algo importante que preguntarte...
    </p>
    <!-- Botón original -->
    <button onclick="mostrarMensaje()">💌 Presiona aquí</button>
    
    <!-- Botones Sí/No se agregan dinámicamente -->
    <div id="botones-si-no"></div>
</div>

<script>
function mostrarMensaje() {
    document.getElementById("mensaje").innerHTML =
        "¿Quieres ser mi San Valentín? 💕🥰";

    // Crear botones Sí y No
    let contenedor = document.getElementById("botones-si-no");
    contenedor.innerHTML = `
        <button id="btn-si" onclick="presionarSi()">Sí 💕</button>
        <button id="btn-no">No 😢</button>
    `;

    // Agregar evento para que el botón No huya del mouse
    let btnNo = document.getElementById("btn-no");
    btnNo.addEventListener("mousemove", moverBoton);
    btnNo.addEventListener("click", moverBoton);
}

function presionarSi() {
    document.getElementById("mensaje").innerHTML = "¡Me alegra que digas Sí! ❤️";
    let corazon = document.createElement("div");
    corazon.className = "corazon-enorme";
    corazon.innerText = "❤️";
    document.querySelector(".carta").appendChild(corazon);

    // Ocultar los botones Sí/No
    document.getElementById("botones-si-no").style.display = "none";
}

function moverBoton(event) {
    let btnNo = event.target;
    let maxX = window.innerWidth - btnNo.offsetWidth - 20;
    let maxY = window.innerHeight - btnNo.offsetHeight - 20;
    let randX = Math.floor(Math.random() * maxX);
    let randY = Math.floor(Math.random() * maxY);

    btnNo.style.position = "absolute";
    btnNo.style.left = randX + "px";
    btnNo.style.top = randY + "px";
}
</script>

</body>
</html>
"""

with open("../html/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✨ Proyecto actualizado con botón No que huye al mouse. Abre html/index.html")
