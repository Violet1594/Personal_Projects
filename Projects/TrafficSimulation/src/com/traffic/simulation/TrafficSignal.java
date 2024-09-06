package com.traffic.simulation;

public class TrafficSignal {
    private boolean isGreen;

    public TrafficSignal(boolean isGreen) {
        this.isGreen = isGreen;
    }

    public boolean isGreen() {
        return isGreen;
    }

    public void switchSignal() {
        isGreen = !isGreen;
    }
}