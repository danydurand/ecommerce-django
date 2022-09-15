$(document).ready(function () {
    $(".increment-btn").click(function (e) {
      e.preventDefault();
      var qty = $('#qty-input').val();
      var value = parseInt(qty, 10);
      value = isNaN(value) ? 0 : value;
      if (value < 10) {
        value++;
        $("#qty-input").val(value);
      }
    });
    $(".decrement-btn").click(function (e) {
      e.preventDefault();
      var qty = $('#qty-input').val();
      var value = parseInt(qty, 10);
      value = isNaN(value) ? 0 : value;
      if (value > 1) {
        value--;
        $("#qty-input").val(value);
      }
    });
})