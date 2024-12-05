from sprites import Enemy, BattleMap


class RoundCreator:
    def __init__(self):
        self.sequence = []  # This will store the sequence of spawn events

    def add_pause(self, duration=1000):
        self.sequence.append({
            'type': 'pause', 
            'duration': duration
        })

    def add_interval(self, enemy_name: str, spacing: int, duration: int):
        self.sequence.append({
            'type': 'interval', 
            'enemy_name': enemy_name, 
            'spacing': spacing, 
            'duration': duration
        })

    def create_round(self, round_number: int) -> 'Round':
        enemy_spawns = []
        spawn_interval = 0
        
        for event in self.sequence:
            if event['type'] == 'pause':
                spawn_interval += event['duration']
            elif event['type'] == 'interval':
                for i in range(0, event['duration'], event['spacing']):
                    enemy = Enemy(enemy_name=event['enemy_name'])
                    enemy_spawns.append(enemy)
                spawn_interval += event['duration']

        return Round(round_number, enemy_spawns, spawn_interval)


class Round:
    def __init__(self, round_number: int, enemy_spawns: list[Enemy], spawn_interval: int):
        self.round_number = round_number
        self.enemy_spawns = enemy_spawns
        self.spawn_interval = spawn_interval
        self.enemies_spawned = 0
        self.spawn_timer = 0 


class RoundManager:
    def __init__(self, map: BattleMap):
        self.map = map
        self.current_round = 1
        self.rounds = []  # List to store all rounds

    def add_round(self, round: Round):
        self.rounds.append(round)

    def start_round(self, round_number: int):
        self.current_round = round_number
        current_round = self.rounds[round_number - 1]
        self.spawn_enemies(current_round)

    def spawn_enemies(self, round: Round):
        for event in round.enemy_spawns:
            self.map.spawn_enemy(event, round.round_number)

    def update(self):
        current_round = self.rounds[self.current_round - 1]
        if current_round.spawn_timer >= current_round.spawn_interval:
            self.spawn_enemies(current_round)
            current_round.spawn_timer = 0
        else:
            current_round.spawn_timer += 1 