from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    get_param = request.GET.get('from-landing', '')
    if get_param == 'test':
        counter_click[get_param] += 1
    elif get_param == 'original':
        counter_click[get_param] += 1
    print('count click original', counter_click['original'])
    print('count click test', counter_click['test'])
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    get_param = request.GET.get('ab-test-arg', '')
    if get_param == 'test':
        counter_show[get_param] += 1
        print('cout-show test', counter_show['test'])
        print('cout-show original', counter_show['original'])
        return render(request, 'landing_alternate.html')

    counter_show[get_param] += 1

    print('cout-show test', counter_show['test'])
    print('cout-show original',counter_show['original'])
    return render(request, 'landing.html')


def stats(request):

    test_conversion = 0
    show_conversion = 0
    if counter_show['test'] != 0:
        test_conversion = (counter_click['test']/ counter_show['test']) * 1
    if counter_show['original'] != 0:
        show_conversion = (counter_click['original'] / counter_show['original']) * 1

    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': show_conversion,
    })
