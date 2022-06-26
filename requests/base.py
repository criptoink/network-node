class Base(request):
    def __init__(self, request):
        self.request = request.body
        self.host = request.host
        self.owner = request.owner
        self.response = None
        
