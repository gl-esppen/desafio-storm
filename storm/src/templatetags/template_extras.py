from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='join_hiperlink')
def join_hiperlink(queryset):
	conteudo = ''
	for key, value in enumerate(queryset):

		conteudo += '<a href="%s">%s</a>' % (value.get_absolute_url(), value.nome)
		if (len(queryset) - 1) != key:
			conteudo += ', '
			
	return mark_safe(conteudo)
