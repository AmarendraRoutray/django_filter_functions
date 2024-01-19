from django import template

register = template.Library()


@register.filter()      # using decorator arg is not mandatory it automatically takes function name
def swap(value):
    return value.swapcase()

# register.filter('swap',swap)

@register.filter()     
def remove(value,arg):
    
    return value.lower().replace(arg.lower(),'')

# register.filter('remove',remove)

@register.filter()
def counting(value,arg):
    c = 0
    for ind in range(len(value)):
        if arg == value[ind:len(arg)+ind:1]:
            c += 1
    return c