# myapp/middlware.py


def middleware_factory(a):
    def b(request):
        print('before get_reponse called')
        response = a(request)
        print('after get_reponse called')

        return response

    return b
