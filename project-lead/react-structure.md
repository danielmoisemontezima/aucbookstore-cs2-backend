# AUC Bookstore — Structure Frontend React
## Correction : Flutter → React (décision du professeur)

## Stack Confirmé
- Frontend  : React + Vite
- Backend   : Node.js / Express
- Database  : PostgreSQL
- Versioning: Git & GitHub

## Structure Frontend React

frontend/
  ├── src/
  │   ├── pages/
  │   │   ├── auth/
  │   │   │   ├── LoginPage.jsx
  │   │   │   └── RegisterPage.jsx
  │   │   ├── home/
  │   │   │   └── HomePage.jsx
  │   │   ├── products/
  │   │   │   ├── ProductsPage.jsx
  │   │   │   └── ProductDetailPage.jsx
  │   │   ├── cart/
  │   │   │   └── CartPage.jsx
  │   │   ├── orders/
  │   │   │   └── OrdersPage.jsx
  │   │   └── admin/
  │   │       └── AdminDashboard.jsx
  │   ├── components/
  │   │   ├── Navbar.jsx
  │   │   ├── BookCard.jsx
  │   │   └── CartItem.jsx
  │   ├── services/
  │   │   ├── api.js
  │   │   ├── auth.js
  │   │   └── payment.js
  │   ├── context/
  │   │   ├── AuthContext.jsx
  │   │   └── CartContext.jsx
  │   └── main.jsx
  ├── public/
  └── index.html

## Tables Base de Données Complètes

| Table       | Colonnes principales                              |
|-------------|---------------------------------------------------|
| Users       | id, name, email, password, role, created_at       |
| Products    | id, title, price, stock, category_id, created_at  |
| Categories  | id, name                                          |
| Orders      | id, user_id, total, status, created_at            |
| OrderItems  | id, order_id, product_id, quantity, price         |
| Cart        | id, user_id, product_id, quantity                 |
| Payments    | id, order_id, method, transaction_id              |
| Supplies    | id, name, price, stock, category_id               |

## Décision
Après consultation avec le professeur, le frontend
sera développé en React et non Flutter.
Le backend Node.js/Express reste inchangé.