import easygui
while 1 == 1:
    ConversDirect = easygui.buttonbox ("Choose the conversion direction", choices = ['Fahr to Cels', 'Cels to Fahr'])
    if not ConversDirect: break
    if ConversDirect == 'Fahr to Cels':
        Fahr = float (easygui.enterbox ("Enter a temperature in Fahringeit to converse it to Celsius: "))
        Cels = 5 / 9 * ( Fahr - 32 )
        easygui.msgbox ("%.1f F is " % Fahr + "%.1f C" % Cels)
    elif ConversDirect == 'Cels to Fahr':
        Cels = float (easygui.enterbox ("Enter a temperature in Celsius to converse it to Fahringeit: "))
        Fahr = 9 / 5 * Cels + 32
        easygui.msgbox ("%.1f C is " % Cels + "%.1f F" % Fahr)
