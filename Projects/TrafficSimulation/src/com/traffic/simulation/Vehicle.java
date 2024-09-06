package com.traffic.simulation;

public class Vehicle implements Runnable {
    private Intersection current;
    private Intersection destination;
    private Dijkstra dijkstra;

    public Vehicle(Intersection start, Intersection destination, Dijkstra dijkstra) {
        this.current = start;
        this.destination = destination;
        this.dijkstra = dijkstra;
    }

    @Override
    public void run() {
        System.out.println("Vehicle started at: " + current.getName());

        // Calculate the shortest path
        dijkstra.findShortestPath(current, destination);

        // Simulate vehicle movement here (e.g., wait for time, update current position)
        System.out.println("Vehicle reached destination: " + destination.getName());
    }
}