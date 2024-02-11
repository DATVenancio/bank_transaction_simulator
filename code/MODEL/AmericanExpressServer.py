from BankNetworkServer import BankNetworkServer
class AmericanExpressServer(BankNetworkServer):
    def __init__(self):
        super().__init__()
        self._initial_server_configuration()
        self._connect_db()
        self._create_api_routes()
        
        pass
    def _initial_server_configuration(self):
        #db
        self.db_host="localhost"
        self.db_user="daniel"
        self.db_passwd="daniel"
        self.db_name="public_database"

        #api
        self.api_host="localhost"
        self.api_port=5011

server=AmericanExpressServer()