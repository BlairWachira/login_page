function check(event) {
  in_user = document.getElementById("username_id").value
  in_pass = document.getElementById("pass_id").value
  if (in_user == "" || in_pass == "") {
    alert("please fill in the fields")
    event.preventDefault();
  }
}
document.getElementById("login_button").addEventListener("click", check)