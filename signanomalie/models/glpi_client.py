from dotenv import load_dotenv
from .glpi_api import GLPI

class GLPI_CLIENT(GLPI):
    """
    Hérite de GLPI et utilise ses méthodes pour accéder aux données contenues dans la base de données de l'instance de GLPI

    Beaucoup de ces méthodes ne sont pas utilisées, mais servent d'exemple au fonctionnement de l'api GLPI et présentent des pistes pour des évolutions futures

    Les données récupérées sont celles de l'instance de glpi sur laquelle on initialise la session 
    """

    def __init__(self, url, apptoken, auth, verify_certs=True, use_headers=True):
        """
        Fait appel au super pour initier la session
        """
        super().__init__(url, apptoken, auth, verify_certs, use_headers)
        self.set_active_profile(4) # augmentation de privilèges
        self.priorite = {
            2 : "basse",
            1 : "normale",
            4 : "haute"
        }
        # permet de charger une seule fois la liste des lieux
        self.locations = self.get_locations()

    def get_user(self, id):
        """
        Retourne l'utilisateur qui correspond à l'id passé en paramètre
        """
        return self.get_item("User", 20)

    def get_ticket(self, id):
        """
        Retourne le ticket associé à l'id passé en paramètre
        """
        return self.get_item("Ticket", id)
    
    def get_user_id(self, firstname, realname):
        """
        Cherche dans la base de donnée l'utilisateur dont le prénom et nom correspondent à firstname et realname
        L'affichage est restreint à son ID
        """
        criteria = [{'field': 34, 'searchtype': 'contains', 'value': realname},
        {'field': 9, 'searchtype': 'contains', 'value': firstname}]
        forcedisplay = ["id"]
        return self.search('User', criteria = criteria, forcedisplay = forcedisplay)
    
    def get_ticket(self, ticket_user_id):
        """
        Retourne les tickets associées à un ticket user id
        """
        return self.get_sub_items("Ticket_user", ticket_user_id, "Ticket")
    
    def tickets_user(self, user_name):
        """
        Retourne les tickets d'un utilisateur identifié par son user_name
        """
        criteria = [{'field': 4, 'searchtype': 'equals', 'value': user_name}]
        forcedisplay = []
        return self.search('Ticket_user', criteria = criteria, forcedisplay = forcedisplay)

    def create_ticket(self, title, content, email, priority, location, device, notification):
        """
        title -> str : contient le titre du ticket
        content -> str : contient la description du ticket
        email -> str : contient l'adresse mail de suivi
        location -> int : contient l'id du lieux dans la base de données de glpi
        device -> int : contient l'id du matériel dans la base de données de glpi
        notification -> bool : si oui ou non l'utilisateur souhaite avoir des mails de suivi

        Ajoute un ticket dans la base de données de glpi avec les informations fournies
        """
        self.add("Ticket", 
                {"name" : self.locations.get(int(location)) + "  : " + title + " - " + device, 
                "content" : content,
                "urgency" : priority,
                "itilcategories_id" : 14, # Dépannage
                "locations_id" : location,
                "type" : 1,
                "_users_id_requester" : 0,
                "_users_id_requester_notif" : {
                    "use_notification" : notification, 
                    "alternative_email" : [email]
                    }
                }
            )
    
    def get_cateogory_names(self):
        """
        Retourne un dict contenant en clef les id des catégories et en valeur leurs noms
        """
        categories = self.get_all_items("ITILCategory")
        return {categorie["id"] : categorie["name"] for categorie in categories}
        
    def get_category_per_id(self, id):
        """
        Retourne une catégorie en fonction de son id
        """
        criteria = [{'field': 2, 'searchtype': 'contains', 'value': id}]
        forcedisplay = ["completename"]
        return self.search('ITILCategory', criteria = criteria, forcedisplay = forcedisplay)[0]["1"]
    
    def get_locations(self):
        """
        Retourne tous les lieux stockées dans la base de données de glpi 
        """
        locations = self.get_all_items("Location")
        return {location["id"] : location["name"] for location in locations}
    
    def get_computers_per_location(self, location_id):
        """
        Retourne tous les objets Computer d'un lieux identifié par son id sous forme d'un dict contenant en clef les id des ordinateurs et en valeur leurs noms
        """
        computers = self.get_sub_items("Location", location_id, "Computer")
        return { computers["id"] : computers["name"] for computers in computers }

    def get_printers_per_location(self, location_id):
        """
        Retourne tous les objets Printer d'un lieux identifié par son id sous forme d'un dict contenant en clef les id des imprimantes et en valeur leurs noms
        """
        printers = self.get_sub_items("Location", location_id, "Printer")
        return { printer["id"] : printer["name"] for printer in printers }

    def get_monitors_per_location(self, location_id):
        """
        Retourne tous les objets Monitor d'un lieux  identifié par son id sous forme d'un dict contenant en clef les id des écrans et en valeur leurs noms
        """
        monitors = self.get_sub_items("Location", location_id, "Monitor")
        return { monitor["id"] : monitor["name"] for monitor in monitors }

    def get_sub_locations(self, location_id):
        """
        Retourne tous les sous lieux d'un lieux identifié par son id sous forme d'un dict contenant en clef les id des lieux et en valeur leurs noms
        """
        locations = self.get_sub_items("Location", location_id, "Location")
        return { location["id"] : location["name"] for location in locations}

    def get_batiments(self):
        """
        Utilise self.locations pour chercher tous les bâtiments parmi les lieux : 
        Les bâtiments contiennent "Bâtiment" dans leur nom, convention faite par le service informatique
        Retourne un dict avec en clef l'id des lieux et en valeur leurs noms
        """
        return {id_ : location for id_, location in self.locations.items() if "Bâtiment" in location}
