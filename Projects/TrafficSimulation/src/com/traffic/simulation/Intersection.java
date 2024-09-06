package com.traffic.simulation;

public class Intersection {
    private int id;
    private String name;

    public Intersection(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}