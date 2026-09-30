from Studente import Studente


class Scuola:
    """Gestisce il registro generale degli studenti e le operazioni di ricerca."""

    def __init__(self, nome="Istituto Superiore"):
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente):
        """Aggiunge uno studente al registro."""
        if isinstance(studente, Studente):
            self.studenti.append(studente)
        else:
            raise TypeError("L'oggetto deve essere un'istanza della classe Studente.")

    def cerca_per_cognome(self, cognome):
        """Restituisce tutti gli studenti con il cognome cercato."""
        return [s for s in self.studenti if cognome.lower() in s.cognome.lower()]

    def cerca_per_eta(self, eta):
        """Restituisce tutti gli studenti dell'età specificata."""
        return [s for s in self.studenti if s.eta == eta]

    def conteggio_studenti(self):
        """Restituisce il numero totale di studenti registrati."""
        return len(self.studenti)

    def __str__(self):
        return f"Scuola '{self.nome}' - Totale iscritti: {self.conteggio_studenti()}"