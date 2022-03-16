from dotenv import load_dotenv
from .glpi_api import GLPI

class GLPI_CLIENT(GLPI):

    def __init__(self, url, apptoken, auth, verify_certs=True, use_headers=True):
        super().__init__(url, apptoken, auth, verify_certs, use_headers)
        self.set_active_profile(4)
        self.priorite = {
            2 : "basse",
            1 : "normale",
            4 : "haute"
        }
        self.update()

    def update(self):
        self.categories = self.get_cateogory_names()
        self.locations = self.get_locations()
        self.batiments = self.get_batiments()

    def get_user(self, id):
        return self.get_item("User", 20)

    def get_ticket(self, id):
        return self.get_item("Ticket", id)
    
    def get_user_id(self, firstname, realname):
        criteria = [{'field': 34, 'searchtype': 'contains', 'value': realname},
        {'field': 9, 'searchtype': 'contains', 'value': firstname}]
        forcedisplay = ["id"]
        return self.search('User', criteria = criteria, forcedisplay = forcedisplay)
    
    def get_ticket(self, ticket_user_id):
        return self.get_sub_items("Ticket_user", ticket_user_id, "Ticket")
    
    def tickets_user(self, user_name):
        criteria = [{'field': 4, 'searchtype': 'equals', 'value': user_name}]
        forcedisplay = []
        return self.search('Ticket_user', criteria = criteria, forcedisplay = forcedisplay)

    def create_ticket(self, title, content, email, priorite, categorie, location):
        self.add("Ticket", 
                {"name" : title, 
                "content" : content,
                "urgency" : priorite,
                "itilcategories_id" : self.categories.get(categorie),
                "locations_id" : self.locations.get(location),
                "type" : 1,
                "_users_id_requester" : 0,
                "_users_id_requester_notif" : {
                    "use_notification" : 1, 
                    "alternative_email" : [email]
                    }
                }
            )
    
    def get_cateogory_names(self):
        categories = self.get_all_items("ITILCategory")
        return {categorie["id"] : categorie["name"] for categorie in categories}
        
    def get_category_per_id(self, id):
        criteria = [{'field': 2, 'searchtype': 'contains', 'value': id}]
        forcedisplay = ["completename"]
        return self.search('ITILCategory', criteria = criteria, forcedisplay = forcedisplay)[0]["1"]
    
    def get_locations(self):
        locations = self.get_all_items("Location")
        return {location["id"] : location["name"] for location in locations}
    
    def get_computers_per_location(self, location_id):
        computers = self.get_sub_items("Location", location_id, "Computer")
        return { computers["id"] : computers["name"] for computers in computers }

    def get_sub_locations(self, location_id):
        locations = self.get_sub_items("Location", location_id, "Location")
        return { location["id"] : location["name"] for location in locations}

    def get_batiments(self):
        return {id_ : location for id_, location in self.locations.items() if "Bâtiment" in location}
