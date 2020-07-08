### main ###
def main ():

    programkjorer=True
    while programkjorer:
        print()
        print ('For valg av operasjon: skriv inn en av følgende kommandoer:')
        print()
        print ("Registrer student: 1\nRegistrer emne: 2\nRegistrer eksamensresultat: 3\nSlett student: 4\nSkriv ut karakterliste: 5\nSkriv ut sensurliste: 6\nAvslutt program: 9")

        operasjon = input ('')

        #Meny for valg av funksjoner
        if operasjon == '1':
        	registrereStudent ()
        elif operasjon == '2':
        	registrereEmne ()
        elif operasjon == '3':
        	registrereEksamensresultat ()
        elif operasjon == '4':
        	slettStudent ()
        elif operasjon == '5':
        	karakterliste ()
        elif operasjon == '6':
        	sensurliste ()
        elif operasjon == '9':
        	programkjorer = False

    print ('Program avsluttet')

####################################################
### finnes x ###

def finnesStudent (student):
	"""returnerer True eller False basert på om studenten finnes"""
	studentfil = open ('Student10.txt', 'r')
	
	resultat = False
	for linje in studentfil:
		linje = linje.rstrip ('\n')

		if linje == student:
			resultat = True

	studentfil.close ()

	return resultat


def finnesEmne (emneNavn):
	"""returnerer True eller False basert på om emnet finnes"""
	emnefil = open ('Emne10.txt', 'r')
	
	resultat = False
	for linje in emnefil:
		linje = linje.rstrip ('\n')

		if linje == emneNavn:
			resultat = True

	emnefil.close ()

	return resultat

def finnesIeksamenRes (studentnr):
	"""Returnerer True eller False basert på om gitt studentnr eksisterer i eksamensresultat-filen"""
	eksamenfilen=open('Eksamensresultat10.txt','r')

	resultat=False
	for linje in eksamenfilen:
		linje=linje.rstrip('\n')

		if linje==studentnr:
			resultat=True

	eksamenfilen.close ()

	return resultat

def finnesEksamensresultat (studentnr, emnekode):
	"""returnerer True eller False basert på om eksamensresultat finnes på gitt studentnr og emnekode"""

	eksamenfil=open('Eksamensresultat10.txt','r')
	resultat=False

	linje = eksamenfil.readline ()

	while linje != '':
		linje = linje.rstrip('\n')

		if linje == emnekode:
			# Leser inn neste linje som studentnummer i eksamensfil
			filStudentnummer = eksamenfil.readline ()
			filStudentnummer = filStudentnummer.rstrip ('\n')

			if filStudentnummer == studentnr:
				resultat = True
		linje = eksamenfil.readline ()
	eksamenfil.close ()

	return resultat

####################################################
### slett ###
def slettStudent ():
	"""Slett student ved bruk av temp-fil"""

	#importerer os for å kunne erstatte original fil med tempfil
	import os
	print ('----- Kjører operasjon for sletting av student -----\n')
	studentnr = input ('Studentnummer: ')

	# Sjekk for om studenten finnes og om det er registrert eksamensresultat
	if finnesStudent (studentnr) == True and finnesIeksamenRes (studentnr) == False:
		print ('Starter sletting av student...')

		studentfil = open ('Student10.txt', 'r')
		tempfil = open ('tempfil.txt', 'w')

		linje = studentfil.readline ()
		# Leser gjennom studenfilen
		while linje != '':

			linje = linje.rstrip ('\n')
			# Skriver inn linjene, for student som ikke skal slettes, til temp-fil
			if linje != studentnr:
				filStudentnummer = (linje + '\n')
				filFornavn = studentfil.readline ()
				filEtternavn = studentfil.readline ()
				filStudium = studentfil.readline ()

				tempfil.write (filStudentnummer)
				tempfil.write (filFornavn)
				tempfil.write (filEtternavn)
				tempfil.write (filStudium)
			# Unnlater å skrive linjene for student som skal slettes til temp-fil
			else:
				filStudentnummer = (linje + '\n')
				filFornavn = studentfil.readline ()
				filEtternavn = studentfil.readline ()
				filStudium = studentfil.readline ()

			# Leser neste linje i fila, som da vil være neste studentnummer eller blank
			linje = studentfil.readline ()

		studentfil.close ()
		tempfil.close ()

		# Erstatter den originale Student10.txt-filen med tempfilen
		os.remove ('Student10.txt')
		os.rename ('tempfil.txt', 'Student10.txt')
		print ('Student fjernet!')


	elif finnesIeksamenRes (studentnr) == True:
		print ('Det er registrert eksamensresultat på denne studenten, studenten kan derfor ikke slettes')
	else:
		print ('Studenten du ønsker å slette finnes ikke')

