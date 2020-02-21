from django.shortcuts import render, HttpResponse

# Create your views here.

class Main:
    def main_site(self, value1, value2):
        return HttpResponse(f'<h1>Hello World! A soma entre {value1} e {value2} = {value1 + value2}</h1>')
