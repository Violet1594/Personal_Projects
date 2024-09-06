package com.traffic.simulation;

import java.util.ArrayList;
import java.util.List;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.stage.Stage;

public class GraphicalInterface extends Application {
    private Pane root;
    private List<Intersection> intersections;
    private List<Road> roads;

    @Override
    public void start(Stage primaryStage) {
        root = new Pane();
        intersections = new ArrayList<>();
        roads = new ArrayList<>();

        Scene scene = new Scene(root, 800, 600);
        primaryStage.setTitle("Traffic Simulation");
        primaryStage.setScene(scene);
        primaryStage.show();

        setupUI();
    }

    private void setupUI() {
        // Input fields for intersection coordinates and road connections
        TextField intersectionInput = new TextField();
        intersectionInput.setPromptText("Intersection (x, y)");
        intersectionInput.setLayoutX(10);
        intersectionInput.setLayoutY(10);

        Button addIntersectionButton = new Button("Add Intersection");
        addIntersectionButton.setLayoutX(200);
        addIntersectionButton.setLayoutY(10);
        addIntersectionButton.setOnAction(e -> {
            String[] coords = intersectionInput.getText().split(",");
            int x = Integer.parseInt(coords[0].trim());
            int y = Integer.parseInt(coords[1].trim());
            addIntersection(x, y);
        });

        TextField roadInput = new TextField();
        roadInput.setPromptText("Road (from, to, weight)");
        roadInput.setLayoutX(10);
        roadInput.setLayoutY(50);

        Button addRoadButton = new Button("Add Road");
        addRoadButton.setLayoutX(200);
        addRoadButton.setLayoutY(50);
        addRoadButton.setOnAction(e -> {
            String[] roadData = roadInput.getText().split(",");
            int fromIndex = Integer.parseInt(roadData[0].trim());
            int toIndex = Integer.parseInt(roadData[1].trim());
            double weight = Double.parseDouble(roadData[2].trim());
            addRoad(fromIndex, toIndex, weight);
        });

        root.getChildren().addAll(intersectionInput, addIntersectionButton, roadInput, addRoadButton);
    }

    private void addIntersection(int x, int y) {
        Intersection intersection = new Intersection(intersections.size(), "Intersection " + (intersections.size() + 1));
        intersections.add(intersection);

        Circle circle = new Circle(x, y, 10, Color.BLUE);
        root.getChildren().add(circle);
    }

    private void addRoad(int fromIndex, int toIndex, double weight) {
        Intersection from = intersections.get(fromIndex);
        Intersection to = intersections.get(toIndex);

        Road road = new Road(from, to, weight);
        roads.add(road);

        Line line = new Line(from.getX(), from.getY(), to.getX(), to.getY());
        line.setStroke(Color.BLACK);
        root.getChildren().add(line);
    }

    public static void main(String[] args) {
        launch(args);
    }
}