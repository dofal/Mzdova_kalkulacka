function send() {  
      
    var summ = document.getElementById("summ")
    var check = document.querySelector("#check")
    var student = document.querySelector("#student")
    var handicap = document.querySelector("#handicap")
    var invalid = document.querySelector("#invalid")
    var kids = document.getElementById("kids")
    var kids_handicap = document.getElementById("kids_handicap")

    var entry = {
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

  function get_values(){
    $.ajax({
      type: "POST",
      url: "/calculation",
      dataType: 'json', 
      success: function(data){
        $(result).replaceWith(data)
      }
    });
  }