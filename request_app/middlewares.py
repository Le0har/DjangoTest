from django.http import HttpRequest


def set_useragent_middleware(get_response):
    print('запуск middleware')

    def middleware(request):
        print('до запроса')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('после запроса')
        return response
    
    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exeptions_cont = 0

    def __call__(self, request):
        self.requests_count += 1
        # print('Количество запросов =', self.requests_count)
        response = self.get_response(request)
        self.response_count += 1
        # print('Количество ответов =', self.response_count)
        return response
    
    def process_exception(self, request, exeption):
        self.exeptions_cont += 1
        # print('Получили', self.exeptions_cont, 'ошибок')


def throttling_middleware(get_response):
    print('запуск middleware частота запросов')

    def middleware(request):
        # print('до запроса частоты')
        user_ip = request.META.get('REMOTE_ADDR')
        response = get_response(request)
        # print('IP:', user_ip)
        # print('после запроса частоты')
        return response
    
    return middleware
