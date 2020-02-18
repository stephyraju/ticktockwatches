from django import template
register = template.Library()
@register.filter
def is_user_in_fav(user, favourites):
    """[summary]
    :param user: [description]
    :type user: [type]
    :param favourites: ManyRelatedManager instance holding the Product.favourite relationship
    :type favourites: [ManyRelatedManager]
    :return: [description]
    :rtype: [type]
    """
    return user.id in list(map(lambda d: d.id, favourites.all()))