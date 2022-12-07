document.cookie = "name=oeschger; SameSite=None; Secure";
document.cookie = "favorite_food=tripe; SameSite=None; Secure";

function showCookies() {
  const output = document.getElementById('cookies')
  output.textContent = `> ${document.cookie}`
}

function clearOutputCookies() {
  const output = document.getElementById('cookies')
  output.textContent = ''
}