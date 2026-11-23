#!/usr/bin/env python3
"""Factory pattern: create vehicles through a registry."""


class Bus:
    """A bus travels on the road."""

    def mode(self) -> str:
        """Return how the bus travels."""
        return "road"


class Train:
    """A train travels on rails."""

    def mode(self) -> str:
        """Return how the train travels."""
        return "rails"


class Bike:
    """A bike travels in a lane."""

    def mode(self) -> str:
        """Return how the bike travels."""
        return "lane"


class Scooter:
    """A scooter travels in a scooter lane."""

    def mode(self) -> str:
        """Return how the scooter travels."""
        return "scooter_lane"


class VehicleFactory:
    """Creates vehicles by name using a registry of classes."""

    def __init__(self):
        """Start with an empty registry."""
        self._registry = {}

    def register_kind(self, name: str, cls) -> None:
        """Map a vehicle name to the class that builds it."""
        self._registry[name] = cls

    def create(self, kind: str):
        """Return a new vehicle of the registered kind."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main():
    """Register vehicle kinds and print how each one travels."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
