def nest(volume):
    def bell(text):
        return text.lower() + '...'
    def hell(text):
        return text.upper() + '...'

    if(volume > 5):
        return bell
    else:
        return hell

result = nest(0)
res = nest(6)
print(result," ....... ",res)

