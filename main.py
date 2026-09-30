import random
from Scuola import Scuola
from Studente import Studente


def popola_1000_studenti(scuola):
    """Popola la scuola con circa 1000 studenti generati casualmente."""
    nomi = ["Marco", "Sofia", "Luca", "Giulia", "Alessandro", "Martina", "Matteo", "Francesca", "Gabriele", "Chiara"]
    cognomi = ["Rossi", "Ferrari", "Russo", "Bianchi", "Romano", "Gallo", "Costa", "Fontana", "Conti", "Esposito"]
    citta_list = ["Roma", "Milano", "Napoli", "Torino", "Palermo", "Bologna", "Firenze", "Bari"]

    for _ in range(1000):
        nome = random.choice(nomi)
        cognome = random.choice(cognomi)
        eta = random.randint(14, 19)
        citta = random.choice(citta_list)

        scuola.aggiungi_studente(Studente(nome, cognome, eta, citta))


def menu_console():
    scuola = Scuola("ITIS Fermi")
    print("Inizializzazione e caricamento di 1000 studenti in corso...")
    popola_1000_studenti(scuola)
    print("Caricamento completato!\n")

    while True:
        print("=" * 45)
        print("          GESTIONALE SCUOLA - MENU          ")
        print("=" * 45)
        print("1. Mostra conteggio totale studenti")
        print("2. Aggiungi un nuovo studente")
        print("3. Cerca studenti per cognome")
        print("4. Cerca studenti per età")
        print("5. Esci")
        
        scelta = input("\nSeleziona un'opzione (1-5): ").strip()

        if scelta == "1":
            print(f"\n-> {scuola}")

        elif scelta == "2":
            print("\n--- Inserimento Nuovo Studente ---")
            nome = input("Nome: ").strip()
            cognome = input("Cognome: ").strip()
            try:
                eta = int(input("Età (14-19): "))
                citta = input("Città di residenza: ").strip()
                nuovo = Studente(nome, cognome, eta, citta)
                scuola.aggiungi_studente(nuovo)
                print(f"Studente aggiunto con successo: {nuovo}")
            except ValueError:
                print("Errore: l'età deve essere un numero intero!")

        elif scelta == "3":
            cognome_cercato = input("\nInserisci il cognome da cercare: ").strip()
            risultati = scuola.cerca_per_cognome(cognome_cercato)
            print(f"\nTrovati {len(risultati)} studenti:")
            for s in risultati[:10]:  # Mostra i primi 10 risultati
                print(f" - {s}")
            if len(risultati) > 10:
                print(f" ...e altri {len(risultati) - 10} studenti.")

        elif scelta == "4":
            try:
                eta_cercata = int(input("\nInserisci l'età da cercare: "))
                risultati = scuola.cerca_per_eta(eta_cercata)
                print(f"\nTrovati {len(risultati)} studenti di {eta_cercata} anni:")
                for s in risultati[:10]:
                    print(f" - {s}")
                if len(risultati) > 10:
                    print(f" ...e altri {len(risultati) - 10} studenti.")
            except ValueError:
                print("Errore: inserisci un numero valido per l'età!")

        elif scelta == "5":
            print("\nUscita dal programma. Arrivederci!")
            break
        else:
            print("\nOpzione non valida, riprova.")


if __name__ == "__main__":
    menu_console()