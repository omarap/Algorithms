import cmd

class Motocycle:
    def __init__(self, base, travel, efficency):
        self.base = base
        self.travel = travel
        self.trips = []
        self.efficency = efficency

    def cost(self, length):
        if not (0<= length <= 50):
            raise ValueError('Invalid trip length')
        return (self.base + self.travel * length) * 1.06

    def distance(self):
        return sum(trip[0] for trip in self.trips)

    def record_trip(self, distance, people):
        if len(self.trips) + 1 > 24:
            raise ValueError("Can't store more than 24 trips")
        if self.distance() + distance > 350:
            raise ValueError("Can't store more than 350KM")
        self.trips.append((distance, people))

    def average_cost(self):
        return self.distance() * self.efficency

    def total_people(self):
        return sum(trip[1] for trip in self.trips)

    def gross_income(self):
        return sum(self.cost(distance) for distance, _ in self.trips)


def args(values, metas):
    values = values.split()
    if len(values) > len(metas):
        keys = ', '.join(m[0] for m in metas)
        raise ValueError(f'Too many keys should have {keys}')

    if len(values) < len(metas):
        keys = ', '.join(m[0] for m in metas[len(values):])
        raise ValueError(f'Missing {keys}')

    output = []
    for value, meta in zip(values, metas):
        try:
            value = meta[1](value)
        except ValueError as e:
            raise ValueError(f'Invalid value for {meta[0]}')
        output.append(value)
    return output


class MotocycleRenter(cmd.Cmd):
    intro = 'Welcome to distance fare.   Type help or ? to list commands.\n'
    prompt = '> '
    motocycles = {
        'boda':         Motocycle(1000, 500, 4.4/100),
    }

    def get_motocycle(self, motocycle):
        v = self.motocycles.get(motocycle, None)
        if v is None:
            keys = ', '.join(self.motocycles.keys())
            raise ValueError(f'Invalid motocycle {motocycle!r}, options are {keys}')
        return v

    def do_motocycles(self, _):
        """List all the motocycles available."""
        print(', '.join(self.motocycles.keys()))

    def do_cost(self, arg):
        """
        Calculate the cost of a trip.

        cost {motocycle name} {distance}
        """
        try:
            motocycle, distance = args(arg, (('motocycle', str), ('distance', float)))
            print(self.get_motocycle(motocycle).cost(distance))
        except ValueError as e:
            print(e)

    def do_trip(self, arg):
        """
        Record a trip.

        trip {motocycle name} {distance} {people}
        trip boda 3 1
        """
        try:
            motocycle, distance, people = args(arg, (('motocycle', str), ('distance', float), ('people', int)))
            self.get_motocycle(motocycle).record_trip(distance, people)
        except ValueError as e:
            print(e)


    def do_stats(self, _):
        """See the stats of the motocycles"""
        for name, v in self.motocycles.items():
            print(
                f'{name}:\n'
                f'  trips: {len(v.trips)}\n'
                f'  distance: {v.distance()}\n'
                f'  people: {v.total_people()}\n'
                f'  gross income: {v.gross_income():.2f}\n'
                f'  fuel: {v.average_cost():.2f}\n'
                f'  net profit: {v.gross_income() - v.average_cost():.2f}\n'
            )

if __name__ == '__main__':
    MotocycleRenter().cmdloop()


