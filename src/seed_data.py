"""
Script para poblar la base de datos con datos de ejemplo de StarWars
"""
from app import app, db
from models import Usuario, Planetas, Personajes

def seed_data():
    """Función para poblar la base de datos con datos de ejemplo"""
    
    with app.app_context():
        # Crear las tablas
        db.create_all()
        
        # Verificar si ya hay datos
        if Usuario.query.first() is not None:
            print("La base de datos ya contiene datos. Saltando el seeding...")
            return
        
        # Crear usuarios de ejemplo
        usuarios = [
            Usuario(username="luke_skywalker", password="force123"),
            Usuario(username="leia_organa", password="rebel123"),
            Usuario(username="han_solo", password="falcon123"),
        ]
        
        for usuario in usuarios:
            db.session.add(usuario)
        
        # Crear planetas de ejemplo
        planetas = [
            Planetas(
                nombre="Tatooine",
                clima="arid",
                poblacion="200000",
                diametro="10465",
                periodo_rotacion="23",
                periodo_orbital="304",
                gravedad="1 standard",
                terreno="desert",
                superficie_agua="1"
            ),
            Planetas(
                nombre="Alderaan",
                clima="temperate",
                poblacion="2000000000",
                diametro="12500",
                periodo_rotacion="24",
                periodo_orbital="364",
                gravedad="1 standard",
                terreno="grasslands, mountains",
                superficie_agua="40"
            ),
            Planetas(
                nombre="Yavin IV",
                clima="temperate, tropical",
                poblacion="1000",
                diametro="10200",
                periodo_rotacion="24",
                periodo_orbital="4818",
                gravedad="1 standard",
                terreno="jungle, rainforests",
                superficie_agua="8"
            ),
            Planetas(
                nombre="Hoth",
                clima="frozen",
                poblacion="unknown",
                diametro="7200",
                periodo_rotacion="23",
                periodo_orbital="549",
                gravedad="1.1 standard",
                terreno="tundra, ice caves, mountain ranges",
                superficie_agua="100"
            ),
            Planetas(
                nombre="Dagobah",
                clima="murky",
                poblacion="unknown",
                diametro="8900",
                periodo_rotacion="23",
                periodo_orbital="341",
                gravedad="N/A",
                terreno="swamp, jungles",
                superficie_agua="8"
            ),
            Planetas(
                nombre="Bespin",
                clima="temperate",
                poblacion="6000000",
                diametro="118000",
                periodo_rotacion="12",
                periodo_orbital="5110",
                gravedad="1.5 standard",
                terreno="gas giant",
                superficie_agua="0"
            ),
            Planetas(
                nombre="Endor",
                clima="temperate",
                poblacion="30000000",
                diametro="4900",
                periodo_rotacion="18",
                periodo_orbital="402",
                gravedad="0.85 standard",
                terreno="forests, mountains, lakes",
                superficie_agua="8"
            ),
            Planetas(
                nombre="Naboo",
                clima="temperate",
                poblacion="4500000000",
                diametro="12120",
                periodo_rotacion="26",
                periodo_orbital="312",
                gravedad="1 standard",
                terreno="grassy hills, swamps, forests, mountains",
                superficie_agua="12"
            ),
            Planetas(
                nombre="Coruscant",
                clima="temperate",
                poblacion="1000000000000",
                diametro="12240",
                periodo_rotacion="24",
                periodo_orbital="368",
                gravedad="1 standard",
                terreno="cityscape, mountains",
                superficie_agua="unknown"
            ),
            Planetas(
                nombre="Kamino",
                clima="temperate",
                poblacion="1000000000",
                diametro="19720",
                periodo_rotacion="27",
                periodo_orbital="463",
                gravedad="1 standard",
                terreno="ocean",
                superficie_agua="100"
            )
        ]
        
        for planeta in planetas:
            db.session.add(planeta)
        
        # Crear personajes de ejemplo
        personajes = [
            Personajes(
                nombre="Luke Skywalker",
                altura="172",
                peso="77",
                color_cabello="blond",
                color_piel="fair",
                color_ojos="blue",
                año_nacimiento="19BBY",
                genero="male"
            ),
            Personajes(
                nombre="C-3PO",
                altura="167",
                peso="75",
                color_cabello="n/a",
                color_piel="gold",
                color_ojos="yellow",
                año_nacimiento="112BBY",
                genero="n/a"
            ),
            Personajes(
                nombre="R2-D2",
                altura="96",
                peso="32",
                color_cabello="n/a",
                color_piel="white, blue",
                color_ojos="red",
                año_nacimiento="33BBY",
                genero="n/a"
            ),
            Personajes(
                nombre="Darth Vader",
                altura="202",
                peso="136",
                color_cabello="none",
                color_piel="white",
                color_ojos="yellow",
                año_nacimiento="41.9BBY",
                genero="male"
            ),
            Personajes(
                nombre="Leia Organa",
                altura="150",
                peso="49",
                color_cabello="brown",
                color_piel="light",
                color_ojos="brown",
                año_nacimiento="19BBY",
                genero="female"
            ),
            Personajes(
                nombre="Owen Lars",
                altura="178",
                peso="120",
                color_cabello="brown, grey",
                color_piel="light",
                color_ojos="blue",
                año_nacimiento="52BBY",
                genero="male"
            ),
            Personajes(
                nombre="Beru Whitesun lars",
                altura="165",
                peso="75",
                color_cabello="brown",
                color_piel="light",
                color_ojos="blue",
                año_nacimiento="47BBY",
                genero="female"
            ),
            Personajes(
                nombre="R5-D4",
                altura="97",
                peso="32",
                color_cabello="n/a",
                color_piel="white, red",
                color_ojos="red",
                año_nacimiento="unknown",
                genero="n/a"
            ),
            Personajes(
                nombre="Biggs Darklighter",
                altura="183",
                peso="84",
                color_cabello="black",
                color_piel="light",
                color_ojos="brown",
                año_nacimiento="24BBY",
                genero="male"
            ),
            Personajes(
                nombre="Obi-Wan Kenobi",
                altura="182",
                peso="77",
                color_cabello="auburn, white",
                color_piel="fair",
                color_ojos="blue-gray",
                año_nacimiento="57BBY",
                genero="male"
            ),
            Personajes(
                nombre="Anakin Skywalker",
                altura="188",
                peso="84",
                color_cabello="blond",
                color_piel="fair",
                color_ojos="blue",
                año_nacimiento="41.9BBY",
                genero="male"
            ),
            Personajes(
                nombre="Wilhuff Tarkin",
                altura="180",
                peso="unknown",
                color_cabello="auburn, grey",
                color_piel="fair",
                color_ojos="blue",
                año_nacimiento="64BBY",
                genero="male"
            ),
            Personajes(
                nombre="Chewbacca",
                altura="228",
                peso="112",
                color_cabello="brown",
                color_piel="unknown",
                color_ojos="blue",
                año_nacimiento="200BBY",
                genero="male"
            ),
            Personajes(
                nombre="Han Solo",
                altura="180",
                peso="80",
                color_cabello="brown",
                color_piel="fair",
                color_ojos="brown",
                año_nacimiento="29BBY",
                genero="male"
            ),
            Personajes(
                nombre="Greedo",
                altura="173",
                peso="74",
                color_cabello="n/a",
                color_piel="green",
                color_ojos="black",
                año_nacimiento="44BBY",
                genero="male"
            ),
            Personajes(
                nombre="Jabba Desilijic Tiure",
                altura="175",
                peso="1,358",
                color_cabello="n/a",
                color_piel="green-tan, brown",
                color_ojos="orange",
                año_nacimiento="600BBY",
                genero="hermaphrodite"
            ),
            Personajes(
                nombre="Wedge Antilles",
                altura="170",
                peso="77",
                color_cabello="brown",
                color_piel="fair",
                color_ojos="hazel",
                año_nacimiento="21BBY",
                genero="male"
            ),
            Personajes(
                nombre="Jek Tono Porkins",
                altura="180",
                peso="110",
                color_cabello="brown",
                color_piel="fair",
                color_ojos="blue",
                año_nacimiento="unknown",
                genero="male"
            ),
            Personajes(
                nombre="Yoda",
                altura="66",
                peso="17",
                color_cabello="white",
                color_piel="green",
                color_ojos="brown",
                año_nacimiento="896BBY",
                genero="male"
            ),
            Personajes(
                nombre="Palpatine",
                altura="170",
                peso="75",
                color_cabello="grey",
                color_piel="pale",
                color_ojos="yellow",
                año_nacimiento="82BBY",
                genero="male"
            )
        ]
        
        for personaje in personajes:
            db.session.add(personaje)
        
        # Confirmar los cambios
        db.session.commit()
        
        print("¡Base de datos poblada exitosamente!")
        print(f"- {len(usuarios)} usuarios creados")
        print(f"- {len(planetas)} planetas creados")
        print(f"- {len(personajes)} personajes creados")

if __name__ == "__main__":
    seed_data()