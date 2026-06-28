#AUC bookstore system
**Version enrichie du projet de systeme de gestion et de vente pour le bookstore de l'AUC**

1.**Contexte et problematique**
Le bookstore de l’AUC rencontre fréquemment des difficultés liées à la gestion des commandes, aux longues files d’attente, aux heures de pause, aux jours fériés et à l’accès limité aux services. Afin d’améliorer l’expérience des étudiants et des clients particuliers, ce projet vise à développer une application mobile moderne permettant la gestion des commandes, des stocks, des paiements et des livraisons.

2.**Objectifs du Projet**
Réduire les files d’attente.
Permettre la réservation et les commandes en ligne.
Faciliter la gestion des stocks.
Automatiser le suivi des commandes.
Moderniser les services du bookstore.
Améliorer l’accessibilité des produits et services.

3.**Utilisateurs du Système**
Administrateurs
Employés
Clients
Livreurs

4.**Fonctionnalités Principales**
4.1 *Côté Client*
Inscription et connexion
Catalogue de produits et services
Recherche avancée
Panier et commandes
Réservation de produits
Paiements mobiles et électroniques
Suivi des commandes
Avis et commentaires
Notifications

4.2 *Côté Administrateur*
Gestion du catalogue
Gestion des catégories
Gestion des stocks
Gestion des utilisateurs
Gestion des paiements
Gestion des commandes
Statistiques des ventes

5.**Technologies Utilisées**
*Composant*                     *Technologie*
 Frontend                        Flutter / Dart
 Backend                         Node.js / Express
 Base de données                 PostgreSQL
 Versioning                      Git & GitHub
 Déploiement                     Render / Railway / VPS

6.**Architecture du Système**
Le système adoptera une architecture client-serveur moderne.

Application Mobile Flutter       
         ↓
API REST Node.js / Express    
         ↓
Base de Données PostgreSQL

  **Structure directory**

AUC-BOOKSTORE/
│
├── frontend/
│   ├── lib/
│   │   ├── screens/
│   │   │   ├── auth/
│   │   │   ├── home/
│   │   │   ├── products/
│   │   │   ├── cart/
│   │   │   ├── orders/
│   │   │   └── profile/
│   │   │
│   │   ├── widgets/
│   │   │   ├── buttons/
│   │   │   ├── cards/
│   │   │   ├── dialogs/
│   │   │   └── navigation/
│   │   │
│   │   ├── services/
│   │   │   ├── api_service.dart
│   │   │   ├── auth_service.dart
│   │   │   └── payment_service.dart
│   │   │
│   │   ├── models/
│   │   │   ├── user_model.dart
│   │   │   ├── product_model.dart
│   │   │   ├── order_model.dart
│   │   │   └── payment_model.dart
│   │   │
│   │   ├── providers/
│   │   │   ├── auth_provider.dart
│   │   │   ├── cart_provider.dart
│   │   │   └── order_provider.dart
│   │   │
│   │   ├── utils/
│   │   │   ├── constants.dart
│   │   │   ├── validators.dart
│   │   │   └── helpers.dart
│   │   │
│   │   └── main.dart
│   │
│   ├── assets/
│   │   ├── images/
│   │   ├── icons/
│   │   └── fonts/
│   │
│   └── pubspec.yaml
│
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   │   ├── authController.js
│   │   │   ├── productController.js
│   │   │   ├── orderController.js
│   │   │   └── paymentController.js
│   │   │
│   │   ├── routes/
│   │   │   ├── authRoutes.js
│   │   │   ├── productRoutes.js
│   │   │   ├── orderRoutes.js
│   │   │   └── paymentRoutes.js
│   │   │
│   │   ├── middlewares/
│   │   │   ├── authMiddleware.js
│   │   │   ├── errorMiddleware.js
│   │   │   └── uploadMiddleware.js
│   │   │
│   │   ├── models/
│   │   │   ├── User.js
│   │   │   ├── Product.js
│   │   │   ├── Order.js
│   │   │   └── Payment.js
│   │   │
│   │   ├── services/
│   │   │   ├── paymentService.js
│   │   │   ├── emailService.js
│   │   │   └── notificationService.js
│   │   │
│   │   ├── config/
│   │   │   ├── db.js
│   │   │   ├── env.js
│   │   │   └── jwt.js
│   │   │
│   │   ├── utils/
│   │   │   ├── logger.js
│   │   │   └── validators.js
│   │   │
│   │   └── app.js
│   │
│   ├── uploads/
│   ├── tests/
│   └── package.json
│
├── database/
│   ├── migrations/
│   ├── seeders/
│   ├── backups/
│   └── schema.sql
│
├── docs/
│   ├── UML/
│   ├── API/
│   ├── reports/
│   └── presentation/
│
├── .env
├── .gitignore
├── README.md
├── docker-compose.yml
└── LICENSE

7.**Diagrammes UML Recommandés**
Use Case Diagram
Class Diagram
Activity Diagram
Sequence Diagram
Deployment Diagram

8.**Structure Prévisionnelle de la Base de Données**
**Users**
id
name
email
password
role

**Products**
id
title
price
stock
category_id

**Orders**
id
user_id
total
status

**Payments**
id
order_id
method
transaction_id

**Categories**
id
name

9.**MVP (Minimum Viable Product)**
Afin d’éviter une surcharge de développement, le projet sera divisé en plusieurs phases.

**Phase 1**
Authentification
Catalogue
Panier
Commandes
Gestion des stocks

**Phase 2**
Paiements en ligne
Notifications
Commentaires
Statistiques

**Phase 3**
Livraison
Tracking
Géolocalisation
Analytics avancés

10.**Organisation de l’Équipe**
MILLIEN Brightson Zigi – Project Lead
MARCELLO Germina – Documentation Manager
DIER Hendel Cado – Frontend Developer
MAILLARD Ridensky – Backend Developer
VAVAL Gaël – Tester

11.**Workflow Git Recommandé**
main : version stable
develop : développement principal
feature/* : nouvelles fonctionnalités
bugfix/* : corrections

12.**Sécurité du Système**
Authentification JWT
Hashage des mots de passe
Validation des données
Protection des APIs
Gestion des rôles et permissions

13.**Stratégie de Tests**
Tests unitaires
Tests fonctionnels
Tests UI/UX
Tests de sécurité
Tests responsive mobile

14.**Déploiement**
Le backend sera hébergé sur Render, Railway ou un VPS Ubuntu. La base de données PostgreSQL pourra être déployée via Supabase ou Neon. L’application mobile sera distribuée 
sous forme d’APK Android puis sur iOS.

15.**Conclusion**
Ce projet représente une solution numérique moderne destinée à améliorer les services du bookstore de l’AUC. Grâce à une architecture évolutive, une bonne organisation d’équipe et une planification progressive, le système pourra devenir une plateforme fiable et professionnelle.

