import trafficSimulator as ts

sim = ts.Simulation()

# Add road segments
sim.create_segment((-100, 50), (150, 56))
sim.create_segment((-100, 50), (-200,-100))
sim.create_segment((220, -70), (150, 56))
sim.create_segment((0, -120), (150, 56))
sim.create_segment((-200,-100), (0, -120))
sim.create_segment((-200,-100), (-190, -200))
sim.create_segment((20, -220), (-190, -200))
sim.create_segment((20, -220), (0, -120))
sim.create_segment((220, -70), (0, -120))
sim.create_segment((220, -70), (260, -190))
sim.create_segment((20, -220), (260, -190))

# Add vehicle generator
sim.create_vehicle_generator(
    vehicle_rate=20,
    vehicles=[
        (10, {'path': [0], 'v': 16.6}),
        (1, {'path': [0], 'v': 16.6, 'l': 7}),

        (10, {'path': [1], 'v': 16.6}),
        (1, {'path': [1], 'v': 16.6, 'l': 7})
        ]
    )

# Show simulation visualization
win = ts.Window(sim)
win.show()
