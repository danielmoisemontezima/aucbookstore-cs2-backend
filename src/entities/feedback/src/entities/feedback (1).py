#author :Sebastien_germina 

"""
=============================================================================
COUCHE 1 : ENTITÉS — Feedback
=============================================================================

Ce qui vit ici :
    Objet métier représentant un avis client sur une commande.

La règle d'or :
    Feedback ne connaît RIEN des bases de données, des API ou des frameworks.
    C'est de la logique métier pure, avec ses validations.

Règles métier encodées ici :
    1. Un feedback peut être dans trois états : EN_ATTENTE, APPROUVÉ, REJETÉ.
    2. Seul un feedback en attente peut être approuvé ou rejeté.
    3. Une fois approuvé ou rejeté, on ne peut pas revenir en arrière
       (décision métier – à adapter si besoin).
    4. Un feedback appartient toujours à une commande existante (order_id obligatoire).
    5. Le commentaire est facultatif mais doit être une chaîne si fourni.

Quand cette entité change-t-elle ?
    Quand les règles métier autour du traitement des avis évoluent.
=============================================================================
"""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import uuid

# ------------------------------------------------------------
# IMPORT DEPUIS L'ENTITÉ ORDER (Value Object OrderId)
# ------------------------------------------------------------
# On importe uniquement le type identifiant, pas l'entité complète.
# Cela respecte la règle DDD : un agrégat référence un autre agrégat
# par son identifiant, pas par une référence objet.
#from order import OrderId 
  # <--- À adapter selon votre structure de dossiers
# ------------------------------------------------------------


def _now() -> datetime:
    """Retourne la date/heure UTC courante."""
    return datetime.now(timezone.utc)


class FeedbackStatus(Enum):
    """
    États possibles d'un Feedback dans notre domaine métier.

    C'est un concept métier – pas un enum de base de données ni une chaîne d'API.
    Il exprime ce qu'un feedback PEUT être, défini par le métier.
    """
    PENDING = "pending"      
    APPROVED = "approved"    
    REJECTED = "rejected"    


@dataclass(kw_only=True)   # Force les paramètres nommés pour plus de clarté
class Feedback:
    """
    Avis client sur une commande.

    Attributs :
        order_id   : Identifiant de la commande concernée (obligatoire).
                     Désormais ce n'est plus une chaîne, mais un OrderId (Value Object).
        comment    : Avis textuel optionnel.
        status     : État actuel du feedback (défaut : PENDING).
        feedback_id: Identifiant unique (auto-généré si non fourni).
        date_time  : Date de création (auto-initialisée à maintenant).
    """

    # --- Champs obligatoires --
    #order_id: OrderId          # Type fort au lieu de str  #commenté pour l'instant, car OrderId n'est pas défini dans ce contexte.
    comment: Optional[str] = None

  
    feedback_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: FeedbackStatus = field(default=FeedbackStatus.PENDING)
    date_time: datetime = field(default_factory=_now)

    def __post_init__(self) -> None:
        """
        Valide l'état de l'entité après initialisation.

        Lève :
            ValueError: Si un champ viole les règles métier.
        """
        # Vérification que order_id est bien un OrderId (si c'est une classe)
        #de comanté pour l'instant, car OrderId n'est pas défini dans ce contexte.
#        if not isinstance(self.order_id, OrderId):
#            raise ValueError("order_id doit être une instance de OrderId.")
        # Vérification du commentaire
        if self.comment is not None and not isinstance(self.comment, str):
            raise ValueError("comment doit être une chaîne de caractères ou None.")
        if not isinstance(self.date_time, datetime):
            raise ValueError("date_time doit être un objet datetime.")
        #  commentaire (si présent)
        if self.comment is not None:
            self.comment = self.comment.strip()

    # -------------------------------------------------------------------------
    # Comportement métier —  méthodes ENONCant les règles métier
    # -------------------------------------------------------------------------

    def approve(self) -> None:
        """
        Approuve le feedback.

        Règle métier : Seul un feedback en attente peut être approuvé.
        Une fois approuvé, il est considéré comme validé et ne peut plus être modifié.

        Lève :
            ValueError: Si le feedback n'est pas en attente.
        """
        if self.status != FeedbackStatus.PENDING:
            raise ValueError(
                f"Impossible d'approuver un feedback dont l'état est '{self.status.value}'. "
                "Seul un feedback en attente peut être approuvé."
            )
        self.status = FeedbackStatus.APPROVED

    def reject(self) -> None:
        """
        Rejette le feedback.

        Règle métier : Seul un feedback en attente peut être rejeté.
        Une fois rejeté, il est considéré comme invalide et ne peut plus être modifié.

        Lève :
            ValueError: Si le feedback n'est pas en attente.
        """
        if self.status != FeedbackStatus.PENDING:
            raise ValueError(
                f"Impossible de rejeter un feedback dont l'état est '{self.status.value}'. "
                "Seul un feedback en attente peut être rejeté."
            )
        self.status = FeedbackStatus.REJECTED

    def reset_to_pending(self) -> None:
        """
        Remet le feedback à l'état PENDING (en attente).

        Règle métier : Seul un feedback APPROUVÉ ou REJETÉ peut être réinitialisé.
        Utile pour des corrections administratives.

        Lève :
            ValueError: Si le feedback est déjà en attente.
        """
        if self.status == FeedbackStatus.PENDING:
            raise ValueError("Le feedback est déjà en attente.")
        self.status = FeedbackStatus.PENDING

    def update_comment(self, new_comment: Optional[str]) -> None:
        """
        Met à jour le commentaire du feedback.

        Règle métier : On ne peut pas modifier le commentaire si le feedback a déjà
        été APPROUVÉ ou REJETÉ — on le considère comme finalisé.

        Lève :
            ValueError: Si le feedback n'est pas en attente ou si new_comment est invalide.
        """
        if self.status != FeedbackStatus.PENDING:
            raise ValueError(
                f"Impossible de modifier le commentaire d'un feedback dont l'état est '{self.status.value}'. "
                "Seul un feedback en attente peut être modifié."
            )
        if new_comment is not None:
            if not isinstance(new_comment, str):
                raise ValueError("Le commentaire doit être une chaîne ou None.")
            new_comment = new_comment.strip()
        self.comment = new_comment

    # -------------------------------------------------------------------------
    # l'interrogation — des vérifications booléennes simples
    # -------------------------------------------------------------------------

    def is_pending(self) -> bool:
        """Retourne True si le feedback est encore en attente."""
        return self.status == FeedbackStatus.PENDING

    def is_approved(self) -> bool:
        """Retourne True si le feedback a été approuvé."""
        return self.status == FeedbackStatus.APPROVED

    def is_rejected(self) -> bool:
        """Retourne True si le feedback a été rejeté."""
        return self.status == FeedbackStatus.REJECTED