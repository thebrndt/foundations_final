const hamburger = document.querySelector(".hamburger");
const navBar = document.querySelector(".navbar");

const member = document.querySelector(".already-member");
const nonMember = document.querySelector(".not-member");

var signUpSection = document.querySelector(".join-signup-section")
var loginSection = document.querySelector(".join-login-section")

// Funtions for Responsive Navigation in Mobile View to toggle
// the Hamburger Menu
function toggleNavActive() {
    navBar.classList.toggle("active");
}
hamburger.addEventListener('click', function(){
    toggleNavActive()
})

// Funtions for Join Page to diplay content according to what
//  the user needs: either to sign-up or to sign-in
function removeSignUp() {
    signUpSection.style.display = "none";
}
function displaySignUp() {
    signUpSection.style.display = "block";
}
function removeLogin() {
    loginSection.style.display = "none";
}
function displayLogin() {
    loginSection.style.display = "block";
}

removeLogin()

member.addEventListener('click', ()=>{
    removeSignUp();
    displayLogin();
});
nonMember.addEventListener('click', ()=>{
    removeLogin();
    displaySignUp();
});