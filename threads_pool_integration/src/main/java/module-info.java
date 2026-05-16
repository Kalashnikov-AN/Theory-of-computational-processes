module zabsu.threads_pool_integration {
    requires javafx.controls;
    requires javafx.fxml;


    opens zabsu.threads_pool_integration to javafx.fxml;
    exports zabsu.threads_pool_integration;
}