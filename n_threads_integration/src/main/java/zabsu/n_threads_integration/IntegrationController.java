package zabsu.n_threads_integration;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.*;

/**
 * Контроллер приложения для численного интегрирования
 */
public class IntegrationController {

    @FXML private TextField aField;          // нижняя граница интегрирования
    @FXML private TextField bField;          // верхняя граница интегрирования
    @FXML private TextField nField;          // количество разбиений
    @FXML private TextField threadsField;   // количество потоков

    @FXML private Label resultLabel;        // вывод результата интегрирования
    @FXML private Label statusLabel;        // статус (ожидание/выполнение/ошибка)
    @FXML private Label timeLabel;          // время выполнения алгоритма

    @FXML private ComboBox<String> functionBox;     // выбор функции


    /**
     * Сервис, выполняющий параллельное интегрирование
     */
    private final IntegrationService service = new IntegrationService();


    /**
     * Инициализация UI
     */
    @FXML
    public void initialize() {
        // Заполняем список доступных функций
        functionBox.getItems().addAll(
                "sin(x)",
                "cos(x)",
                "x^2",
                "e^x"
        );

        // Устанавливаем значение по умолчанию
        functionBox.setValue("sin(x)");
    }


    /**
     * Возвращает выбранную пользователем математическую функцию
     * Используется функциональный интерфейс MathFunction
     */
    private MathFunction getSelectedFunction() {

        String selected = functionBox.getValue();

        // В зависимости от выбора возвращаем соответствующую функцию
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


    /**
     * Обработчик кнопки "Вычислить".
     *
     * Выполняет:
     *  1. Чтение данных из UI
     *  2. Запуск вычислений в отдельном потоке
     *  3. Обновление UI после завершения
     */
    @FXML
    public void onCalculate() {

        double a = Double.parseDouble(aField.getText());   // начало интервала
        double b = Double.parseDouble(bField.getText());   // конец интервала
        int n = Integer.parseInt(nField.getText());        // число разбиений
        int threads = Integer.parseInt(threadsField.getText()); // число потоков

        // Получаем выбранную функцию
        MathFunction function = getSelectedFunction();

        // Обновляем статус
        statusLabel.setText("Вычисление...");

        new Thread(() -> {
            try {
                // Создаём модель задачи
                IntegrationModel model = new IntegrationModel(a, b, n, function);

                // Замер времени
                long startTime = System.nanoTime();

                // Выполнение параллельного интегрирования
                double result = service.integrate(model, threads);

                long endTime = System.nanoTime();

                // Перевод времени в миллисекунды
                double timeMs = (endTime - startTime) / 1_000_000.0;


                // Platform.runLater помещает задачу в очередь UI-потока
                Platform.runLater(() -> {
                    resultLabel.setText(String.valueOf(result)); // вывод результата
                    timeLabel.setText(String.format("%.3f ms", timeMs)); // вывод времени
                    statusLabel.setText("Готово!");
                });

            } catch (Exception e) { // обработка ошибок
                Platform.runLater(() -> {
                    statusLabel.setText("Ошибка");
                });
            }
        }).start(); // запуск потока
    }
}