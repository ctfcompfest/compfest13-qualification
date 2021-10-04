from django import template

register = template.Library()

@register.filter(name='moneyfmt')
def money_format(value):
    ret = ""
    v_str = str(value)
    for i in range(len(v_str) - 1, -1, -3):
        ret = "," * (i - 3 >= 0) + v_str[max(i-2, 0) : i+1] + ret
    return ret