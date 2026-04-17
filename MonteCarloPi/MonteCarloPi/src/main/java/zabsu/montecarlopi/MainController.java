package zabsu.montecarlopi;

import javafx.concurrent.Task;
import javafx.fxml.FXML;
import javafx.scene.control.*;

/**
 * Контроллер главного окна J
 * Отвечает за обработку пользовательских действий и взаимодействие с моделью данных
 */
public class MainController {

    /** Поле ввода количества итераций */
    @FXML private TextField iterationsField;

    /** Метка для отображения результата вычислений числа PI */
    @FXML private Label resultLabel;

    /** Метка состояния (информация о процессе выполнения) */
    @FXML private Label statusLabel;

    /** Индикатор прогресса выполнения вычислений */
    @FXML private ProgressBar progressBar;

    /** Модель данных, реализующая вычисление числа PI методом Монте-Карло */
    private final MonteCarloPi model = new MonteCarloPi();

    /** Фоновая задача (запуск в отдельном потоке) */
    private Task<Double> backgroundTask;

    /**
     * Метод инициализации контроллера.
     */
    @FXML
    private void initialize() {
        iterationsField.setText("100000000"); // Устанавливаем значение по умолчанию
        progressBar.setProgress(0); // Сбрасываем прогресс
    }

    /**
     * Обработчик запуска вычислений в основном потоке
     */
    @FXML
    private void runInMainThread() {
        // Останавливаем возможную фоновую задачу перед запуском новой в основном потоке
        stopComputation();

        // Снимаем привязку progressBar (если ранее была привязка к Task)
        progressBar.progressProperty().unbind();
        long iterations = getIterations();
        statusLabel.setText("Выполняется в основном потоке...");
        progressBar.setProgress(0);

        /*
         * Запуск вычислений напрямую (в этом же потоке).
         * progressCallback и resultCallback выполняются в UI-потоке
         */
        double pi = model.calculate(
                iterations,
                progress -> progressBar.setProgress(progress), // Обновление прогресса
                result -> resultLabel.setText(String.format("%.10f", result)) // Обновление результата
        );

        // После завершения вычислений обновляем статус
        statusLabel.setText("Завершено. PI = " + pi);
    }

    /**
     * Обработчик запуска вычислений в отдельном потоке
     */
    @FXML
    private void runInBackgroundThread() {
        // Останавливаем предыдущую задачу перед запуском новой
        stopComputation();

        // Снимаем старую привязку progressBar
        progressBar.progressProperty().unbind();
        long iterations = getIterations();
        statusLabel.setText("Выполняется в отдельном потоке...");
        progressBar.setProgress(0);

        /*
         * Создание фоновой задачи в отдельном потоке
         */
        backgroundTask = new Task<>() {
            @Override
            protected Double call() {
                return model.calculate(
                        iterations,
                        progress -> updateProgress(progress, 1.0),
                        result -> {}
                );
            }
        };


        /*
         * Привязываем ProgressBar к прогрессу Task
         * Тогда прогресс обновляется автоматически
         */
        progressBar.progressProperty().bind(backgroundTask.progressProperty());

        /*
         * Обработчик успешного завершения задачи
         * Выполняется в UI потоке
         */
        backgroundTask.setOnSucceeded(event -> {
            double pi = backgroundTask.getValue(); // Получаем результат из Task
            resultLabel.setText(String.format("%.10f", pi));
            statusLabel.setText("Вычисление завершено.");
        });

        /*
         * Обработчик отмены задачи
         */
        backgroundTask.setOnCancelled(event ->
                statusLabel.setText("Вычисление остановлено.")
        );

        // Запуск задачи в отдельном потоке
        new Thread(backgroundTask).start();
    }

    /**
     * Обработчик остановки вычислений
     *
     * Реализуется через:
     * - флаг в модели (model.stop())
     * - отмену Task (cancel())
     */
    @FXML
    private void stopComputation() {

        // Сообщаем модели, что нужно остановить вычисления
        model.stop();

        // Отменяем Task (если она существует)
        if (backgroundTask != null) {
            backgroundTask.cancel();
        }
        statusLabel.setText("Остановка вычислений...");
    }

    /**
     * Геттер для получения числа итераций из поля ввода
     *
     * @return количество итераций
     */
    private long getIterations() {
        try {
            return Long.parseLong(iterationsField.getText());
        } catch (NumberFormatException e) {
            showAlert("Ошибка", "Введите корректное число итераций.");
            return 1_000_000;
        }
    }

    /**
     * Показ диалогового окна с ошибкой
     */
    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}