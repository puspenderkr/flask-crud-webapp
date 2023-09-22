import unittest
from flask import Flask, request, session
from flask_testing import TestCase
from website import create_app, db
from website.models import User

class AuthTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF protection for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an in-memory database for testing
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_signup(self):
        response = self.client.post('/sign-up', data={'email': 'test@example.com', 'firstName': 'Test', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Test')

    def test_login(self):
        user = User(email='test@example.com', first_name='Test', password='hashed_password')
        db.session.add(user)
        db.session.commit()
        response = self.client.post('/login', data={'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect upon successful login

    def test_logout(self):
        user = User(email='test@example.com', first_name='Test', password='hashed_password')
        db.session.add(user)
        db.session.commit()
        with self.client:
            self.client.post('/login', data={'email': 'test@example.com', 'password': 'testpassword'})
            response = self.client.get('/logout')
            self.assertEqual(response.status_code, 302)  # Expecting a redirect upon logout
            self.assertIsNone(session.get('user_id'))

if __name__ == '__main__':
    unittest.main()
