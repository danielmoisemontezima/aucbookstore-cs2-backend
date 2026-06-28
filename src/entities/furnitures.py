from enum import Enum


class StatutFourniture(Enum):
    DISPONIBLE = "Disponible"
    CRITIQUE = "Critique"
    EN_RUPTURE = "En rupture"


class Fourniture:
    def __init__(self, id: int, nom: str, description: str,
                 categorie: str, quantite_stock: int,
                 prix_unitaire: float, fournisseur: str,
                 seuil_alerte: int = 5):

        # Tout validasyon yo gwoupe nan yon sèl metòd
        self._valider(nom, prix_unitaire, quantite_stock, seuil_alerte)

        self.id = id
        self.nom: str = nom
        self.description = description
        self.categorie = categorie
        self.quantite_stock = quantite_stock
        self.prix_unitaire = prix_unitaire
        self.fournisseur = fournisseur
        self.seuil_alerte = seuil_alerte
        # Pa gen self.statut = ... isit la, paske 'statut' se yon @property
        # ki kalkile l otomatikman pi ba a, depi quantite_stock ak seuil_alerte.

    def _valider(self, nom: str, prix_unitaire: float,
                 quantite_stock: int, seuil_alerte: int) -> None:
        """Tout règ validasyon pou yon Fourniture."""
        if not nom.strip():
            raise ValueError("Le nom est obligatoire.")
        if prix_unitaire <= 0:
            raise ValueError("Le prix unitaire doit être positif.")
        if quantite_stock < 0:
            raise ValueError("La quantité en stock ne peut pas être négative.")
        if seuil_alerte < 0:
            raise ValueError("Le seuil d'alerte ne peut pas être négatif.")

    def ajouter_stock(self, quantite: int):
        if quantite <= 0:
            raise ValueError("La quantité à ajouter doit être supérieure à 0.")
        self.quantite_stock += quantite

    def retirer_stock(self, quantite: int):
        if quantite <= 0:
            raise ValueError("La quantité à retirer doit être supérieure à 0.")
        if quantite > self.quantite_stock:
            raise ValueError("Stock insuffisant.")
        self.quantite_stock -= quantite

    def est_en_stock_critique(self) -> bool:
        return self.quantite_stock <= self.seuil_alerte

    @property
    def statut(self) -> StatutFourniture:
        """Statut kalkile otomatikman selon kantite stock la."""
        if self.quantite_stock == 0:
            return StatutFourniture.EN_RUPTURE
        elif self.quantite_stock <= self.seuil_alerte:
            return StatutFourniture.CRITIQUE
        else:
            return StatutFourniture.DISPONIBLE

    def __str__(self):
        return (
            f"Fourniture(id={self.id}, nom='{self.nom}', "
            f"stock={self.quantite_stock}, "
            f"prix={self.prix_unitaire}, "
            f"statut={self.statut.value})"
        )


# Création d'un objet Fourniture
f = Fourniture(
    id=12,
    nom="Kaye",
    description="Pour prendre des notes",
    categorie="Papeterie",
    quantite_stock=20,
    prix_unitaire=1.50,
    fournisseur="Papeterie ABC",
    seuil_alerte=5
)
print(f)
