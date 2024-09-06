package com.traffic.simulation;

public class Road {
    private Intersection start;
    private Intersection end;
    private double weight;  // Represents the time or distance to travel the road

    public Road(Intersection start, Intersection end, double weight) {
        this.start = start;
        this.end = end;
        this.weight = weight;
    }

    public Intersection getStart() {
        return start;
    }

    public Intersection getEnd() {
        return end;
    }

    public double getWeight() {
        return weight;
    }
}