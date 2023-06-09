


function toggle(source) {
    checkboxes = document.getElementsByName('category');
    for(var i=0, n=checkboxes.length;i<n;i++) {
        checkboxes[i].checked = source.checked;
      }
  }

function n() {
    t=document.getElementById('all-categories')
    checkboxes = document.getElementsByName('category');
    let count = 0
    for(var i=0, n=checkboxes.length;i<n;i++) {
        if (checkboxes[i].checked == false){
            count += 1
        }
    }
    if (count==0){
        t.checked = true
    }
    else{
        t.checked = false
    }

}