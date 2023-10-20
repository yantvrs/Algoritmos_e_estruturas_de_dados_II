# Class to represent car setups with various components
class CarSetups:
    def __init__(self, breaks, gearBox, rearWing, frontWing, suspension, engine):
        # Initialize car setup components
        self.breaks = breaks
        self.gearBox = gearBox
        self.rearWing = rearWing
        self.frontWing = frontWing
        self.suspension = suspension
        self.engine = engine

    # Options for each component
    breaksOptions = ["Wildcore", "Suspense", "The Warden", "Onyx", "Axiom", "Crisis SL", "Essence", "Starter"]
    gearBoxesOptions = ["Voyage", "Vector", "Kick Shift", "Verdict", "Spectrum", "Swiftcharge", "Switch-R-OO", "Starter"]
    rearWingsOptions = ["Typhoon", "Transcendence", "Freeflare", "The Patron", "The Wasp", "The Matador", "Phantom-X", "Starter"]
    frontWingsOptions = ["Virtue", "Thunderclap", "Trailblazer", "Zeno", "The Vagabond", "Feral Punch", "The Scout", "Starter"]
    suspensionsOptions = ["Sigma", "Presence", "Horizon", "Radiance", "Icon V3", "Rodeo", "The Equator", "Starter"]
    enginesOptions = ["Cloudroar", "Avalanche", "The Rover", "Twinburst", "Enigma", "Nova", "Brute Force", "Starter"]

    # Calculate and return contributions for the setup
    def sum_contributions(self):
        contributions = {
            "speed": 0,
            "cornering": 0,
            "powerUnit": 0,
            "reliability": 0,
            "averagePitStopTime": 0
        }

        # Define contributions for each component
        brakes_contributions = {
            "Wildcore": (36, 23, 33, 22, 0.59),
            "Suspense": (20, 32, 23, 21, 0.37),
            "The Warden": (26, 28, 27, 25, 0.43),
            "Onyx": (26, 23, 25, 50, 0.49),
            "Axiom": (14, 34, 18, 15, 0.67),
            "Crisis SL": (27, 16, 18, 19, 0.51),
            "Essence": (14, 13, 12, 25, 0.76),
            "Starter": (1, 1, 1, 1, 1)
        }

        gearbox_contributions = {
            "Voyage": (23, 28, 22, 27, 0),
            "Vector": (24, 38, 22, 36, 0.55),
            "Kick Shift": (18, 19, 29, 19, 0.45),
            "Verdict": (33, 18, 20, 30, 0.63),
            "Spectrum": (20, 25, 21, 23, 0.53),
            "Swiftcharge": (14, 23, 22, 16, 0.71),
            "Switch-R-OO": (12, 13, 11, 14, 0.47),
            "Starter": (1, 1, 1, 1, 1)
        }


        rear_wing_contributions = {
            "Typhoon": (50, 27, 26, 23, 0.53),
            "Transcendence": (24, 22, 36, 37, 0.53),
            "Freeflare": (21, 33, 20, 22, 0.37),
            "The Patron": (23, 21, 19, 37, 0.61),
            "The Wasp": (16, 24, 23, 14, 0.69),
            "The Matador": (19, 16, 18, 17, 0.72),
            "Phantom-X": (26, 15, 12, 11, 0.76),
            "Starter": (1, 1, 1, 1, 1)
        }

        front_wing_contributions = {
            "Virtue": (23, 50, 27, 24, 0.49),
            "Thunderclap": (35, 23, 21, 33, 0.55),
            "Trailblazer": (21, 23, 42, 20, 0.57),
            "Zeno": (25, 23, 22, 26, 0.53),
            "The Vagabond": (31, 20, 23, 21, 0.35),
            "Feral Punch": (13, 15, 22, 21, 0.73),
            "The Scout": (13, 27, 15, 14, 0.73),
            "Starter": (1, 1, 1, 1, 1)
        }

        suspension_contributions = {
            "Sigma": (32, 28, 30, 29, 0.39),
            "Presence": (23, 26, 24, 22, 0.2),
            "Horizon": (22, 36, 24, 37, 0.53),
            "Radiance": (25, 17, 26, 19, 0.65),
            "Icon V3": (17, 13, 16, 23, 0.54),
            "Rodeo": (23, 22, 15, 14, 0.69),
            "The Equator": (20, 19, 18, 21, 0.61),
            "Starter": (1, 1, 1, 1, 1)
        }

        engine_contributions = {
            "Cloudroar": (26, 24, 50, 27, 0.55),
            "Avalanche": (34, 22, 25, 21, 0.35),
            "The Rover": (27, 25, 28, 24, 0.53),
            "Twinburst": (16, 29, 18, 17, 0.51),
            "Enigma": (16, 13, 23, 25, 0.69),
            "Nova": (31, 13, 15, 16, 0.71),
            "Brute Force": (21, 19, 36, 18, 0.63),
            "Starter": (1, 1, 1, 1, 1)
        }

        # Add contributions from selected components to the overall contributions
        contributions["speed"] += brakes_contributions[self.breaks][0]
        contributions["cornering"] += brakes_contributions[self.breaks][1]
        contributions["powerUnit"] += brakes_contributions[self.breaks][2]
        contributions["reliability"] += brakes_contributions[self.breaks][3]
        contributions["averagePitStopTime"] += brakes_contributions[self.breaks][4]

        contributions["speed"] += gearbox_contributions[self.gearBox][0]
        contributions["cornering"] += gearbox_contributions[self.gearBox][1]
        contributions["powerUnit"] += gearbox_contributions[self.gearBox][2]
        contributions["reliability"] += gearbox_contributions[self.gearBox][3]
        contributions["averagePitStopTime"] += gearbox_contributions[self.gearBox][4]

        contributions["speed"] += rear_wing_contributions[self.rearWing][0]
        contributions["cornering"] += rear_wing_contributions[self.rearWing][1]
        contributions["powerUnit"] += rear_wing_contributions[self.rearWing][2]
        contributions["reliability"] += rear_wing_contributions[self.rearWing][3]
        contributions["averagePitStopTime"] += rear_wing_contributions[self.rearWing][4]

        contributions["speed"] += front_wing_contributions[self.frontWing][0]
        contributions["cornering"] += front_wing_contributions[self.frontWing][1]
        contributions["powerUnit"] += front_wing_contributions[self.frontWing][2]
        contributions["reliability"] += front_wing_contributions[self.frontWing][3]
        contributions["averagePitStopTime"] += front_wing_contributions[self.frontWing][4]

        contributions["speed"] += suspension_contributions[self.suspension][0]
        contributions["cornering"] += suspension_contributions[self.suspension][1]
        contributions["powerUnit"] += suspension_contributions[self.suspension][2]
        contributions["reliability"] += suspension_contributions[self.suspension][3]
        contributions["averagePitStopTime"] += suspension_contributions[self.suspension][4]

        contributions["speed"] += engine_contributions[self.engine][0]
        contributions["cornering"] += engine_contributions[self.engine][1]
        contributions["powerUnit"] += engine_contributions[self.engine][2]
        contributions["reliability"] += engine_contributions[self.engine][3]
        contributions["averagePitStopTime"] += engine_contributions[self.engine][4]

        return contributions

