package com.traffic.simulation;

import java.util.ArrayList;
import java.util.List;

public class Simulation {
    private List<Intersection> intersections;
    private List<Road> roads;
    private List<Vehicle> vehicles;

    public Simulation() {
        intersections = new ArrayList<>();
        roads = new ArrayList<>();
        vehicles = new ArrayList<>();
    }

    public void setup() {
        // Create intersections (nodes)
        Intersection a = new Intersection(1, "A");
        Intersection b = new Intersection(2, "B");
        Intersection c = new Intersection(3, "C");

        intersections.add(a);
        intersections.add(b);
        intersections.add(c);

        // Create roads (edges)
        Road ab = new Road(a, b, 5); // Road from A to B with weight 5
        Road bc = new Road(b, c, 10);

        roads.add(ab);
        roads.add(bc);

        // Create vehicles
        Dijkstra dijkstra = new Dijkstra();
        Vehicle vehicle = new Vehicle(a, c, dijkstra);
        vehicles.add(vehicle);
    }

    public void startSimulation() {
        for (Vehicle vehicle : vehicles) {
            Thread t = new Thread(vehicle);
            t.start();
        }
    }

    public static void main(String[] args) {
        Simulation simulation = new Simulation();
        simulation.setup();
        simulation.startSimulation();
    }
}