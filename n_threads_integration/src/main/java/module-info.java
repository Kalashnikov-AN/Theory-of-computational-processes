module zabsu.n_threads_integration {
    requires javafx.controls;
    requires javafx.fxml;


    opens zabsu.n_threads_integration to javafx.fxml;
    exports zabsu.n_threads_integration;
}