# Driver performance data
drivers = {
    'Max Verstappen': {
        'overtaking': 97,
        'defending': 86,
        'qualifying': 99,
        'race_start': 89,
        'tyre_management': 94
    },
    'Charles Leclerc': {
        'overtaking': 93,
        'defending': 99,
        'qualifying': 97,
        'race_start': 87,
        'tyre_management': 89
    },
    'Fernando Alonso': {
        'overtaking': 99,
        'defending': 92,
        'qualifying': 89,
        'race_start': 97,
        'tyre_management': 88
    },
    'Lewis Hamilton': {
        'overtaking': 81,
        'defending': 86,
        'qualifying': 89,
        'race_start': 94,
        'tyre_management': 90
    },
    'Lando Norris': {
        'overtaking': 99,
        'defending': 95,
        'qualifying': 99,
        'race_start': 99,
        'tyre_management': 99
    },
    'George Russell': {
        'overtaking': 95,
        'defending': 90,
        'qualifying': 91,
        'race_start': 83,
        'tyre_management': 86
    },
    'Sergio Perez': {
        'overtaking': 85,
        'defending': 96,
        'qualifying': 89,
        'race_start': 91,
        'tyre_management': 84
    },
    'Carlos Sainz': {
        'overtaking': 84,
        'defending': 85,
        'qualifying': 95,
        'race_start': 90,
        'tyre_management': 91
    },
    'Lance Stroll': {
        'overtaking': 92,
        'defending': 83,
        'qualifying': 87,
        'race_start': 94,
        'tyre_management': 89
    },
    'Pierre Gasly': {
        'overtaking': 88,
        'defending': 93,
        'qualifying': 83,
        'race_start': 85,
        'tyre_management': 96
    },
}

