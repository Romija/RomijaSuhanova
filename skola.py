def noteikt_izglitibu(gadi_skola, gadi_darba,diploms):
    if diploms=='bakalaurs' and gadi_skola>=4 and gadi_darba>=2:
        print('Tev ir ok izglītība un darba pieredze')
    elif diploms=='magistrs' and gadi_skola>=6 and gadi_darba>=4:
        print('Darba devējam patiks Tava bagāža.')
    else:
        print('Ieteicams uzkrāt pieredzi.')

skolas_gadi=float(input('Cik gadus esi mācījies?'))
darba_gadi=float(input('Cik gadus esi strādājis savā jomā? '))
izg_limenis=input('Kāds ir Tavs izglītības līmenis?(bakalaurs/magistrs)')

noteikt_izglitibu(skolas_gadi,darba_gadi,izg_limenis)