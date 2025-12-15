# Define races and classes for Cyberdelia EX

RACES = {
    "Human": {
        "description": "Versatile and adaptive, with balanced stats.",
        "stats": {"hp": 100, "energy": 100, "strength": 10, "tech": 10, "speed": 10},
        "abilities": ["Adapt", "Negotiate"]
    },
    "Cyborg": {
        "description": "Enhanced with cybernetics. High tech and energy.",
        "stats": {"hp": 90, "energy": 130, "strength": 12, "tech": 15, "speed": 8},
        "abilities": ["Overclock", "EMP Resistance"]
    },
    "AI": {
        "description": "Artificial intelligence. Superior tech, low HP.",
        "stats": {"hp": 70, "energy": 150, "strength": 8, "tech": 18, "speed": 12},
        "abilities": ["Hack", "Data Ghost"]
    },
    "Mutant": {
        "description": "Genetically altered. High HP and strength.",
        "stats": {"hp": 130, "energy": 80, "strength": 15, "tech": 7, "speed": 11},
        "abilities": ["Regenerate", "Feral Rage"]
    }
}

CLASSES = {
    "Netrunner": {
        "description": "Elite hackers, masters of cyberspace.",
        "stats": {"tech": 5, "energy": 20},
        "abilities": ["Quickjack", "Firewall"]
    },
    "Street Samurai": {
        "description": "Combat specialists, skilled with weapons.",
        "stats": {"hp": 20, "strength": 5},
        "abilities": ["Blade Rush", "Counterattack"]
    },
    "Techie": {
        "description": "Engineers and inventors, can repair and build.",
        "stats": {"tech": 3, "energy": 10},
        "abilities": ["Repair", "Deploy Drone"]
    },
    "Fixer": {
        "description": "Deal-makers and info brokers, resourceful survivors.",
        "stats": {"speed": 3, "energy": 10},
        "abilities": ["Scavenge", "Contact"]
    }
}
