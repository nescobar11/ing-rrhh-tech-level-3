def f(sequence):
    n = len(sequence)
    collisions = [0] * n  # Inicializamos una lista para contar las colisiones de cada robot.
    robots = list(sequence)
    
    while True:
        new_robots = robots[:]
        collision_occurred = False
        
        for i in range(n - 1):
            if robots[i] == 'R' and robots[i + 1] == 'L':
                collisions[i] += 1
                collisions[i + 1] += 1
                new_robots[i] = 'L'
                new_robots[i + 1] = 'R'
                collision_occurred = True
        
        robots = new_robots
        
        if not collision_occurred:
            break
    
    return ' '.join(map(str, collisions))