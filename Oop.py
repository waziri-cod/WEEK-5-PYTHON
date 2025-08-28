# Base class
class Rifle:
    """Base rifle class with attributes and methods."""
    def __init__(self, name, ammo_capacity, range_meters):
        self.name = name
        self.ammo_capacity = ammo_capacity
        self.current_ammo = ammo_capacity
        self.range_meters = range_meters

    def shoot(self):
        if self.current_ammo > 0:
            self.current_ammo -= 1
            return f"{self.name}: 🔫 Shooting... {self.current_ammo} bullets left."
        else:
            return f"{self.name}: ❌ Out of ammo! Reload needed."

    def reload(self):
        self.current_ammo = self.ammo_capacity
        return f"{self.name}: 🔄 Reloaded to {self.ammo_capacity} bullets."

    def info(self):
        return f"{self.name} | Ammo: {self.current_ammo}/{self.ammo_capacity} | Range: {self.range_meters}m"


# Child classes (inheritance + polymorphism)
class AK14(Rifle):
    def shoot(self):
        if self.current_ammo > 0:
            self.current_ammo -= 2  # AK14 fires 2 bullets per shot
            if self.current_ammo < 0:
                self.current_ammo = 0
            return f"{self.name}: 🔥 Rapid fire! {self.current_ammo} bullets left."
        else:
            return f"{self.name}: ❌ Click! No bullets left."


class SMG(Rifle):
    def shoot(self):
        if self.current_ammo > 0:
            self.current_ammo -= 3  # SMG bursts more
            if self.current_ammo < 0:
                self.current_ammo = 0
            return f"{self.name}: 💥 Spraying bullets! {self.current_ammo} bullets left."
        else:
            return f"{self.name}: ❌ Empty! Reload now."


class M15(Rifle):
    def shoot(self):
        if self.current_ammo > 0:
            self.current_ammo -= 1  # precision rifle, single shot
            return f"{self.name}: 🎯 Precision shot fired. {self.current_ammo} bullets left."
        else:
            return f"{self.name}: ❌ No ammo, reload required."


# Example usage
if __name__ == "__main__":
    rifles = [
        AK14("AK14", 30, 400),
        SMG("SMG", 25, 250),
        M15("M15", 20, 600)
    ]

    for r in rifles:
        print(r.info())
        print(r.shoot())
        print(r.shoot())
        print(r.reload())
        print(r.info())
        print("-" * 40)
