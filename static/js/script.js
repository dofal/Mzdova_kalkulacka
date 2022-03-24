    let summ = document.getElementById("summ")
    let check = document.querySelector("#check")
    let student = document.querySelector("#student")
    let handicap = document.querySelector("#handicap")
    let invalid = document.querySelector("#invalid")
    let kids = document.getElementById("kids")
    let kids_handicap = document.getElementById("kids_handicap")

    let message_container = document.querySelector("#message");


function send() {  
      let entry = {
      summ: summ.value,
      check: check.checked,
      student: student.checked,
      handicap: handicap.checked,
      invalid: invalid.value,
      kids: kids.value,
      kids_handicap: kids_handicap.value
    };
    
    fetch('/', {

      method: "POST",
      credentials: "include",
      body: JSON.stringify(entry),
      cache: "no-cache",
      headers : new Headers({
        "content-type" : "application/json"
      })
    })
}

  function get_values() {
    $.ajax({
      type: "POST",
      url: "/calculation",
      dataType: 'json', 
      success: function(data){
        $(result).replaceWith(data)
      }
    });

    message_container.classList.add('message-container-style');

}



$("#button-one").click(function(event){
  event.preventDefault();
  $(".tax-discount").slideToggle("slow");
}); 

$("#button-two").click(function(event){
  event.preventDefault();
  $(".tax-discount-kids").slideToggle("slow");
});  

