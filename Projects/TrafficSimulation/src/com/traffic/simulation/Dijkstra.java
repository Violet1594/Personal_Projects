package com.traffic.simulation;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Dijkstra {
    public Map<Intersection, Double> findShortestPath(Intersection start, Intersection destination) {
        PriorityQueue<Intersection> pq = new PriorityQueue<>((a, b) -> Double.compare(a.getId(), b.getId()));
        Map<Intersection, Double> distances = new HashMap<>();
        distances.put(start, 0.0);

        pq.add(start);

        while (!pq.isEmpty()) {
            Intersection current = pq.poll();

            // Check for destination reach
            if (current.equals(destination)) {
				break;
			}

            // Implement logic for updating distances here
        }

        return distances;
    }
}