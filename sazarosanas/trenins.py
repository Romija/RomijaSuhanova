nenodots = input('Vai jums ir kāds laikā nenodots izdevums? (j/n): ')
if nenodots == 'j':
    print('Jūs nevarat saņemt izdevumu')
elif nenodots == 'n':
    pieprasits = input('Vai ir pieprasīts? (j/n)')
    if pieprasits == 'j':
        print('Izsniedz uz 2 dienām')
    elif pieprasits == 'n':
        zurnals = input('Vai publikācija ir žurnāls?')
        if zurnals == 'j':
            print('izsniedz uz 7diennām')
        elif zurnals == 'n':
            students = input('Vai jūs esat students?')
            if students == 'j':
                print('Izsniedz uz 14 dienām')
            elif students == 'n':
                print('Izsniedz uz 28dienam')

    