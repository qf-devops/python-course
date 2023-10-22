#!/usr/bin/env python3

import json

cars = {
    "manufacturers": [
        "Acura", "Alfa-Romeo", "Aston-Martin", "Audi", "Bentley", "BMW",
        "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Citroen",
        "Deus Automobiles", "Dodge", "Ferrari", "Fiat", "Ford", "Geely",
        "Genesis", "GMC", "Honda", "Hyundai", "Infiniti", "Jaguar", "Jeep",
        "Kia", "Koenigsegg", "Lamborghini", "Lancia", "Land Rover", "Lexus",
        "Lincoln", "Lotus", "Maserati", "Maybach", "Mazda", "McLaren", "Mercedes",
        "Mini", "Mitsubishi", "Nissan", "Opel", "Pagani", "Peugeot", "Pontiac",
        "Porsche", "Ram", "Renault", "Rolls-Royce", "Skoda", "Smart", "Subaru",
        "Suzuki", "Tesla", "Toyota", "Volkswagen", "Volvo"
    ]
}

print(json.dumps(cars, indent=4))
