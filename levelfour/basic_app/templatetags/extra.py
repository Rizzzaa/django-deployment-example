from django import template

register = template.Library()

# USE ONE OF THE WAY TO REGISTERr

# FIRST WAY TO REGISTER
@register.filter(name ='cut')
def cut (value, arg):
    """
    Tis cuts out all values of 'arg' form the string!
    """
    return value.replace(arg,'')


# SECOND WAY TO REGISTER
# register.filter('string', function)
register.filter('cut', cut)
