##IProcesses
	Hva er prosess?
		Eksekveringen av et program, utføringen av instruksjonene
	Ved kjøringen av et program får vi tilstandsinformasjon
		Som for eksempel:
			ID, pekere til minneområder, tilstand, signaler, pekere til stacken, osv
		Det må lagres et sted, som er en del av prosessen.

##Process creation
	- En prosess kan lage en annen process ved hjelp av for eksempel fork().
		- lager en eksakt kopi av kallende prosess og fortsetter parallelt
		
	- Forskjellen på barneprosess og foreldreprosess er i returverdiene
		- Foreldre: barneprosess sin PID ved suksess, -1 ellers
		- Barn: 0 ved suksess, hvis ikke er det ikke en barneprosess

	- Andre måter å lage prosess kan være
		- clone(): deler
		- vfork():

##Process creation fork
	**Ganske hånd i hånd med process creation, punktene beskriver godt**

	**større skrift?**


##Program execution
	**Punktene forklarer godt**

	**større skrift her og?**

##Process waiting
	- For å få en prosess til å vente på en annen prosess kan vi bruke "pid_t wait(int *status) systemkall
		- Kallende prosess venter avhengig av variabel vi har
			- venter på hvilken som helst av barnenodene på å terminere (hvis det finnes)
	- Returnerer
		- -1 hvis ingen barneprosesser eksisterer
		- PID for terminert barneprosess og legger statusen i *status variabelen

##Process termination

	**Punktene sier alt som er nødvendig**

##Process states
    **Forklarer de ulike tilstandene**
	- Vi har en begrenset mengde ressurser, noen prosesser venter, noen kjører, noen venter på at andre skal kjøre.
	- Da har vi definerte tilstander for de forskjellige prosessene
		- Kjørende (running): utfører instruksjonene
		- Klar (ready): har ikke noe eksternt å vente på men er klare til å kjøre så fort de får tilgang til prosessen
		- Blokkert (blocked): venter på noe eksternt før man kan fortsette, for eksempel input.

    **Forklarer de ulike overgangene**	
	- Mellom tilstandene har vi definerte overganger
		- running -> blocked : prosess er blokkert for input
		- running -> ready : scheduler stopper prosessen
		- ready -> running : scheduler starter prosessen
		- blocked -> ready : ekstern hendelse ferdig, klar til å kjøre
		- ingenting -> ready: prosess blir opprettet
		- running -> ingenting: prosessen blir terminert

**Animasjonen viser et godt eksempel på tilstand og overgang, tenker det kan være hjelpsomt å forklare de først**


##Context switching
**Videoen som allerede er produsert på den er allerede bra, her er noen korte notater om det blir nødvendig**

	- Bytte fra en kjørende prosess til en annen
		1. slutt å kjøre prosess 1
		2. lagre tilstanden (registre, instruksjonspekere) til prosess 1 (oftest på stack eller pcb)
		3. Gjenopprette tilstanden til prosess 2, motsatt av punkt 2
		4. fortsette å kjøre prosess 2

	- Essensielt for multi-tasking systemer

	- Utfordringen er at det er dyrt å flytte på informasjonen fram og tilbake (overhead)
	
	- Årsaker til at det skjer
		- scheduler bytter prosess på grunn av algoritme og time slices
		- interrupts
		- bytte mellom user-mode og kernel-mode ved systemkall


##Processes vs threads
**Er dette nyttig å bruke tid på? Viser at det er billigere enn kontekst svitsjing**

	- Prosesser: gruppering av ressurser og eksekvering	
	
	- Tråder
		- oppnår flere kjørende enheter i samme prosess
		- deler mange ressurser (mest merkbart address space)
		
	- Bruker mindre tid å bytte mellom tråder enn å bytte mellom prosesser
	

##Example - multiple processes
**Ved å ha kode i forklaringen av de andre tingene, er det noe vi trenger å gjøre?**