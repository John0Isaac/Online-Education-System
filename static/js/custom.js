// the selector will match all input controls of type :checkbox
// and attach a click event handler 
$("input:checkbox").on('click', function() {
  // in the handler, 'this' refers to the box clicked on
  var $box = $(this);
  if ($box.is(":checked")) {
    // the name of the box is retrieved using the .attr() method
    // as it is assumed and expected to be immutable
    var group = "input:checkbox[name='" + $box.attr("name") + "']";
    // the checked state of the group/box on the other hand will change
    // and the current value is retrieved using .prop() method
    $(group).prop("checked", false);
    $box.prop("checked", true);
  } else {
    $box.prop("checked", false);
  }
});


// Get Data, time to display it
var dt = new Date();
document.getElementById("datetime").innerHTML = dt.toLocaleString();

const descInput = document.getElementById('description');
      document.getElementById('form').onsubmit = function(e) {
        e.preventDefault();
        const desc = descInput.value;
        descInput.value = '';
        fetch('/todos/create', {
          method: 'POST',
          body: JSON.stringify({
            'description': desc,
          }),
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .then(response => response.json())
        .then(jsonResponse => {
          const li = document.createElement('li');
          const checkbox = document.createElement('input');
          checkbox.className = 'check-completed';
          checkbox.type = 'checkbox';
          checkbox.setAttribute('data-id', jsonResponse.id);
          li.appendChild(checkbox);
        })
      }