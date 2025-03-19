import logging


print("Hello, Git!") # 0

# Configuration de base des logs
logging.basicConfig(
    filename="app.log",  
    level=logging.INFO,  
    format="%(asctime)s - %(levelname)s - %(message)s",  
)

logging.info("Ceci est un log d'information.")
logging.warning("Attention ! Quelque chose pourrait mal tourner.")
logging.error("Erreur critique détectée !")

