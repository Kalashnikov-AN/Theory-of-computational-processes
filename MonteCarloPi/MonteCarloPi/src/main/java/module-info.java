module zabsu.montecarlopi {
    requires javafx.controls;
    requires javafx.fxml;


    opens zabsu.montecarlopi to javafx.fxml;
    exports zabsu.montecarlopi;
}