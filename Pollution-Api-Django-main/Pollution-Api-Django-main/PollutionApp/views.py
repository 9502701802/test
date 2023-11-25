from django.shortcuts import render
from . import services
def home(request):
    return render(request, 'homepage.html')


def pollution(request):
    if request.method == 'POST':
        query = request.POST['query']
        code, response = services.get_data(query)
        flag = True if code == 200 else False
        data = {}
        if flag :
            data = response['stations'][0]
        data.update({'flag' : flag, 'city' : query})
        print(code)
        print(data)
        return render(request, 'pollution.html', data)
    else:
        return render(request, 'pollution.html')
