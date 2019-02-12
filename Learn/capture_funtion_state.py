def nest(volume,text):
    def bell():
        return text.lower() + 'bell'
    def hell():
        return text.upper() + 'hell'

    if(volume > 5):
        return bell
    else:
        return hell

result = nest(0,"It is ")
print(result())
