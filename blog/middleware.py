from datetime import datetime

class CurrentYearMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_year = datetime.now().year
        request.current_year = current_year
        response = self.get_response(request)
        return response