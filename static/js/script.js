$(function() {
  $('a#process_input').bind('click', function() {
  $.getJSON('/calculation', {

    summ: $('input[name="summ"]').val(),
    check: $('#check').prop('checked'),
    student: $('#student').prop('checked'),
    handicap: $('#handicap').prop('checked'),
    invalid: $('#invalid').val(),
    kids: $('input[name="kids"]').val(),
    kids_handicap: $('input[name="kids_handicap"]').val()

  }, function(data) {
    $("#result").html('');
    $("#result").append(`
      <p>Vaše čistá měsíčni mzda činí:</p>
      <h2>${data.result}</h2>
      <p>Daň:
        <span id="tax">${data.tax}</span>
        <a href="#" data-tip="Pokud tato částka výjde v mínusu, jedná se o daňový bonus. Pro vyplacení daňového bonusu musí tato částka dosáhnout alespoň 100kč.">
        <i class="fas fa-info-circle"></i>
        </a>
      </p>
      <p>Sociální odvody: <span id="social_tax"></span>${data.social_tax}</p>
      <p>Zdravotní odvody: <span id="medical_tax"></span>${data.medical_tax}</p>
    `);
  });
  return false;
  });
});


$("#button-one").click(function(event){
  event.preventDefault();
  $(".tax-discount").slideToggle("slow");
}); 

$("#button-two").click(function(event){
  event.preventDefault();
  $(".tax-discount-kids").slideToggle("slow");
});  

