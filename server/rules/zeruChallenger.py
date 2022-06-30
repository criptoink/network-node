from shared.modules.database import get_node_in_connections_list, get_node_out_connections_list, get_node_forbidden_connections_list

class ZeruChallenger:
    def __init__(self, request_data):
        self.request = request_data
        self.host_is_valid = False
        self.host_at_forbidde_list = True
        self.host_at_in_list = False
        self.host_at_out_list = False
        self.host_is_verified = False

    def validate_host(self):
        # Impeditivo
        # Valida se o host informado no who-i-am é o mesmo informado no Request     
         self.valid_host = True

    def validade_host_forbidde_list(self):
        # Impeditivo
        # Valida se o host informado esta na lista de nós que estão proibidos
        self.host_at_forbidde_list =  False
    
    def validade_host_in_list(self):
        # Valida se o host informado esta na lista de nós que já enviam dados
        self.host_at_in_list = True

    def validade_host_out_list(self):
        # Valida se o host informado esta na lista de nós que já recebem dados
        self.host_at_out_list = True

    def validate_host_in_neighborhood(self):
        # Valida se o host é acessivel a partir de outro nó e se as informações são as mesmas do who-i-am
        # Opcional: O Nó consultado pode enviar se o host pesquisado está em alguma de suas listas
        self.host_is_verified = True



