$(document).ready(function() {
  $('#contactModal').on('show.bs.modal', function(event) {
    var modal = $(this);
    modal.find('.modal-body').load('{% url "contact" %}');
  });

  $('form').on('submit', function(event) {
    event.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      dataType: 'json',
      success: function(response) {
        if (response.success) {

          $('#contactModal .modal-body').html('<p>Message sent successfully!</p>');
        } else {

          var formHtml = $('<form>').html(response.errors);
          $('#contactModal .modal-body').html(formHtml);
        }
      }
    });
  });
});
