

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #before view

        request.my_var = 123
        response = self.get_response(request)
        response['X-MY-HEADER'] = 123

        # After view
        return response