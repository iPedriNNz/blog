from django import template

register = template.Library()


@register.filter(name='plural_coments')
def plural_coments(num_coments):
    try:
        num_coments = int(num_coments)

        if num_coments >= 2:
            return f'{num_coments} comentários'
        elif num_coments == 1:
            return f'{num_coments} comentário'
        else:
            return f'Nenhum comentário'
    except:
        return f'{num_coments} comentários'
