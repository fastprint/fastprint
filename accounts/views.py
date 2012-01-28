# -*- coding: utf-8 -*
from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from store.views import get_global_data, handle_uploaded_file
from accounts.models import Profile, Legal, Delivery
from accounts.forms import LoginForm, ProfileForm, LegalForm, DeliveryForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from store.send_html_mail import send_html_mail
import md5

@render_to('login.html')
def signlogup(request):
    data = get_global_data(request)
    data['message'] = False
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    request.session.set_expiry(60*60*24*365)
                    login(request, user)
                    return HttpResponseRedirect('/profile/')

                else:
                    data['message'] = 'Эккаунт заблокирован'
            else:
                data['message'] = 'Неправильная пара логин/пароль'

        elif 'username' in request.POST:
            username = request.POST['username']
            try:
                user = User.objects.create_user(username, username, username)
                user.is_active = False
                user.is_staff = False
                activate_code = md5.new(username).hexdigest()
                send_html_mail('Activation letter', username, {'name': username, 'code': activate_code}, 'emails/activate_letter.html', sender='web@fastprint.info')
                user.save()
                profile = Profile(user = user, phone = '+7 ')
                profile.save()
                return { 'message': 'Спасибо за регистрацию. Вам выслано письмо с инструкциями по активации эккаунта.' }
            except:
                if User.objects.get(username=username) is not None:
                    data['message'] = 'Пользователь с таким e-mail уже зарегистрирован'
                else:
                    data['message'] = 'Неизвестная ошибка при добавлении пользователя. Обратитесь в поддержку'

    else:
        form = LoginForm()

    data['login_form'] = form
    return data

def kickout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def confirm_email(request, username, code):
    try:
        user = User.objects.get(username = username)
        if user.username == username and md5.new(username).hexdigest() == code:
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/activate/complite/')
        return HttpResponseRedirect('/activate/failed/')
    except:
        return HttpResponseRedirect('/activate/failed/')

@login_required
def update(request):
    '''
    Данная функция отвечает за обноление всех данных о пользователе: Профиль, Юр. данные, Инф. о доставке.
    Она принимает на вход всего 1 форму и в зависимости от параметров расбрасывает эти данные в набор моделей.
    '''
    if request.method == 'POST': # Если пришли данные от формы
        form = ProfileForm(request.POST, request.FILES) # Создадним экземпляр формы
        if form.is_valid(): # Если все данные введены корректно...
            # Если произошли изменения в модели пользователя
            user = User.objects.get(id=request.user.id)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            
            # Если произошли изменения в модели профиля
            profile = Profile.objects.get(user=user)
            profile.phone = form.cleaned_data['phone']
            is_legal = int(form.cleaned_data['is_legal'])
            # Подгрузка аватарки на сервер
            try:
                profile.img = handle_uploaded_file(request.FILES['img'], 'user_pic')
            except:
                pass
            # Проверка, является ли пользователь юр.лицом
            if is_legal == 0:
                profile.is_legal = False
            else:
                profile.is_legal = True
            profile.save()

            # Если пользователь становится юр.лицом, необходимо сохранить в базе его юридические данные
            form = LegalForm(request.POST)
            if form.is_valid():
                try:
                    legal = Legal.objects.get(profile=profile)
                    legal.title = form.cleaned_data['legal_name']
                    legal.inn = form.cleaned_data['inn']
                    legal.kpp = form.cleaned_data['kpp']
                    legal.bik = form.cleaned_data['bik']
                    legal.rs = int(form.cleaned_data['rs'])
                    legal.ks = int(form.cleaned_data['ks'])
                    legal.post = form.cleaned_data['post']
                except:
                    legal = Legal(
                        profile = profile,
                        title = form.cleaned_data['legal_name'],
                        inn = form.cleaned_data['inn'],
                        kpp = form.cleaned_data['kpp'],
                        bik = form.cleaned_data['bik'],
                        rs = int(form.cleaned_data['rs']),
                        ks = int(form.cleaned_data['ks']),
                        post = form.cleaned_data['post'],
                    )
                legal.save()

            # Если пользователь вводит свои данные по доставке
            form = DeliveryForm(request.POST)
            if form.is_valid():
                try:
                    delivery = Delivery.objects.get(profile=profile)
                    delivery.title = form.cleaned_data['delivery_name']
                    delivery.address = form.cleaned_data['address']
                    delivery.city = form.cleaned_data['city']
                except:
                    delivery = Delivery(
                        profile = profile,
                        title = form.cleaned_data['delivery_name'],
                        address = form.cleaned_data['address'],
                        city = form.cleaned_data['city']
                    )
                delivery.save()


    return HttpResponseRedirect('/profile/')

@login_required
@render_to('profile.html')
def profile(request, *args):
    data = get_global_data(request)
    # Получаем данные профиля
    user = {
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
        'password':request.user.password,
    }
    profile = Profile.objects.get(user=request.user)
    if profile is not None:
        user['phone'] = profile.phone
        user['img'] = profile.img
        user['is_legal'] = profile.is_legal

    # Получаем данные ЮЛ
    try:
        legal = Legal.objects.get(profile=profile)
        if legal is not None:
            legal = {
                'legal_name': legal.title,
                'inn': legal.inn,
                'kpp': legal.kpp,
                'bik': legal.bik,
                'rs': legal.rs,
                'ks': legal.ks,
                'post': legal.post,
            }
    except:
        legal = {}

    # Получаем данные доставки
    try:
        delivery = Delivery.objects.get(profile=profile)
        if delivery is not None:
            delivery = {
                'delivery_name': delivery.title,
                'city': delivery.city,
                'address': delivery.address,
            }
    except:
        delivery = {}

    data['form_profile'] = ProfileForm(user)
    data['form_legal'] = LegalForm(legal)
    data['form_delivery'] = DeliveryForm(delivery)
    return data