####################################################
### Registrere x ###

def registrereStudent ():
	print ('----- Kjører operasjon for registrering av student -----\n')
	ny_student=True
	while ny_student==True:

		print()
		studentnr = input ('Studentnr: ')
	
		# Sjekker om studenten finnes, gir beskjed hvis den allerede er registrert
		if finnesStudent (studentnr) == False:
			studentFornavn = input ('Studentens fornavn: ')
			studentEtternavn = input ('Studentens etternavn: ')
			studieprogram = input ('Studieprogram: ')
			
			# Her skal studentens info legges inn i filen
			studentfil = open ('Student10.txt', 'a')

			studentfil.write (studentnr + '\n')
			studentfil.write (studentFornavn + '\n')
			studentfil.write (studentEtternavn + '\n')
			studentfil.write (studieprogram + '\n')

			studentfil.close ()
		else:
			print('Studenten eksisterer allerede!')
			print()
		print()
		svar=input('Registerer ny student? ')
		if svar=='nei' or svar=='Nei':
			ny_student=False

def registrereEmne ():
	print ('----- Kjører operasjon for registrering av emne -----\n')
	nytt_emne=True  #Legge til nytt emnenavn og emnekode.
	while nytt_emne==True:
		emnekode = input ('Emnekode: ')
		emnenavn = input ('Emnenavn: ')
		
		if  finnesEmne (emnenavn) ==False:
			Emnefil = open ('Emne10.txt', 'a')  #Åpner tekstfila.
			Emnefil.write (emnekode + '\n')     #Skriver inn i tekstfila.
			Emnefil.write (emnenavn + '\n')

			Emnefil.close ()  #Lukker tekstfila.
			
		print()
		svar=input('Registrere nytt emne? ')
		
		if svar=='Nei' or svar=='nei':  #Menyvalg for å legge til et emne eller gå til meny.
			nytt_emne=False

def registrereEksamensresultat ():
    # Funksjon for å registerere eksamensresultat
    print('--- kjører operasjon for registrering av eksamensresultat ---\n')
    
    # Det skal leses inn minst et eksamensresultat og skal forsette så lenge brukeren ønsker
    emnekode = input ('Emnekode: ')
    studentnr = input ('Studentnr: ')
    eksamensresultat = input ('Karakter: ')

    # Tester for å kunne gi brukeren beskjed om input finnes eller finnes ikke
    if finnesEmne (emnekode) ==False:
        print('Emnet eksisterer ikke!')
    if finnesStudent (studentnr) ==False:
        print('Studenten eksisterer ikke!')
    if finnesEksamensresultat (studentnr, emnekode) ==True:
        print('Karakter for student eksisterer allerede!')

    # Tester om eksamensresultat, studentnr og emnekode finnes fra før
    # Skriver ikke til filen om noen av testene ikke består
    if finnesEksamensresultat (studentnr, emnekode) ==False and finnesStudent (studentnr) ==True and finnesEmne (emnekode) ==True:
        Eksamensresultatfil = open ('Eksamensresultat10.txt', 'a')

        Eksamensresultatfil.write (emnekode + '\n')
        Eksamensresultatfil.write (studentnr + '\n')
        Eksamensresultatfil.write (eksamensresultat + '\n')
        Eksamensresultatfil.close ()

	
####################################################
### Utskrift ###

