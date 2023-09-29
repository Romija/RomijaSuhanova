laiks = (input('Vai pie Jums atrodas laikā nenodots izdevums?')) #pārbauda vai var izsniegt vispār izdevumus

if laiks == 'jā': #ja mainīgais "laiks" ir jā, tad nevar izsniegt grāmatu
    print('Nevar izsniegt izdevumu')
elif laiks == 'nē': #ja mainīgais "laiks" ir nē, tad uzdod tālāk jautājumus
    pieprasitais = (input('Vai izdevums ir pieprasīto izdevumu sarakstā(tad rakstiet "jā"), parasta grāmata(rakstiet grāmata) vai žurnāls(rakstiet žurnāls)?'))
    #pārbauda vai pieprasīto uzdevumu sarakstā, un vai tā ir grāmata vai žurnāls
    if pieprasitais == 'žurnāls': #ja lietotājs ievada vārdu žurnāls, tad pasaka, ka var ņemt tikai  uz 7dienām
        print('Varat saņemt uz 7dienām')
    if pieprasitais == 'jā': # ja lietotājs ievada vārdu jā, tad var izsniegt tikai uz 2 dienām
        print('Varat saņemt uz 2 dienām')
    elif pieprasitais == 'grāmata': #ja tā ir grāmata, tad tālāk prasa vai personāls vai students
        personals = (input('Esat personāls vai students?'))
        if personals == 'personāls': #personālam uz 28 dienām var izsniegt
            print('Varat saņemt izdevumu uz 28 dienām')
        if personals == 'students': #studentim tikai uz 14dienām
            print('Varat saņemt izdevumu uz 14 dienām')
else:
    print('Nav ievadīts korekti')   #ja lietotājs neievadīja prasītos vārdus korekti, tad parādas šis print 

