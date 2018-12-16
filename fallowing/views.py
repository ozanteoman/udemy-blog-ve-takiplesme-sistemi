from django.http import HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, Http404
from .models import Fallowing
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def kullanici_modal_takip_et_cikar(request):
    response = sub_kullanici_takip_et_cikar(request)
    fallow_type = request.GET.get('fallow_type')
    owner = request.GET.get('owner')
    data = response.get('data')
    # fallowed = response.get('fallowed')
    # kendi profilimmiş gibi hareket ediyorum ve kendi takipçilerimi tekrardan çekiyorum
    my_fallowed = Fallowing.get_fallowed_username(user=request.user)
    if owner == request.user.username:
        takipci_ve_takip_edilen_sayisi = Fallowing.kullanici_takip_edilenler_ve_takipciler(request.user)
        context = {'user': request.user, 'takipciler': takipci_ve_takip_edilen_sayisi['takipciler'],
                   'takip_edilenler': takipci_ve_takip_edilen_sayisi['takip_edilenler']}
        html_render_takip_durum = render_to_string('auths/profile/include/fallowing/fallowing_partion.html',
                                                   context=context,
                                                   request=request)

        if fallow_type == "fallowed":
            # gelen kullanıcı takip edilenleri açtıysa takip edilenler sayfası açılıyor.
            fallowing = Fallowing.get_fallowed(user=request.user)
            fallowing = fallowers_and_fallowed_paginate(fallowing, 1)
            html = render_to_string('fallowing/profile/include/fallowing_fallowed_list.html', context={
                'fallowing': fallowing, 'my_fallowed': my_fallowed, 'fallow_type': fallow_type
            }, request=request)

            html_paginate = render_to_string('fallowing/profile/include/button_include/show_more_button.html',
                                             context={'username': request.user.username, 'fallowing': fallowing,
                                                      'fallow_type': fallow_type})

            data.update({'html': html, 'html_paginate': html_paginate})

        data.update({'fallow_type': fallow_type, 'html_takip_render': html_render_takip_durum, 'owner': True})
    else:
        data.update({'owner': False})
        # bu profil başkasına aitse demek oluyor
    return JsonResponse(data=data)


def kullanici_takip_et_cikar(request):
    response = sub_kullanici_takip_et_cikar(request)
    data = response.get('data')
    fallowed = response.get('fallowed')
    takipci_ve_takip_edilen_sayisi = Fallowing.kullanici_takip_edilenler_ve_takipciler(fallowed)
    context = {'user': fallowed, 'takipciler': takipci_ve_takip_edilen_sayisi['takipciler'],
               'takip_edilenler': takipci_ve_takip_edilen_sayisi['takip_edilenler']}
    html = render_to_string('auths/profile/include/fallowing/fallowing_partion.html', context=context, request=request)
    data.update({'html': html})
    return JsonResponse(data=data)


def kullanici_takip_et_cikar_for_post(request):
    data = {'html': ''}
    response = sub_kullanici_takip_et_cikar(request)
    takip_edilen_kullanici = response.get('fallowed')
    my_fallowed_user = Fallowing.get_fallowed_username(request.user)
    html = render_to_string('blog/include/favorite/favorite-user-obj.html', context={
        'user': takip_edilen_kullanici, 'my_fallowed_user': my_fallowed_user
    }, request=request)

    data.update({'html': html})
    return JsonResponse(data=data)


def sub_kullanici_takip_et_cikar(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    data = {'takip_durum': True, 'html': '', 'is_valid': True, 'msg': '<b>Takipten Çıkar</b>'}
    fallower_username = request.GET.get('fallower_username', None)
    fallowed_username = request.GET.get('fallowed_username', None)

    fallower = get_object_or_404(User, username=fallower_username)
    fallowed = get_object_or_404(User, username=fallowed_username)

    takip_ediyor_mu = Fallowing.kullaniciyi_takip_ediyor_mu(fallower=fallower, fallowed=fallowed)

    if not takip_ediyor_mu:
        Fallowing.kullanici_takip_et(fallower=fallower, fallowed=fallowed)
    else:
        Fallowing.kullanici_takipten_cikar(fallowed=fallowed, fallower=fallower)
        data.update({'msg': '<b>Takip Et</b>', 'takip_durum': False})
    return {'data': data, 'fallowed': fallowed}


def fallowed_or_fallowers_list(request, fallow_type):
    data = {'is_valid': True, 'html': ''}
    page = request.GET.get('page', 1)
    username = request.GET.get('username', None)
    if not username:
        raise Http404

    user = get_object_or_404(User, username=username)
    my_fallowed = Fallowing.get_fallowed_username(user=request.user)
    if fallow_type == 'fallowed':
        takip_edilenler = Fallowing.get_fallowed(user=user)
        takip_edilenler = fallowers_and_fallowed_paginate(queryset=takip_edilenler, page=page)
        html = render_to_string('fallowing/profile/include/fallowing_fallowed_list.html', context={
            'fallowing': takip_edilenler, 'my_fallowed': my_fallowed, 'fallow_type': fallow_type,
        }, request=request)

        html_paginate = render_to_string('fallowing/profile/include/button_include/show_more_button.html',
                                         context={'username': user.username, 'fallowing': takip_edilenler,
                                                  'fallow_type': fallow_type})

        # kullanıcın takip ettiği kişiler

    elif fallow_type == 'fallowers':
        # kullanıcıyı takip eden kişileri göster
        takipciler = Fallowing.get_fallowers(user=user)
        takipciler = fallowers_and_fallowed_paginate(queryset=takipciler, page=page)
        html = render_to_string('fallowing/profile/include/fallowing_fallowed_list.html', context={
            'fallowing': takipciler, 'fallow_type': fallow_type, 'my_fallowed': my_fallowed}, request=request)
        html_paginate = render_to_string('fallowing/profile/include/button_include/show_more_button.html',
                                         context={'username': user.username, 'fallowing': takipciler,
                                                  'fallow_type': fallow_type})
    else:
        raise Http404
    data.update({'html': html, 'html_paginate': html_paginate})
    return JsonResponse(data=data)


def fallowers_and_fallowed_paginate(queryset, page):
    paginator = Paginator(queryset, 1)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return queryset
