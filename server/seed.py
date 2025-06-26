#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Seed initial plants
    initial_plants = [
        Plant(name="Aloe", image="/images/aloe.jpg", price=11.50),
        Plant(name="ZZ Plant", image="/images/zz-plant.jpg", price=25.98),
        Plant(name="Pothos", image="/images/pothos.jpg", price=15.99),
        Plant(name="Snake Plant", image="/images/snake.jpg", price=29.99),
        Plant(name="Monstera", image="/images/monstera.jpg", price=35.50)
    ]

    db.session.bulk_save_objects(initial_plants)
    db.session.commit()
    print("🌱 Database seeded successfully with plants!")