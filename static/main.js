$(function() {
  $('form').on('submit', function(e){

    allInputsForm = []

    $(this).find(".input-form").each(function(i) {
      inputForm = {}

      inputFormId = $(this).find(".input-id").serializeArray()[0]
      inputForm["_id"] = inputFormId["id"]

      $(this).find(".form-control").each(function(j) {
        inputFormProperty = $(this).serializeArray()[0]
        console.log(inputFormProperty)
        inputForm[inputFormProperty.keys()[0]] = inputFormProperty.values()[0]
      })

      allInputsForm.push(inputForm)
    })

    console.log(JSON.stringify(allInputsForm))
    $.ajax({
      dataType: 'json',
      contentType:"application/json",
      data: JSON.stringify(allInputsForm),
      type: 'POST',
      url : '/update_input'
    })
    .done(function(data){
      if (data.error){
        alert("OHNO")
      }
      else {
        alert(data)
      }
    })

    e.preventDefault();
  });

});

