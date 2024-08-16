const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/lingling.jpeg") {
    myImage.setAttribute("src", "images/lingling2.jpeg");
  } else {
    myImage.setAttribute("src", "images/lingling.jpeg");
  }
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
      setUserName();
    } else {
      localStorage.setItem("name", myName);
      myHeading.textContent = `Lingling is cool, ${myName}`;
    }
  }

if (!localStorage.getItem("name")) {
setUserName();
} else {
const storedName = localStorage.getItem("name");
myHeading.textContent = `Lingling is cool, ${storedName}`;
}

myButton.onclick = () => {
    setUserName();
};