package zabsu.n_threads_integration;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.*;

public class IntegrationController {

    @FXML private TextField aField;
    @FXML private TextField bField;
    @FXML private TextField nField;
    @FXML private TextField threadsField;
    @FXML private Label resultLabel;
    @FXML private Label statusLabel;
    @FXML private ComboBox<String> functionBox;
    @FXML private TextField customFunctionField;
    @FXML private Label timeLabel;

    private final IntegrationService service = new IntegrationService();


    @FXML
    public void initialize() {
        functionBox.getItems().addAll(
                "sin(x)",
                "cos(x)",
                "x^2",
                "e^x"
        );

        functionBox.setValue("sin(x)");
    }

    private MathFunction getSelectedFunction() {

        String selected = functionBox.getValue();

        switch (selected) {
            case "sin(x)":
                return Math::sin;
            case "cos(x)":
                return Math::cos;
            case "x^2":
                return x -> x * x;
            case "e^x":
                return Math::exp;
            default:
                return Math::sin;
        }
    }

    @FXML
    public void onCalculate() {

        double a = Double.parseDouble(aField.getText());
        double b = Double.parseDouble(bField.getText());
        int n = Integer.parseInt(nField.getText());
        int threads = Integer.parseInt(threadsField.getText());

        MathFunction function = getSelectedFunction();

        statusLabel.setText("Вычисление...");

        new Thread(() -> {
            try {
                IntegrationModel model = new IntegrationModel(a, b, n, function);

                long startTime = System.nanoTime();

                double result = service.integrate(model, threads);

                long endTime = System.nanoTime();

                double timeMs = (endTime - startTime) / 1_000_000.0;

                Platform.runLater(() -> {
                    resultLabel.setText(String.valueOf(result));
                    timeLabel.setText(String.format("%.3f ms", timeMs));
                    statusLabel.setText("Готово!");
                });

            } catch (Exception e) {
                Platform.runLater(() -> {
                    statusLabel.setText("Ошибка");
                });
            }
        }).start();
    }
}