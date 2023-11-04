from django.shortcuts import render


def about(requests):
    teamplate = 'pages/about.html'
    return render(requests, teamplate)


def rules(requests):
    teamplate = 'pages/rules.html'
    return render(requests, teamplate)