def karakterliste ():
	"""
	 skrive ut karakterliste for en student som inneholder studentopplysningene, 
	 hvilket studium studenten går på og alle oppnådde eksamensresultater med emnekode, 
	 emnenavn og karakter.
	"""
	print ('----- Kjører operasjon for print av Karakterliste -----\n')
	studentnr = input ('Studentnummer: ')

	# Første del finner og printer info på studenten
	if finnesStudent (studentnr) == True:
		studentfil = open ('Student10.txt','r')
		
		for linje in studentfil:
			linje = linje.rstrip ('\n')
			if linje == studentnr:
				fornavn = studentfil.readline ()
				etternavn = studentfil.readline ()
				studium = studentfil.readline ()

				fornavn = fornavn.rstrip ('\n')
				etternavn = etternavn.rstrip ('\n')
				studium = studium.rstrip ('\n')
		studentfil.close ()

		print ('Studentnummer:',studentnr,'Navn:',fornavn,etternavn,'Studium:',studium,) # denne må rettes på

		# Denne delen finner og printer alle eksamenskarakterer på studenten
		eksamenResFil = open ('Eksamensresultat10.txt', 'r')
		
		linje = eksamenResFil.readline ()
		while linje != '':
			filEmnekode = linje.rstrip ()
			filStudentnr = eksamenResFil.readline ()
			filKarakter = eksamenResFil.readline ()

			filStudentnr = filStudentnr.rstrip ('\n')
			filKarakter = filKarakter.rstrip ('\n')

			# sjekk for om lagret info, i variabler, er på ønsket student
			if filStudentnr == studentnr:
				emnenavn = finnEmnenavnMed (filEmnekode)

				print ('Emnenavn: ', emnenavn, 'Emnekode: ', filEmnekode, 'Karakter: ', filKarakter, '\n')
			linje = eksamenResFil.readline ()
			
		eksamenResFil.close ()

	else:
		print ('Studenten eksisterer ikke!')



def sensurliste ():
	"""
	skrive ut en sensurliste for et bestemt emne som inneholder emnekode og emnenavn, 
	og alle studenter med studentnr, fornavn, etternavn, studium og karakter.
	"""
	print ('----- Kjører operasjon for print av Sensurliste -----\n')

	emnekode = input ('Skriv inn emnekode: ')

	if finnesEmne (emnekode) == True:
		# Emnet finnes, derfor kan vi printe en sensurliste.
		emnenavn = finnEmnenavnMed (emnekode)

		print ('Sensurliste for Emne:', emnenavn,'Emnekode:',emnekode, '\n')

    	# Finn karakterinfo i eksamensresultatfilen og print hvert samlede resultat
		eksamenResFil = open ('Eksamensresultat10.txt', 'r')
		
		linje = eksamenResFil.readline ()
		while linje != '':
			linje = linje.rstrip ('\n')

			# Dersom nåværende linje samsvarer med søkt emnekoden; lagres info på kommende linjer i variabler til print
			if linje == emnekode:
				studentnr = eksamenResFil.readline ()
				karakter = eksamenResFil.readline ()
				studentnr = studentnr.rstrip ('\n')
				karakter = karakter.rstrip ('\n')
				
				print ('studentnummer: ', studentnr, 'karakter: ', karakter)

				studentfil = open ('Student10.txt', 'r')
				sfLinje = studentfil.readline ()
				
				# Denne delen søker etter utfyllende informasjon som ikke ligger i eksamensresultat-filen
				while sfLinje != '':
					sfLinje = sfLinje.rstrip ('\n')

					if sfLinje == studentnr:
						studentFornavn = studentfil.readline ()
						studentEtternavn = studentfil.readline ()
						studium = studentfil.readline ()

						studentFornavn = studentFornavn.rstrip ('\n')
						studentEtternavn = studentEtternavn.rstrip ('\n')
						studium = studium.rstrip ('\n')
						
						print ('student:', studentFornavn, studentEtternavn, 'Studium: ', studium, '\n')

					sfLinje = studentfil.readline ()
				studentfil.close ()

			linje = eksamenResFil.readline ()
		eksamenResFil.close ()
		
	else:
		print ('Emnet med emnekode "'+emnekode+'" finnes ikke.')

####################################################
### Tilleggsfunksjoner ###
def finnEmnenavnMed (emnekode):
	"""Finner emnenavnet fra emnefil, basert på gitt emnekode"""
	emnefil = open ('Emne10.txt','r')
	
	for linje in emnefil:
		linje = linje.rstrip ('\n')
		if linje == emnekode:
			emnenavn = emnefil.readline ()
			emnenavn = emnenavn.rstrip ('\n')
			emnefinnes = True

	emnefil.close ()

	if emnefinnes:
		return emnenavn
main ()
