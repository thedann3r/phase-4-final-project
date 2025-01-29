from faker import Faker
from random import randint, choice
from models import Planes, PlaneCompany, PlanesOwners, Owners, db
from app import app

fake = Faker()
with app.app_context():
    
    Planes.query.delete()
    PlaneCompany.query.delete()
    PlanesOwners.query.delete()
    Owners.query.delete()
    
    planenames = ["Boeing 747", "Airbus A380", "Concorde", "Lockheed Martin F-22 Raptor", "Cessna 172", "P-51 Mustang", "Boeing 787 Dreamliner", "McDonnell Douglas F-15 Eagle", "Airbus A320", "Lockheed C-130 Hercules"]
    companies = ["Boeing", "Airbus", "Lockheed Martin", "McDonnell Douglas", "Bombardier", "Embraer", "Northrop Grumman", "Sukhoi", "Dassault Aviation"]
    own = ["Air Combat", "Transport & Logistics", "Search and Rescue", "Reconnaissance & Surveillance", "Air Refueling", "Training & Simulation"]

    for company_name in companies:
        # Check if company already exists
        if not PlaneCompany.query.filter_by(name=company_name).first():
            company_instance = PlaneCompany(
                name=company_name,
                founded=fake.date()
            )
            db.session.add(company_instance)

    for _ in range(10):
        plane = Planes(
            name=choice(planenames),
            planeCompany_id=choice(range(10))
        )
        db.session.add(plane)

    for _ in range(6):
        owner = Owners(
            name=choice(own)
        )
        db.session.add(owner)

    for _ in range(10):
        planeowner = PlanesOwners(
            planes_id=choice(range(10)),  
            owners_id=choice(range(6))  
        )
        db.session.add(planeowner)

    db.session.commit()
    print("Seeding complete!")
