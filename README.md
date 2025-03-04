Reto CTF - Ingeniería Inversa 🔍

Bienvenido al Reto CTF SemanaHackhers. Tu misión es descifrar la flag escondida en el ejecutable cifrado con AES. ¡Demuestra tus habilidades de ingeniería inversa y criptografía! 💻✨

📌 Instrucciones

1-Descargar el reto
git clone https://github.com/Aldana222/SemanaHackhers_ctf
cd SemanaHackhers_ctf
O si prefieres descargar solo el binario:
wget https://github.com/Aldana222/SemanaHackhers_ctf/raw/main/dist/reto
chmod +x reto
./reto
2-Ejecutar el binario
./reto
3-Encuentra la flag y valídala! 🔑

🕵️ Hints (Pistas)

💡 Hint 1: Observa cómo se almacena la flag dentro del ejecutable, tal vez un desensamblador pueda ayudarte.

💡 Hint 2: El cifrado utilizado es AES en modo ECB, así que si logras encontrar la clave, podrás descifrar la flag.

💡 Hint 3: Herramientas como Ghidra, Radare2 o strings pueden ayudarte a extraer información valiosa del binario.

🏆 Objetivo

Encuentra la flag en el formato:
Hackhers{tu_respuesta_aqui}

Si crees haber encontrado la flag, introdúcela en el binario y verifica si es correcta. 
