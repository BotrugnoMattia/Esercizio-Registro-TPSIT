class Studente:
    """Rappresenta un singolo studente con anagrafica e classificazione scolastica."""

    def __init__(self, nome, cognome, eta, citta):
        self._nome = nome
        self._cognome = cognome
        self._eta = eta
        self._citta = citta

    @property
    def nome(self):
        return self._nome

    @property
    def cognome(self):
        return self._cognome

    @property
    def eta(self):
        return self._eta

    @property
    def citta(self):
        return self._citta

    def get_ciclo_studi(self):
        """Classifica lo studente in base all'età (Biennio o Triennio)."""
        if self._eta in [14, 15]:
            return "Biennio"
        elif self._eta in [16, 17, 18, 19]:
            return "Triennio"
        else:
            return "Fuori corso / Non specificato"

    def __str__(self):
        return f"{self._cognome} {self._nome}, {self._eta} anni - Città: {self._citta} [{self.get_ciclo_studi()}]"