def form(num):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = num
    valor_formatado = locale.currency(valor, grouping=True)
    return valor_formatado

