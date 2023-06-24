


function toggle(self) {
    checkboxes = document.getElementsByName(self.name);
    for(var i=0, n=checkboxes.length;i<n;i++) {
        checkboxes[i].checked = self.checked;
        sub(checkboxes[i])
      }
    }

function sub(self) {
    subcheckboxes = document.getElementsByClassName(self.class);
    for(var i=0, n=subcheckboxes.length;i<n;i++) {
        subcheckboxes[i].checked = self.checked;
      }
}

function test(checkboxes, t) {
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

function n(self) {
    let t=document.getElementById('all-categories')
    checkboxes = document.getElementsByName(self.name);
    sub(self)
    test(checkboxes, t)
}

function subn(self) {
    let t=document.getElementById('category')
    checkboxes = document.getElementsByName(self.name);
    test(checkboxes, t)
}