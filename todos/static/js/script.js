// Назначение обработчика события click для кнопок "Выполнено"
document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.completed-btn');
  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      alert('Задача завершена!');
      const todoId = button.dataset.id;
      set_completed(todoId);
    });
  });
});