# Performance-enhancing bottles
bottles = {
    'Tsar': {
        'defending': 10,
        'tyre_management': 15,
        'cornering': 15
    },
    'Frost': {
        'tyre_management': 25,
        'race_start': 15,
        'reliability': 10
    },
    'Tulip': {
        'defending': 10,
        'reliability': 20,
        'pit_stop': 20
    },
    'Dragon': {
        'overtaking': 20,
        'tyre_management': 15,
        'power_unit': 15
    },
    'Kawaii': {
        'race_start': 15,
        'cornering': 20,
        'pit_stop': 15
    },
    'Pretzel': {
        'tyre_management': 25,
        'power_unit': 15,
        'pit_stop': 10
    },
    'Vice': {
        'speed': 10,
        'power_unit': 15,
        'reliability': 25
    },
    'Schooner': {
        'defending': 10,
        'reliability': 25,
        'pit_stop': 15
    },
    'Dijin': {
        'defending': 15,
        'cornering': 15,
        'reliability': 20
    },
    'Oud': {
        'overtaking': 15,
        'cornering': 10,
        'pit_stop': 25
    },
    'Eternal Flame': {
        'overtaking': 25,
        'tyre_management': 10,
        'reliability': 15
    },
    'Eagle': {
        'tyre_management': 20,
        'reliability': 15,
        'pit_stop': 15
    },
    'Iron Force': {
        'tyre_management': 10,
        'power_unit': 20,
        'reliability': 20
    },
    'Lumberjack': {
        'defending': 15,
        'tyre_management': 10,
        'reliability': 25
    },
    'Cranberry': {
        'overtaking': 20,
        'defending': 20,
        'reliability': 10
    },
    'Butterfly': {
        'tyre_management': 20,
        'power_unit': 25,
        'pit_stop': 5
    },
    'Tune-in': {
        'speed': 10,
        'cornering': 15,
        'pit_stop': 25
    },
    'Self-Control': {
        'tyre_management': 5,
        'speed': 5,
        'reliability': 5
    },
    'Warrior': {
        'overtaking': 5,
        'defending': 5,
        'speed': 10
    },
    'Ballast': {
        'race_start': 5,
        'cornering': 10,
        'pit_stop': 10
    },
    'Instinct': {
        'race_start': 10,
        'power_unit': 15,
        'reliability': 5},
    'Downforce': {
        'defending': 15,
        'tyre_management': 15,
        'cornering': 5
    },
    'Hex': {
        'overtaking': 20,
        'speed': 15,
        'pit_stop': 5
    },
    'Eggception': {
        'defending': 15,
        'power_unit': 10,
        'pit_stop': 25
    },
    'Rooster': {
        'overtaking': 20,
        'race_start': 20,
        'power_unit': 10
    },
    'Cuppa': {
        'overtaking': 10,
        'race_start': 20,
        'cornering': 20
    },
    'Street Shark': {
        'overtaking': 10,
        'race_start': 25,
        'speed': 15
    },
    'Herald': {
        'overtaking': 10,
        'race_start': 25,
        'cornering': 15
    },
    'Prince': {
        'defending': 10,
        'pit_stop': 20,
        'cornering': 20
    },
    'Unstoppable': {
        'overtaking': 25,
        'speed': 15,
        'power_unit': 10
    },
    'Dead Fast': {
        'tyre_management': 5,
        'speed': 25,
        'power_unit': 20
    },
    'Gladiator': {
        'defending': 25,
        'race_start': 15,
        'power_unit': 10
    },
    'Tauros': {
        'overtaking': 5,
        'speed': 20,
        'power_unit': 25
    },
    'Merlion': {
        'speed': 15,
        'cornering': 25,
        'pit_stop': 10
    },
    'Samba': {
        'speed': 5,
        'power_unit': 25,
        'pit_stop': 20
    },
    'Caveira': {
        'overtaking': 15,
        'speed': 25,
        'power_unit': 10
    },
    'Fogos': {
        'overtaking': 15,
        'race_start': 15,
        'speed': 20
    },
    'Movember': {
        'defending': 15,
        'tyre_management': 10,
        'cornering': 25
    },
    'Palmeira': {
        'defending': 20,
        'tyre_management': 20,
        'race_start': 10},
    'Nazar': {
        'tyre_management': 15,
        'race_start': 20,
        'reliability': 15
    },
    'Aderencia': {
        'race_start': 10,
        'cornering': 25,
        'reliability': 15
    },
    'Arco-iris': {
        'defending': 25,
        'race_start': 5,
        'speed': 20
    },
    'Eclipse': {
        'overtaking': 15,
        'speed': 25,
        'pit_stop': 10
    },
    'Rena': {
        'defending': 20,
        'cornering': 10,
        'pit_stop': 20
    }
}

