#TIK TAK TOE DOCUMENT <br>
Este es un ejemplo de 5 hs de trabajo haciendo un tateti en una aplicacion rest echa en python y 
un cliente en spring boot basico que lo consume con rest template
# Endpoints
[POST] env-/game/tiktaktoe/create/<GameId>/<Player>
[PUT]  env-/game/tiktaktoe/play/<GameId>/<row>/<col>
[GET]  env-/game/tiktaktoe/history
[DEL]  env-/game/tiktaktoe/<GameId>

#Features
- [x] Crea diferentes juegos y guarda el tiempo
- [x] Habilidad para seleccionar un casillero
- [x] Valida si el lugar selecionado esta ocupado o no
- [x] Informacion historica de las partidas
- [x] Borrar partida
- [x] Movimiento automatico de la computadora
- [x] Detecta cuando termina el juego y quien gano
- [x] El movimiento de la maquina no pisa casilleros de la pc o el jugador
- [x] Codigos de respuesta apropiados
- [ ] Refactor Code
- [ ] Unit Test
- [ ] Consumir el serivico mediandte una app en spring boot
 
#Tecnologias
Java TBD
	SpringBoot
	RestTemplate
	
Python
	Flask
	pymongo
	
Mongodb	
