from contact.models import ContactInfo


def subject_renderer(request):
    context = {
        'contact_info': ContactInfo.objects.first()
    }

    # if request.user.is_authenticated:
    #     context.update({
    #         'basket_order_count': ProductItem.objects.filter(user=request.user, status=0).count() or 0,
    #         'wish_list_count': WishList.objects.filter(user=request.user).first().product.count() if WishList.objects.filter(user=request.user).first() else 0
    #         })
    return context
